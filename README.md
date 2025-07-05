# awt-odoo-addons-dev-guide

[最佳實踐指南]（https://github.com/t-s-li/awt-odoo-addons-dev-guide/blob/main/best%20practice.md)
[使用 xStudio 加欄位 vs 自寫addon加欄位，比對 優缺點]()
[]()
[多個模組一次比對](https://github.com/t-s-li/awt-odoo-addons-dev-guide/blob/main/odoo_model_diff_multi_module.py)
✅ 支援「多個模組一次比對」的更新版腳本已完成：

📄 點此下載 odoo_model_diff_multi_module.py

⸻

🔧 使用方式（支援多模組）
	1.	修改這幾行為你的實際路徑與模組清單：

base_path_odoo17 = '/your/path/to/odoo17/addons'
base_path_odoo18 = '/your/path/to/odoo18/addons'
modules = ['sale', 'purchase', 'account']

	2.	執行指令：

python odoo_model_diff_multi_module.py

	3.	輸出結果：

	•	./model_diff_output/model_diff_report.md：所有模組欄位變動的 Markdown 報告
	•	./model_diff_output/model_diff_report.csv：欄位變動表格，適用於 Excel

⸻

需要我幫你做成 HTML 可預覽版報告嗎？或想支援更精細的欄位屬性變更（如 readonly, domain 差異）也可以！ ￼
