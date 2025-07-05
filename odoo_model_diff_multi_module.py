
import os
import ast
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, Tuple, List

# Represents a field with its type and arguments (for deeper comparison)
class FieldDef:
    def __init__(self, field_type: str, args: List[str], keywords: Dict[str, str]):
        self.field_type = field_type
        self.args = args
        self.keywords = keywords

    def __eq__(self, other):
        return (
            self.field_type == other.field_type and
            self.args == other.args and
            self.keywords == other.keywords
        )

    def __hash__(self):
        return hash((self.field_type, tuple(self.args), tuple(sorted(self.keywords.items()))))

    def __repr__(self):
        kw_str = ', '.join(f'{k}={v}' for k, v in self.keywords.items())
        return f"{self.field_type}({', '.join(self.args + [kw_str])})"

# Parse field definitions in Python source files using AST
def parse_field_definitions(py_file: str) -> Dict[str, Dict[str, FieldDef]]:
    with open(py_file, 'r', encoding='utf-8') as f:
        source = f.read()
    node = ast.parse(source, filename=py_file)

    model_fields = defaultdict(dict)

    class ModelFieldVisitor(ast.NodeVisitor):
        def visit_ClassDef(self, class_node):
            is_model = any(
                isinstance(base, ast.Attribute) and base.attr == 'Model'
                for base in class_node.bases
            )
            if is_model:
                model_name = class_node.name
                for stmt in class_node.body:
                    if isinstance(stmt, ast.Assign):
                        target = stmt.targets[0]
                        if isinstance(target, ast.Name) and isinstance(stmt.value, ast.Call):
                            try:
                                field_type = (
                                    stmt.value.func.attr if isinstance(stmt.value.func, ast.Attribute)
                                    else stmt.value.func.id
                                )
                            except Exception:
                                continue
                            args = [ast.unparse(arg) for arg in stmt.value.args]
                            keywords = {kw.arg: ast.unparse(kw.value) for kw in stmt.value.keywords}
                            model_fields[model_name][target.id] = FieldDef(field_type, args, keywords)
            self.generic_visit(class_node)

    ModelFieldVisitor().visit(node)
    return model_fields

# Collect model fields from module directory
def collect_models(base_dir: str) -> Dict[str, Dict[str, FieldDef]]:
    models = defaultdict(dict)
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py') and 'models' in root:
                try:
                    file_path = os.path.join(root, file)
                    model_data = parse_field_definitions(file_path)
                    for model_name, fields in model_data.items():
                        models[model_name].update(fields)
                except Exception:
                    continue
    return models

# Compare fields with details
def compare_model_fields(
    old_models: Dict[str, Dict[str, FieldDef]],
    new_models: Dict[str, Dict[str, FieldDef]]
) -> Dict[str, Dict[str, List[str]]]:
    all_models = set(old_models.keys()).union(new_models.keys())
    changes = {}

    for model in all_models:
        old_fields = old_models.get(model, {})
        new_fields = new_models.get(model, {})
        added = []
        removed = []
        modified = []

        for fname in old_fields:
            if fname not in new_fields:
                removed.append(fname)
            elif old_fields[fname] != new_fields[fname]:
                modified.append(fname)

        for fname in new_fields:
            if fname not in old_fields:
                added.append(fname)

        if added or removed or modified:
            changes[model] = {
                'added': added,
                'removed': removed,
                'modified': modified
            }

    return changes

# Export result as markdown and CSV
def export_diff_to_markdown_csv(
    diffs: Dict[str, Dict[str, List[str]]],
    models_v17: Dict[str, Dict[str, FieldDef]],
    models_v18: Dict[str, Dict[str, FieldDef]],
    output_dir: str
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    md_path = output_dir / "model_diff_report.md"
    csv_path = output_dir / "model_diff_report.csv"

    with md_path.open("w", encoding="utf-8") as md, csv_path.open("w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Model", "Change Type", "Field Name", "Odoo 17 Definition", "Odoo 18 Definition"])

        for model, change in diffs.items():
            md.write(f"## 🔍 Model: `{model}`\n\n")
            for change_type in ["added", "removed", "modified"]:
                if change[change_type]:
                    md.write(f"### {'➕' if change_type == 'added' else '➖' if change_type == 'removed' else '🔄'} {change_type.capitalize()} Fields:\n\n")
                    md.write("| Field | Odoo 17 | Odoo 18 |\n")
                    md.write("|-------|---------|---------|\n")

                    for f in change[change_type]:
                        def17 = str(models_v17.get(model, {}).get(f, '')) if change_type != "added" else ''
                        def18 = str(models_v18.get(model, {}).get(f, '')) if change_type != "removed" else ''
                        md.write(f"| `{f}` | `{def17}` | `{def18}` |\n")
                        csv_writer.writerow([model, change_type, f, def17, def18])
                    md.write("\n")

    return str(md_path), str(csv_path)

# === MAIN EXECUTION ===
if __name__ == '__main__':
    # 🔧 Define base paths and module list
    base_path_odoo17 = '/Users/tsli/Documents/GitHub/odoo-17.0+e.20250705/odoo/addons'
    base_path_odoo18 = '/Users/tsli/Documents/GitHub/odoo-18.0+e.20250705/odoo/addons'
    modules = ['sale', 'purchase', 'account']
    output_dir = './model_diff_output'

    all_v17 = {}
    all_v18 = {}
    for module in modules:
        path_odoo17 = os.path.join(base_path_odoo17, module)
        path_odoo18 = os.path.join(base_path_odoo18, module)
        print(f"🔍 Scanning module: {module}")
        models_v17 = collect_models(path_odoo17)
        models_v18 = collect_models(path_odoo18)
        all_v17.update(models_v17)
        all_v18.update(models_v18)

    print("📊 Comparing fields across all modules...")
    diffs = compare_model_fields(all_v17, all_v18)
    print("📝 Exporting report...")
    md_file, csv_file = export_diff_to_markdown_csv(diffs, all_v17, all_v18, output_dir)

    print(f"✅ Done. Markdown: {md_file}")
    print(f"📄 CSV: {csv_file}")
