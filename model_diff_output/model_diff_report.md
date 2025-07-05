## 🔍 Model: `AccountMoveLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `journal_group_id` | `` | `Many2one(string='Ledger', comodel_name='account.journal.group', store=False, search='_search_journal_group_id')` |
| `account_name` | `` | `Char(related='account_id.name')` |
| `account_code` | `` | `Char(related='account_id.code')` |
| `is_imported` | `` | `Boolean()` |
| `commercial_partner_country` | `` | `Many2one(string='Commercial Partner Country', related='move_id.commercial_partner_id.country_id')` |
| `product_category_id` | `` | `Many2one(related='product_id.product_tmpl_id.categ_id')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `tax_key` | `Binary(compute='_compute_tax_key', exportable=False)` | `` |
| `compute_all_tax` | `Binary(compute='_compute_all_tax', exportable=False)` | `` |
| `compute_all_tax_dirty` | `Boolean(compute='_compute_all_tax')` | `` |
| `blocked` | `Boolean(string='No Follow-up', default=False, help='You can check this box to mark this journal item as a litigation with the associated partner')` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `date` | `Date(related='move_id.date', store=True, copy=False, group_operator='min')` | `Date(related='move_id.date', store=True, copy=False, aggregator='min')` |
| `invoice_date` | `Date(related='move_id.invoice_date', store=True, copy=False, group_operator='min')` | `Date(related='move_id.invoice_date', store=True, copy=False, aggregator='min')` |
| `amount_currency` | `Monetary(string='Amount in Currency', group_operator=None, compute='_compute_amount_currency', inverse='_inverse_amount_currency', store=True, readonly=False, precompute=True, help='The amount expressed in an optional other currency if it is a multi-currency entry.')` | `Monetary(string='Amount in Currency', compute='_compute_amount_currency', inverse='_inverse_amount_currency', store=True, readonly=False, precompute=True, help='The amount expressed in an optional other currency if it is a multi-currency entry.')` |
| `payment_id` | `Many2one(comodel_name='account.payment', string='Originator Payment', related='move_id.payment_id', store=True, auto_join=True, index='btree_not_null', help='The payment that created this entry')` | `Many2one(comodel_name='account.payment', string='Originator Payment', related='move_id.origin_payment_id', store=True, auto_join=True, index='btree_not_null', help='The payment that created this entry')` |
| `amount_residual_currency` | `Monetary(string='Residual Amount in Currency', compute='_compute_amount_residual', store=True, group_operator=None, help='The residual amount on a journal item expressed in its currency (possibly not the company currency).')` | `Monetary(string='Residual Amount in Currency', compute='_compute_amount_residual', store=True, aggregator=None, help='The residual amount on a journal item expressed in its currency (possibly not the company currency).')` |
| `account_root_id` | `Many2one(related='account_id.root_id', string='Account Root', store=True)` | `Many2one(related='account_id.root_id', string='Account Root', depends_context='company')` |
| `discount_date` | `Date(string='Discount Date', store=True, help='Last date at which the discounted amount must be paid in order for the Early Payment Discount to be granted')` | `Date(string='Discount Date', store=True, help='Last date at which the discounted amount must be paid in order for the Early Payment Discount to be granted', readonly=True)` |
| `discount_amount_currency` | `Monetary(string='Discount amount in Currency', store=True, currency_field='currency_id', group_operator=None)` | `Monetary(string='Discount amount in Currency', store=True, currency_field='currency_id', aggregator=None)` |
| `payment_date` | `Date(string='Payment Date', compute='_compute_payment_date', search='_search_payment_date')` | `Date(string='Next Payment Date', compute='_compute_payment_date', search='_search_payment_date')` |

## 🔍 Model: `AccountJournalGroup`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `name` | `Char('Journal Group', required=True, translate=True)` | `Char('Ledger group', required=True, translate=True)` |
| `company_id` | `Many2one('res.company', required=True, default=lambda self: self.env.company)` | `Many2one(comodel_name='res.company', help='Define which company can select the multi-ledger in report filters. If none is provided, available for all companies', default=lambda self: self.env.company)` |
| `excluded_journal_ids` | `Many2many('account.journal', string='Excluded Journals', check_company=True)` | `Many2many('account.journal', string='Excluded Journals')` |

## 🔍 Model: `AccountReconcileModelLine`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `account_id` | `Many2one('account.account', string='Account', ondelete='cascade', domain="[('deprecated', '=', False), ('account_type', '!=', 'off_balance')]", required=True, check_company=True)` | `Many2one('account.account', string='Account', ondelete='cascade', domain="[('deprecated', '=', False), ('account_type', '!=', 'off_balance')]", check_company=True)` |
| `journal_id` | `Many2one('account.journal', string='Journal', ondelete='cascade', domain="[('type', '=', 'general')]", check_company=True)` | `Many2one(comodel_name='account.journal', string='Journal', ondelete='cascade', check_company=True, store=True, readonly=False, compute='_compute_journal_id')` |
| `amount_type` | `Selection([('fixed', 'Fixed'), ('percentage', 'Percentage of balance'), ('percentage_st_line', 'Percentage of statement line'), ('regex', 'From label')], required=True, default='percentage')` | `Selection(selection=[('fixed', 'Fixed'), ('percentage', 'Percentage of balance'), ('percentage_st_line', 'Percentage of statement line'), ('regex', 'From label')], required=True, store=True, precompute=True, compute='_compute_amount_type', readonly=False)` |
| `tax_ids` | `Many2many('account.tax', string='Taxes', ondelete='restrict', check_company=True)` | `Many2many(comodel_name='account.tax', string='Taxes', ondelete='restrict', check_company=True, compute='_compute_tax_ids', readonly=False, store=True)` |

## 🔍 Model: `AccountReconcileModel`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `counterpart_type` | `` | `Selection(selection=[('general', 'Journal Entry'), ('sale', 'Customer Invoices'), ('purchase', 'Vendor Bills')], string='Counterpart Type', default='general')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `match_journal_ids` | `Many2many('account.journal', string='Journals Availability', domain="[('type', 'in', ('bank', 'cash'))]", check_company=True, help='The reconciliation model will only be available from the selected journals.')` | `Many2many('account.journal', string='Journals Availability', domain="[('type', 'in', ('bank', 'cash', 'credit'))]", check_company=True, help='The reconciliation model will only be available from the selected journals.')` |
| `decimal_separator` | `Char(default=lambda self: self.env['res.lang']._lang_get(self.env.user.lang).decimal_point, tracking=True, help='Every character that is nor a digit nor this separator will be removed from the matching string')` | `Char(default=lambda self: self.env['res.lang']._get_data(code=self.env.user.lang).decimal_point, tracking=True, help='Every character that is nor a digit nor this separator will be removed from the matching string')` |

## 🔍 Model: `ProductDocument`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `attached_on_sale` | `` | `Selection(selection=[('hidden', 'Hidden'), ('quotation', 'On quote'), ('sale_order', 'On confirmed order')], required=True, default='hidden', string='Sale : Visible at', help='Allows you to share the document with your customers within a sale.\nOn quote: the document will be sent to and accessible by customers at any time.\ne.g. this option can be useful to share Product description files.\nOn order confirmation: the document will be sent to and accessible by customers.\ne.g. this option can be useful to share User Manual or digital content bought on ecommerce. ', groups='sales_team.group_sale_salesman')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `attached_on` | `Selection(selection=[('quotation', 'Quotation'), ('sale_order', 'Confirmed order')], string='Visible at', help="Allows you to share the document with your customers within a sale.\nLeave it empty if you don't want to share this document with sales customer.\nQuotation: the document will be sent to and accessible by customers at any time.\ne.g. this option can be useful to share Product description files.\nConfirmed order: the document will be sent to and accessible by customers.\ne.g. this option can be useful to share User Manual or digital content bought on ecommerce. ")` | `` |

## 🔍 Model: `PurchaseOrder`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `partner_bill_count` | `` | `Integer(related='partner_id.supplier_invoice_count')` |
| `amount_total_cc` | `` | `Monetary(string='Company Total', store=True, readonly=True, compute='_amount_all', currency_field='company_currency_id')` |
| `company_currency_id` | `` | `Many2one(related='company_id.currency_id', string='Company Currency')` |
| `company_price_include` | `` | `Selection(related='company_id.account_price_include')` |
| `mail_reception_declined` | `` | `Boolean('Reception Declined', readonly=True, copy=False, help='True if PO reception is declined by the vendor.')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `currency_rate` | `Float('Currency Rate', compute='_compute_currency_rate', compute_sudo=True, store=True, readonly=True, help='Ratio between the purchase order currency and the company currency')` | `Float(string='Currency Rate', compute='_compute_currency_rate', digits=0, store=True, precompute=True)` |

## 🔍 Model: `Message`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `account_audit_log_preview` | `` | `Text(string='Description', compute='_compute_account_audit_log_preview')` |
| `account_audit_log_move_id` | `` | `Many2one(comodel_name='account.move', string='Journal Entry', compute='_compute_account_audit_log_move_id', search='_search_account_audit_log_move_id')` |
| `account_audit_log_partner_id` | `` | `Many2one(comodel_name='res.partner', string='Partner', compute='_compute_account_audit_log_partner_id', search='_search_account_audit_log_partner_id')` |
| `account_audit_log_account_id` | `` | `Many2one(comodel_name='account.account', string='Account', compute='_compute_account_audit_log_account_id', search='_search_account_audit_log_account_id')` |
| `account_audit_log_tax_id` | `` | `Many2one(comodel_name='account.tax', string='Tax', compute='_compute_account_audit_log_tax_id', search='_search_account_audit_log_tax_id')` |
| `account_audit_log_company_id` | `` | `Many2one(comodel_name='res.company', string='Company ', compute='_compute_account_audit_log_company_id', search='_search_account_audit_log_company_id')` |
| `account_audit_log_activated` | `` | `Boolean(string='Audit Log Activated', compute='_compute_account_audit_log_activated', search='_search_account_audit_log_activated')` |

## 🔍 Model: `PurchaseOrderLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `is_downpayment` | `` | `Boolean()` |
| `product_template_attribute_value_ids` | `` | `Many2many(related='product_id.product_template_attribute_value_ids', readonly=True)` |
| `product_no_variant_attribute_value_ids` | `` | `Many2many('product.template.attribute.value', string='Product attribute values that do not create variants', ondelete='restrict')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `product_id` | `Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)], change_default=True, index='btree_not_null')` | `Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)], change_default=True, index='btree_not_null', ondelete='restrict')` |
| `product_type` | `Selection(related='product_id.detailed_type', readonly=True)` | `Selection(related='product_id.type', readonly=True)` |
| `price_unit` | `Float(string='Unit Price', required=True, digits='Product Price', compute='_compute_price_unit_and_date_planned_and_name', readonly=False, store=True)` | `Float(string='Unit Price', required=True, digits='Product Price', aggregator='avg', compute='_compute_price_unit_and_date_planned_and_name', readonly=False, store=True)` |
| `price_subtotal` | `Monetary(compute='_compute_amount', string='Subtotal', store=True)` | `Monetary(compute='_compute_amount', string='Subtotal', aggregator=None, store=True)` |

## 🔍 Model: `AccountCodeMapping`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `account_id` | `` | `Many2one(comodel_name='account.account', string='Account', compute='_compute_account_id', search=True)` |
| `company_id` | `` | `Many2one(comodel_name='res.company', string='Company', compute='_compute_company_id', readonly=False)` |
| `code` | `` | `Char(string='Code', compute='_compute_code', inverse='_inverse_code')` |

## 🔍 Model: `ProductTemplate`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `taxes_id` | `Many2many('account.tax', 'product_taxes_rel', 'prod_id', 'tax_id', help='Default taxes used when selling the product.', string='Customer Taxes', domain=[('type_tax_use', '=', 'sale')], default=lambda self: self.env.companies.account_sale_tax_id or self.env.companies.root_id.sudo().account_sale_tax_id)` | `Many2many('account.tax', 'product_taxes_rel', 'prod_id', 'tax_id', string='Sales Taxes', help='Default taxes used when selling the product', domain=[('type_tax_use', '=', 'sale')], default=lambda self: self.env.companies.account_sale_tax_id or self.env.companies.root_id.sudo().account_sale_tax_id)` |
| `supplier_taxes_id` | `Many2many('account.tax', 'product_supplier_taxes_rel', 'prod_id', 'tax_id', string='Vendor Taxes', help='Default taxes used when buying the product.', domain=[('type_tax_use', '=', 'purchase')], default=lambda self: self.env.companies.account_purchase_tax_id or self.env.companies.root_id.sudo().account_purchase_tax_id)` | `Many2many('account.tax', 'product_supplier_taxes_rel', 'prod_id', 'tax_id', string='Purchase Taxes', help='Default taxes used when buying the product', domain=[('type_tax_use', '=', 'purchase')], default=lambda self: self.env.companies.account_purchase_tax_id or self.env.companies.root_id.sudo().account_purchase_tax_id)` |
| `property_account_income_id` | `Many2one('account.account', company_dependent=True, string='Income Account', domain=ACCOUNT_DOMAIN, help='Keep this field empty to use the default value from the product category.')` | `Many2one('account.account', company_dependent=True, ondelete='restrict', string='Income Account', domain=ACCOUNT_DOMAIN, help='Keep this field empty to use the default value from the product category.')` |
| `property_account_expense_id` | `Many2one('account.account', company_dependent=True, string='Expense Account', domain=ACCOUNT_DOMAIN, help='Keep this field empty to use the default value from the product category. If anglo-saxon accounting with automated valuation method is configured, the expense account on the product category will be used.')` | `Many2one('account.account', company_dependent=True, ondelete='restrict', string='Expense Account', domain=ACCOUNT_DOMAIN, help='Keep this field empty to use the default value from the product category. If anglo-saxon accounting with automated valuation method is configured, the expense account on the product category will be used.')` |

## 🔍 Model: `ResPartner`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `partner_vat_placeholder` | `` | `Char(compute='_compute_partner_vat_placeholder')` |
| `partner_company_registry_placeholder` | `` | `Char(compute='_compute_partner_company_registry_placeholder')` |
| `duplicate_bank_partner_ids` | `` | `Many2many(related='bank_ids.duplicate_bank_partner_ids')` |
| `ignore_abnormal_invoice_date` | `` | `Boolean(company_dependent=True)` |
| `ignore_abnormal_invoice_amount` | `` | `Boolean(company_dependent=True)` |
| `invoice_sending_method` | `` | `Selection(string='Invoice sending', selection=[('manual', 'Download'), ('email', 'by Email')], company_dependent=True)` |
| `invoice_edi_format` | `` | `Selection(string='eInvoice format', selection=[], compute='_compute_invoice_edi_format', inverse='_inverse_invoice_edi_format', compute_sudo=True)` |
| `invoice_edi_format_store` | `` | `Char(company_dependent=True)` |
| `display_invoice_edi_format` | `` | `Boolean(default=lambda self: len(self._fields['invoice_edi_format'].selection), store=False)` |
| `invoice_template_pdf_report_id` | `` | `Many2one(comodel_name='ir.actions.report', string='Invoice template', domain="[('is_invoice_report', '=', True)]", readonly=False, store=True)` |
| `display_invoice_template_pdf_report_id` | `` | `Boolean(default=_default_display_invoice_template_pdf_report_id, store=False)` |
| `autopost_bills` | `` | `Selection(selection=[('always', 'Always'), ('ask', 'Ask after 3 validations without edits'), ('never', 'Never')], string='Auto-post bills', help='Automatically post bills for this trusted partner', default='ask', required=True)` |
| `property_outbound_payment_method_line_id` | `` | `Many2one(comodel_name='account.payment.method.line', company_dependent=True, domain=lambda self: [('payment_type', '=', 'outbound'), ('company_id', '=', self.env.company.id)], help='Preferred payment method when buying from this vendor. This will be set by default on all outgoing payments created for this vendor')` |
| `property_inbound_payment_method_line_id` | `` | `Many2one(comodel_name='account.payment.method.line', company_dependent=True, domain=lambda self: [('payment_type', '=', 'inbound'), ('company_id', '=', self.env.company.id)], help='Preferred payment method when selling to this customer. This will be set by default on all incoming payments created for this customer')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `has_unreconciled_entries` | `Boolean(compute='_compute_has_unreconciled_entries', help='The partner has at least one unreconciled debit and credit since last time the invoices & payments matching was performed.')` | `` |
| `last_time_entries_checked` | `Datetime(string='Latest Invoices & Payments Matching Date', readonly=True, copy=False, help='Last time the invoices & payments matching was performed for this partner. It is set either if there\'s not at least an unreconciled debit and an unreconciled credit or if you click the "Done" button.')` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `property_account_payable_id` | `Many2one('account.account', company_dependent=True, string='Account Payable', domain="[('account_type', '=', 'liability_payable'), ('deprecated', '=', False)]", help='This account will be used instead of the default one as the payable account for the current partner', required=True)` | `Many2one('account.account', company_dependent=True, string='Account Payable', domain="[('account_type', '=', 'liability_payable'), ('deprecated', '=', False)]", help='This account will be used instead of the default one as the payable account for the current partner', ondelete='restrict')` |
| `property_account_receivable_id` | `Many2one('account.account', company_dependent=True, string='Account Receivable', domain="[('account_type', '=', 'asset_receivable'), ('deprecated', '=', False)]", help='This account will be used instead of the default one as the receivable account for the current partner', required=True)` | `Many2one('account.account', company_dependent=True, string='Account Receivable', domain="[('account_type', '=', 'asset_receivable'), ('deprecated', '=', False)]", help='This account will be used instead of the default one as the receivable account for the current partner', ondelete='restrict')` |
| `property_payment_term_id` | `Many2one('account.payment.term', company_dependent=True, string='Customer Payment Terms', help='This payment term will be used instead of the default one for sales orders and customer invoices')` | `Many2one('account.payment.term', company_dependent=True, string='Customer Payment Terms', help='This payment term will be used instead of the default one for sales orders and customer invoices', ondelete='restrict')` |
| `trust` | `Selection([('good', 'Good Debtor'), ('normal', 'Normal Debtor'), ('bad', 'Bad Debtor')], string='Degree of trust you have in this debtor', default='normal', company_dependent=True)` | `Selection([('good', 'Good Debtor'), ('normal', 'Normal Debtor'), ('bad', 'Bad Debtor')], string='Degree of trust you have in this debtor', company_dependent=True)` |

## 🔍 Model: `SaleOrderLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `is_configurable_product` | `` | `Boolean(string='Is the product configurable?', related='product_template_id.has_configurable_attributes', depends=['product_id'])` |
| `product_template_attribute_value_ids` | `` | `Many2many(related='product_id.product_template_attribute_value_ids', depends=['product_id'])` |
| `is_product_archived` | `` | `Boolean(compute='_compute_is_product_archived')` |
| `translated_product_name` | `` | `Text(compute='_compute_translated_product_name')` |
| `linked_line_id` | `` | `Many2one(string='Linked Order Line', comodel_name='sale.order.line', ondelete='cascade', domain="[('order_id', '=', order_id)]", copy=False, index=True)` |
| `linked_line_ids` | `` | `One2many(string='Linked Order Lines', comodel_name='sale.order.line', inverse_name='linked_line_id')` |
| `virtual_id` | `` | `Char()` |
| `linked_virtual_id` | `` | `Char()` |
| `selected_combo_items` | `` | `Char(store=False)` |
| `combo_item_id` | `` | `Many2one(comodel_name='product.combo.item')` |
| `technical_price_unit` | `` | `Float()` |
| `qty_invoiced_posted` | `` | `Float(string='Invoiced Quantity (posted)', compute='_compute_qty_invoiced_posted', digits='Product Unit of Measure')` |
| `amount_invoiced` | `` | `Monetary(string='Invoiced Amount', compute='_compute_amount_invoiced', compute_sudo=True)` |
| `amount_to_invoice` | `` | `Monetary(string='Un-invoiced Balance', compute='_compute_amount_to_invoice', compute_sudo=True)` |
| `service_tracking` | `` | `Selection(related='product_id.service_tracking', depends=['product_id'])` |
| `company_price_include` | `` | `Selection(related='company_id.account_price_include')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `product_type` | `Selection(related='product_id.detailed_type', depends=['product_id'])` | `Selection(related='product_id.type', depends=['product_id'])` |

## 🔍 Model: `AccountReportLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `horizontal_split_side` | `` | `Selection(string='Horizontal Split Side', selection=[('left', 'Left'), ('right', 'Right')], compute='_compute_horizontal_split_side', readonly=False, store=True, recursive=True)` |

## 🔍 Model: `AccountCashRounding`

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `company_id` | `Many2one('res.company', related='profit_account_id.company_id')` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `profit_account_id` | `Many2one('account.account', string='Profit Account', company_dependent=True, domain="[('deprecated', '=', False)]")` | `Many2one('account.account', string='Profit Account', company_dependent=True, check_company=True, domain="[('deprecated', '=', False), ('account_type', 'not in', ('asset_receivable', 'liability_payable'))]", ondelete='restrict')` |
| `loss_account_id` | `Many2one('account.account', string='Loss Account', company_dependent=True, domain="[('deprecated', '=', False)]")` | `Many2one('account.account', string='Loss Account', company_dependent=True, check_company=True, domain="[('deprecated', '=', False), ('account_type', 'not in', ('asset_receivable', 'liability_payable'))]", ondelete='restrict')` |

## 🔍 Model: `AccountRoot`

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `company_id` | `Many2one('res.company', )` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `name` | `Char()` | `Char(compute='_compute_root')` |
| `parent_id` | `Many2one('account.root', )` | `Many2one('account.root', compute='_compute_root')` |

## 🔍 Model: `CrmTeam`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `invoiced_target` | `Float(string='Invoicing Target', help='Revenue target for the current month (untaxed total of confirmed invoices).')` | `Float(string='Invoicing Target', help='Revenue Target for the current month (untaxed total of paid invoices).')` |

## 🔍 Model: `ResPartnerBank`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `duplicate_bank_partner_ids` | `` | `Many2many('res.partner', compute='_compute_duplicate_bank_partner_ids')` |

## 🔍 Model: `AccountReport`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `integer_rounding` | `` | `Selection(string='Integer Rounding', selection=[('HALF-UP', 'Nearest'), ('UP', 'Up'), ('DOWN', 'Down')])` |
| `currency_translation` | `` | `Selection(string='Currency Translation', selection=[('current', 'Use the most recent rate at the date of the report'), ('cta', 'Use CTA')], compute=lambda x: x._compute_report_option_filter('currency_translation', 'cta'), readonly=False, store=True, depends=['root_report_id', 'section_main_report_ids'])` |
| `filter_budgets` | `` | `Boolean(string='Budgets', compute=lambda x: x._compute_report_option_filter('filter_budgets'), readonly=False, store=True, depends=['root_report_id', 'section_main_report_ids'])` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `prefix_groups_threshold` | `Integer(string='Prefix Groups Threshold')` | `Integer(string='Prefix Groups Threshold', default=4000)` |
| `default_opening_date_filter` | `Selection(string='Default Opening', selection=[('this_year', 'This Year'), ('this_quarter', 'This Quarter'), ('this_month', 'This Month'), ('today', 'Today'), ('last_month', 'Last Month'), ('last_quarter', 'Last Quarter'), ('last_year', 'Last Year'), ('this_tax_period', 'This Tax Period'), ('last_tax_period', 'Last Tax Period')], compute=lambda x: x._compute_report_option_filter('default_opening_date_filter', 'last_month'), readonly=False, store=True, depends=['root_report_id', 'section_main_report_ids'])` | `Selection(string='Default Opening', selection=[('this_year', 'This Year'), ('this_quarter', 'This Quarter'), ('this_month', 'This Month'), ('today', 'Today'), ('previous_month', 'Last Month'), ('previous_quarter', 'Last Quarter'), ('previous_year', 'Last Year'), ('this_tax_period', 'This Tax Period'), ('previous_tax_period', 'Last Tax Period')], compute=lambda x: x._compute_report_option_filter('default_opening_date_filter', 'previous_month'), readonly=False, store=True, depends=['root_report_id', 'section_main_report_ids'])` |

## 🔍 Model: `IrActionsReport`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `is_invoice_report` | `` | `Boolean(string='Invoice report', copy=True)` |

## 🔍 Model: `ResCompany`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `sale_lock_date` | `` | `Date(string='Sales Lock Date', tracking=True, help="Any sales entry prior to and including this date will be postponed to a later date, in accordance with its journal's sequence.")` |
| `purchase_lock_date` | `` | `Date(string='Purchase Lock date', tracking=True, help="Any purchase entry prior to and including this date will be postponed to a later date, in accordance with its journal's sequence.")` |
| `hard_lock_date` | `` | `Date(string='Hard Lock Date', tracking=True, help='Any entry up to and including that date will be postponed to a later time, in accordance with its journal sequence. This lock date is irreversible and does not allow any exception.')` |
| `user_fiscalyear_lock_date` | `` | `Date(compute='_compute_user_fiscalyear_lock_date')` |
| `user_tax_lock_date` | `` | `Date(compute='_compute_user_tax_lock_date')` |
| `user_sale_lock_date` | `` | `Date(compute='_compute_user_sale_lock_date')` |
| `user_purchase_lock_date` | `` | `Date(compute='_compute_user_purchase_lock_date')` |
| `user_hard_lock_date` | `` | `Date(compute='_compute_user_hard_lock_date')` |
| `display_invoice_tax_company_currency` | `` | `Boolean(string='Taxes in company currency', default=True)` |
| `batch_payment_sequence_id` | `` | `Many2one(comodel_name='ir.sequence', readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].sudo().create({'name': _('Batch Payment Number Sequence'), 'implementation': 'no_gap', 'padding': 5, 'use_date_range': True, 'company_id': self.id, 'prefix': 'BATCH/%(year)s/'}))` |
| `check_account_audit_trail` | `` | `Boolean(string='Audit Trail')` |
| `autopost_bills` | `` | `Boolean(string='Auto-validate bills', default=True)` |
| `account_price_include` | `` | `Selection(selection=[('tax_included', 'Tax Included'), ('tax_excluded', 'Tax Excluded')], string='Default Sales Price Include', default='tax_excluded', required=True, help='Default on whether the sales price used on the product and invoices with this Company includes its taxes.')` |
| `company_vat_placeholder` | `` | `Char(compute='_compute_company_vat_placeholder')` |
| `company_registry_placeholder` | `` | `Char(compute='_compute_company_registry_placeholder')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `period_lock_date` | `Date(string='Journals Entries Lock Date', tracking=True, help="Only users with the 'Adviser' role can edit accounts prior to and inclusive of this date. Use it for period locking inside an open fiscal year, for example.")` | `` |
| `max_tax_lock_date` | `Date(compute='_compute_max_tax_lock_date', recursive=True)` | `` |
| `account_journal_payment_debit_account_id` | `Many2one('account.account', string='Journal Outstanding Receipts', check_company=True)` | `` |
| `account_journal_payment_credit_account_id` | `Many2one('account.account', string='Journal Outstanding Payments', check_company=True)` | `` |
| `invoice_is_email` | `Boolean('Email by default', default=True)` | `` |
| `invoice_is_download` | `Boolean('Download by default', default=True)` | `` |
| `country_code` | `Char(related='country_id.code', depends=['country_id'])` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `fiscalyear_lock_date` | `Date(string='All Users Lock Date', tracking=True, help='No users, including Advisers, can edit accounts prior to and inclusive of this date. Use it for fiscal year locking for example.')` | `Date(string='Global Lock Date', tracking=True, help="Any entry up to and including that date will be postponed to a later time, in accordance with its journal's sequence.")` |
| `tax_lock_date` | `Date(string='Tax Return Lock Date', tracking=True, help='No users can edit journal entries related to a tax prior and inclusive of this date.')` | `Date(string='Tax Return Lock Date', tracking=True, help="Any entry with taxes up to and including that date will be postponed to a later time, in accordance with its journal's sequence. The tax lock date is automatically set when the tax closing entry is posted.")` |
| `transfer_account_id` | `Many2one('account.account', check_company=True, domain="[('reconcile', '=', True), ('account_type', '=', 'asset_current'), ('deprecated', '=', False)]", string='Inter-Banks Transfer Account', help='Intermediary account used when moving money from a liqity account to another')` | `Many2one('account.account', check_company=True, domain="[('reconcile', '=', True), ('account_type', '=', 'asset_current'), ('deprecated', '=', False)]", string='Inter-Banks Transfer Account', help='Intermediary account used when moving money from a liquidity account to another')` |

## 🔍 Model: `AccountFiscalPosition`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `account_map` | `` | `Binary(compute='_compute_account_map')` |
| `tax_map` | `` | `Binary(compute='_compute_tax_map')` |

## 🔍 Model: `AccountGroup`

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `parent_path` | `Char(index=True, unaccent=False)` | `` |

## 🔍 Model: `SaleOrder`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `has_archived_products` | `` | `Boolean(compute='_compute_has_archived_products')` |
| `company_price_include` | `` | `Selection(related='company_id.account_price_include')` |
| `duplicated_order_ids` | `` | `Many2many(comodel_name='sale.order', compute='_compute_duplicated_order_ids')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `analytic_account_id` | `Many2one(comodel_name='account.analytic.account', string='Analytic Account', copy=False, check_company=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `locked` | `Boolean(default=False, copy=False, help='Locked orders cannot be modified.')` | `Boolean(help='Locked orders cannot be modified.', default=False, copy=False, tracking=True)` |
| `validity_date` | `Date(string='Expiration', compute='_compute_validity_date', store=True, readonly=False, copy=False, precompute=True)` | `Date(string='Expiration', help='Validity of the order, after that you will not able to sign & pay the quotation.', compute='_compute_validity_date', store=True, readonly=False, copy=False, precompute=True)` |
| `amount_to_invoice` | `Monetary(string='Amount to invoice', store=True, compute='_compute_amount_to_invoice')` | `Monetary(string='Un-invoiced Balance', compute='_compute_amount_to_invoice')` |
| `amount_invoiced` | `Monetary(string='Already invoiced', compute='_compute_amount_invoiced', compute_sudo=True)` | `Monetary(string='Already invoiced', compute='_compute_amount_invoiced')` |
| `amount_paid` | `Float(compute='_compute_amount_paid', compute_sudo=True)` | `Float(string='Payment Transactions Amount', help="Sum of transactions made in through the online payment form that are in the state 'done' or 'authorized' and linked to this order.", compute='_compute_amount_paid', compute_sudo=True)` |

## 🔍 Model: `PurchaseBillMatch`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `pol_id` | `` | `Many2one(comodel_name='purchase.order.line', readonly=True)` |
| `aml_id` | `` | `Many2one(comodel_name='account.move.line', readonly=True)` |
| `company_id` | `` | `Many2one(comodel_name='res.company', readonly=True)` |
| `partner_id` | `` | `Many2one(comodel_name='res.partner', readonly=True)` |
| `product_id` | `` | `Many2one(comodel_name='product.product', readonly=True)` |
| `line_qty` | `` | `Float(readonly=True)` |
| `line_uom_id` | `` | `Many2one(comodel_name='uom.uom', readonly=True)` |
| `qty_invoiced` | `` | `Float(readonly=True)` |
| `purchase_order_id` | `` | `Many2one(comodel_name='purchase.order', readonly=True)` |
| `account_move_id` | `` | `Many2one(comodel_name='account.move', readonly=True)` |
| `line_amount_untaxed` | `` | `Monetary(readonly=True)` |
| `currency_id` | `` | `Many2one(comodel_name='res.currency', readonly=True)` |
| `state` | `` | `Char(readonly=True)` |
| `product_uom_id` | `` | `Many2one(comodel_name='uom.uom', related='product_id.uom_id')` |
| `product_uom_qty` | `` | `Float(compute='_compute_product_uom_qty', inverse='_inverse_product_uom_qty', readonly=False)` |
| `product_uom_price` | `` | `Float(compute='_compute_product_uom_price', inverse='_inverse_product_uom_price', readonly=False)` |
| `billed_amount_untaxed` | `` | `Monetary(compute='_compute_amount_untaxed_fields', currency_field='currency_id')` |
| `purchase_amount_untaxed` | `` | `Monetary(compute='_compute_amount_untaxed_fields', currency_field='currency_id')` |
| `reference` | `` | `Char(compute='_compute_reference')` |

## 🔍 Model: `res_partner`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `purchase_order_count` | `Integer(compute='_compute_purchase_order_count', string='Purchase Order Count')` | `Integer(string='Purchase Order Count', groups='purchase.group_purchase_user', compute='_compute_purchase_order_count')` |
| `receipt_reminder_email` | `Boolean('Receipt Reminder', default=False, company_dependent=True, help='Automatically send a confirmation email to the vendor X days before the expected receipt date, asking him to confirm the exact date.')` | `Boolean('Receipt Reminder', company_dependent=True, help='Automatically send a confirmation email to the vendor X days before the expected receipt date, asking him to confirm the exact date.')` |
| `reminder_date_before_receipt` | `Integer('Days Before Receipt', default=1, company_dependent=True, help='Number of days to send reminder email before the promised receipt date')` | `Integer('Days Before Receipt', company_dependent=True, help='Number of days to send reminder email before the promised receipt date')` |

## 🔍 Model: `AccountBankStatementLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `journal_id` | `` | `Many2one(comodel_name='account.journal', inherited=True, related='move_id.journal_id', store=True, readonly=False, precompute=True, index=False, required=True)` |
| `company_id` | `` | `Many2one(comodel_name='res.company', inherited=True, related='move_id.company_id', store=True, readonly=False, precompute=True, index=False, required=True)` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `internal_index` | `Char(string='Internal Reference', compute='_compute_internal_index', store=True, index=True)` | `Char(string='Internal Reference', compute='_compute_internal_index', store=True)` |

## 🔍 Model: `AccountBankStatement`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `first_line_index` | `Char(comodel_name='account.bank.statement.line', compute='_compute_date_index', store=True, index=True)` | `Char(comodel_name='account.bank.statement.line', compute='_compute_date_index', store=True)` |
| `line_ids` | `One2many(comodel_name='account.bank.statement.line', inverse_name='statement_id', string='Statement lines', required=True)` | `One2many(comodel_name='account.bank.statement.line', inverse_name='statement_id', string='Statement lines')` |

## 🔍 Model: `AccountPaymentTermLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `display_days_next_month` | `` | `Boolean(compute='_compute_display_days_next_month')` |
| `days_next_month` | `` | `Char(string='Days on the next month', readonly=False, default='10', size=2)` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `delay_type` | `Selection([('days_after', 'Days after invoice date'), ('days_after_end_of_month', 'Days after end of month'), ('days_after_end_of_next_month', 'Days after end of next month')], required=True, default='days_after')` | `Selection([('days_after', 'Days after invoice date'), ('days_after_end_of_month', 'Days after end of month'), ('days_after_end_of_next_month', 'Days after end of next month'), ('days_end_of_month_on_the', 'Days end of month on the')], required=True, default='days_after')` |

## 🔍 Model: `AccountPaymentMethodLine`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `default_account_id` | `` | `Many2one(related='journal_id.default_account_id')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `payment_method_id` | `Many2one(string='Payment Method', comodel_name='account.payment.method', domain="[('payment_type', '=?', payment_type), ('id', 'in', available_payment_method_ids)]", required=True, ondelete='cascade')` | `Many2one(string='Payment Method', comodel_name='account.payment.method', domain="[('payment_type', '=?', payment_type), ('id', 'in', available_payment_method_ids)]", required=True)` |
| `payment_account_id` | `Many2one(comodel_name='account.account', check_company=True, copy=False, ondelete='restrict', domain="[('deprecated', '=', False), '|', ('account_type', 'in', ('asset_current', 'liability_current')), ('id', '=', parent.default_account_id)]")` | `Many2one(comodel_name='account.account', check_company=True, copy=False, ondelete='restrict', domain="[('deprecated', '=', False), '|', ('account_type', 'in', ('asset_current', 'liability_current')), ('id', '=', default_account_id)]")` |
| `journal_id` | `Many2one(comodel_name='account.journal', ondelete='cascade', check_company=True)` | `Many2one(comodel_name='account.journal', check_company=True)` |

## 🔍 Model: `AccountAnalyticApplicability`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `account_prefix_placeholder` | `` | `Char(compute='_compute_prefix_placeholder')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `account_prefix` | `Char(string='Financial Accounts Prefix', help='Prefix that defines which accounts from the financial accounting this applicability should apply on.')` | `Char(string='Financial Accounts Prefixes', help='Prefix that defines which accounts from the financial accounting this applicability should apply on.')` |

## 🔍 Model: `ResCurrency`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `fiscal_country_codes` | `Char(compute='_compute_fiscal_country_codes')` | `Char(store=False, default=_get_fiscal_country_codes)` |

## 🔍 Model: `AccountJournal`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `autocheck_on_post` | `` | `Boolean(string='Auto-Check on Post', default=True)` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `sale_activity_type_id` | `Many2one('mail.activity.type', string='Schedule Activity', default=False, help='Activity will be automatically scheduled on payment due date, improving collection process.')` | `` |
| `sale_activity_user_id` | `Many2one('res.users', string='Activity User', help='Leave empty to assign the Salesperson of the invoice.')` | `` |
| `sale_activity_note` | `Text('Activity Summary', )` | `` |
| `secure_sequence_id` | `Many2one('ir.sequence', help='Sequence to use to ensure the securisation of data', check_company=True, readonly=True, copy=False)` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `type` | `Selection([('sale', 'Sales'), ('purchase', 'Purchase'), ('cash', 'Cash'), ('bank', 'Bank'), ('general', 'Miscellaneous')], required=True, help="Select 'Sale' for customer invoices journals.\nSelect 'Purchase' for vendor bills journals.\nSelect 'Cash' or 'Bank' for journals that are used in customer or vendor payments.\nSelect 'General' for miscellaneous operations journals.")` | `Selection([('sale', 'Sales'), ('purchase', 'Purchase'), ('cash', 'Cash'), ('bank', 'Bank'), ('credit', 'Credit Card'), ('general', 'Miscellaneous')], required=True, help="\n        Select 'Sale' for customer invoices journals.\n        Select 'Purchase' for vendor bills journals.\n        Select 'Cash', 'Bank' or 'Credit Card' for journals that are used in customer or vendor payments.\n        Select 'General' for miscellaneous operations journals.\n        ")` |
| `restrict_mode_hash_table` | `Boolean(string='Lock Posted Entries with Hash', help='If ticked, the accounting entry or invoice receives a hash as soon as it is posted and cannot be modified anymore.')` | `Boolean(string='Secure Posted Entries with Hash', help='If ticked, when an entry is posted, we retroactively hash all moves in the sequence from the entry back to the last hashed entry. The hash can also be performed on demand by the Secure Entries wizard.')` |
| `refund_sequence` | `Boolean(string='Dedicated Credit Note Sequence', help="Check this box if you don't want to share the same sequence for invoices and credit notes made from this journal", default=False)` | `Boolean(string='Dedicated Credit Note Sequence', compute='_compute_refund_sequence', readonly=False, store=True, help="Check this box if you don't want to share the same sequence for invoices and credit notes made from this journal")` |
| `journal_group_ids` | `Many2many('account.journal.group', check_company=True, string='Journal Groups')` | `Many2many('account.journal.group', check_company=True, string='Ledger Group')` |

## 🔍 Model: `ProductCategory`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `property_account_income_categ_id` | `Many2one('account.account', company_dependent=True, string='Income Account', domain=ACCOUNT_DOMAIN, help='This account will be used when validating a customer invoice.')` | `Many2one('account.account', company_dependent=True, string='Income Account', domain=ACCOUNT_DOMAIN, help='This account will be used when validating a customer invoice.', tracking=True, ondelete='restrict')` |
| `property_account_expense_categ_id` | `Many2one('account.account', company_dependent=True, string='Expense Account', domain=ACCOUNT_DOMAIN, help='The expense is accounted for when a vendor bill is validated, except in anglo-saxon accounting with perpetual inventory valuation in which case the expense (Cost of Goods Sold account) is recognized at the customer invoice validation.')` | `Many2one('account.account', company_dependent=True, string='Expense Account', domain=ACCOUNT_DOMAIN, help='The expense is accounted for when a vendor bill is validated, except in anglo-saxon accounting with perpetual inventory valuation in which case the expense (Cost of Goods Sold account) is recognized at the customer invoice validation.', tracking=True, ondelete='restrict')` |

## 🔍 Model: `AccountAnalyticDistributionModel`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `prefix_placeholder` | `` | `Char(compute='_compute_prefix_placeholder')` |

## 🔍 Model: `AccountMove`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `name_placeholder` | `` | `Char(compute='_compute_name_placeholder')` |
| `journal_group_id` | `` | `Many2one('account.journal.group', string='Ledger', store=False, search='_search_journal_group_id')` |
| `origin_payment_id` | `` | `Many2one(comodel_name='account.payment', string='Payment', index='btree_not_null', copy=False, check_company=True)` |
| `matched_payment_ids` | `` | `Many2many(string='Matched Payments', comodel_name='account.payment', relation='account_move__account_payment', column1='invoice_id', column2='payment_id', copy=False)` |
| `payment_count` | `` | `Integer(compute='_compute_payment_count')` |
| `checked` | `` | `Boolean(string='Checked', tracking=True, help='If this checkbox is not ticked, it means that the user was not sure of all the related information at the time of the creation of the move and that the move needs to be checked again.')` |
| `made_sequence_gap` | `` | `Boolean(compute='_compute_made_sequence_gap', store=True)` |
| `company_price_include` | `` | `Selection(related='company_id.account_price_include', readonly=True)` |
| `audit_trail_message_ids` | `` | `One2many('mail.message', 'res_id', domain=[('model', '=', 'account.move'), ('message_type', '=', 'notification')], string='Audit Trail Messages')` |
| `secured` | `` | `Boolean(compute='_compute_secured', search='_search_secured', help='The entry is secured with an inalterable hash.')` |
| `preferred_payment_method_line_id` | `` | `Many2one(string='Preferred Payment Method Line', comodel_name='account.payment.method.line', compute='_compute_preferred_payment_method_line_id', store=True, readonly=False)` |
| `invoice_currency_rate` | `` | `Float(string='Currency Rate', compute='_compute_invoice_currency_rate', store=True, precompute=True, copy=False, digits=0, help='Currency rate from company currency to document currency.')` |
| `amount_untaxed_in_currency_signed` | `` | `Monetary(string='Untaxed Amount Signed Currency', compute='_compute_amount', store=True, readonly=True, currency_field='currency_id')` |
| `status_in_payment` | `` | `Selection(selection=PAYMENT_STATE_SELECTION + [('draft', 'Draft'), ('cancel', 'Cancelled')], compute='_compute_status_in_payment', copy=False)` |
| `reversal_move_ids` | `` | `One2many('account.move', 'reversed_entry_id', )` |
| `is_manually_modified` | `` | `Boolean()` |
| `move_sent_values` | `` | `Selection(selection=[('sent', 'Sent'), ('not_sent', 'Not Sent')], string='Sent', compute='compute_move_sent_values')` |
| `sending_data` | `` | `Json(copy=False)` |
| `abnormal_amount_warning` | `` | `Text(compute='_compute_abnormal_warnings')` |
| `abnormal_date_warning` | `` | `Text(compute='_compute_abnormal_warnings')` |
| `taxes_legal_notes` | `` | `Html(string='Taxes Legal Notes', compute='_compute_taxes_legal_notes')` |
| `next_payment_date` | `` | `Date(string='Next Payment Date', compute='_compute_next_payment_date', search='_search_next_payment_date')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `payment_id` | `Many2one(comodel_name='account.payment', string='Payment', index='btree_not_null', copy=False, check_company=True)` | `` |
| `to_check` | `Boolean(string='To Check', tracking=True, help='If this checkbox is ticked, it means that the user was not sure of all the related information at the time of the creation of the move and that the move needs to be checked again.')` | `` |
| `made_sequence_hole` | `Boolean(compute='_compute_made_sequence_hole')` | `` |
| `string_to_hash` | `Char(compute='_compute_string_to_hash', readonly=True)` | `` |
| `reversal_move_id` | `One2many('account.move', 'reversed_entry_id', )` | `` |
| `send_and_print_values` | `Json(copy=False)` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `secure_sequence_number` | `Integer(string='Inalteralbility No Gap Sequence #', readonly=True, copy=False, index=True)` | `Integer(string='Inalterability No Gap Sequence #', readonly=True, copy=False, index=True)` |
| `inalterable_hash` | `Char(string='Inalterability Hash', readonly=True, copy=False)` | `Char(string='Inalterability Hash', readonly=True, copy=False, index='btree_not_null')` |
| `delivery_date` | `Date(string='Delivery Date', copy=False, compute='_compute_delivery_date', store=True, readonly=False)` | `Date(string='Delivery Date', copy=False, store=True, compute='_compute_delivery_date', precompute=True, readonly=False)` |

## 🔍 Model: `AccountReportExpression`

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `date_scope` | `Selection(string='Date Scope', selection=[('from_beginning', 'From the very start'), ('from_fiscalyear', 'From the start of the fiscal year'), ('to_beginning_of_fiscalyear', 'At the beginning of the fiscal year'), ('to_beginning_of_period', 'At the beginning of the period'), ('normal', 'According to each type of account'), ('strict_range', 'Strictly on the given dates'), ('previous_tax_period', 'From previous tax period')], required=True, default='strict_range')` | `Selection(string='Date Scope', selection=[('from_beginning', 'From the very start'), ('from_fiscalyear', 'From the start of the fiscal year'), ('to_beginning_of_fiscalyear', 'At the beginning of the fiscal year'), ('to_beginning_of_period', 'At the beginning of the period'), ('strict_range', 'Strictly on the given dates'), ('previous_tax_period', 'From previous tax period')], required=True, default='strict_range')` |

## 🔍 Model: `account_journal`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `has_posted_entries` | `` | `Boolean(compute='_compute_has_entries')` |
| `has_entries` | `` | `Boolean(compute='_compute_has_entries')` |
| `has_unhashed_entries` | `` | `Boolean(string='Unhashed Entries', compute='_compute_has_unhashed_entries')` |

## 🔍 Model: `AccountAccount`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `company_fiscal_country_code` | `` | `Char(compute='_compute_company_fiscal_country_code')` |
| `code_store` | `` | `Char(company_dependent=True)` |
| `placeholder_code` | `` | `Char(string='Display code', compute='_compute_placeholder_code', search='_search_placeholder_code')` |
| `company_ids` | `` | `Many2many('res.company', string='Companies', required=True, readonly=False, default=lambda self: self.env.company)` |
| `code_mapping_ids` | `` | `One2many(comodel_name='account.code.mapping', inverse_name='account_id')` |
| `display_mapping_tab` | `` | `Boolean(default=lambda self: len(self.env.user.company_ids) > 1, store=False)` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `company_id` | `Many2one('res.company', string='Company', required=True, readonly=False, default=lambda self: self.env.company)` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `company_currency_id` | `Many2one(related='company_id.currency_id')` | `Many2one('res.currency', compute='_compute_company_currency_id')` |
| `code` | `Char(size=64, required=True, tracking=True, index=True, unaccent=False)` | `Char(string='Code', size=64, tracking=True, compute='_compute_code', search='_search_code', inverse='_inverse_code')` |
| `include_initial_balance` | `Boolean(string='Bring Accounts Balance Forward', help='Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.', compute='_compute_include_initial_balance', store=True, precompute=True)` | `Boolean(string='Bring Accounts Balance Forward', help='Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.', compute='_compute_include_initial_balance', search='_search_include_initial_balance')` |
| `internal_group` | `Selection(selection=[('equity', 'Equity'), ('asset', 'Asset'), ('liability', 'Liability'), ('income', 'Income'), ('expense', 'Expense'), ('off_balance', 'Off Balance')], string='Internal Group', compute='_compute_internal_group', store=True, precompute=True)` | `Selection(selection=[('equity', 'Equity'), ('asset', 'Asset'), ('liability', 'Liability'), ('income', 'Income'), ('expense', 'Expense'), ('off', 'Off Balance')], string='Internal Group', compute='_compute_internal_group', search='_search_internal_group')` |
| `tag_ids` | `Many2many(comodel_name='account.account.tag', relation='account_account_account_tag', string='Tags', help='Optional tags you may want to assign for custom reporting', ondelete='restrict', tracking=True)` | `Many2many(comodel_name='account.account.tag', relation='account_account_account_tag', compute='_compute_account_tags', readonly=False, store=True, precompute=True, string='Tags', help='Optional tags you may want to assign for custom reporting', ondelete='restrict', tracking=True)` |
| `group_id` | `Many2one('account.group', compute='_compute_account_group', store=True, readonly=True, help='Account prefixes can determine account groups.')` | `Many2one('account.group', compute='_compute_account_group', help='Account prefixes can determine account groups.')` |
| `root_id` | `Many2one('account.root', compute='_compute_account_root', store=True, precompute=True)` | `Many2one('account.root', compute='_compute_account_root', search='_search_account_root')` |

## 🔍 Model: `AccountLockException`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `active` | `` | `Boolean(string='Active', default=True)` |
| `state` | `` | `Selection(selection=[('active', 'Active'), ('revoked', 'Revoked'), ('expired', 'Expired')], string='State', compute='_compute_state', search='_search_state')` |
| `company_id` | `` | `Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env.company)` |
| `user_id` | `` | `Many2one('res.users', string='User', default=lambda self: self.env.user)` |
| `reason` | `` | `Char(string='Reason')` |
| `end_datetime` | `` | `Datetime(string='End Date')` |
| `lock_date_field` | `` | `Selection(selection=[('fiscalyear_lock_date', 'Global Lock Date'), ('tax_lock_date', 'Tax Return Lock Date'), ('sale_lock_date', 'Sales Lock Date'), ('purchase_lock_date', 'Purchase Lock Date')], string='Lock Date Field', required=True, help='Technical field identifying the changed lock date')` |
| `lock_date` | `` | `Date(string='Changed Lock Date', help='Technical field giving the date the lock date was changed to.')` |
| `company_lock_date` | `` | `Date(string='Original Lock Date', copy=False, help='Technical field giving the date the company lock date at the time the exception was created.')` |
| `fiscalyear_lock_date` | `` | `Date(string='Global Lock Date', compute='_compute_lock_dates', search='_search_fiscalyear_lock_date', help='The date the Global Lock Date is set to by this exception. If the lock date is not changed it is set to the maximal date.')` |
| `tax_lock_date` | `` | `Date(string='Tax Return Lock Date', compute='_compute_lock_dates', search='_search_tax_lock_date', help='The date the Tax Lock Date is set to by this exception. If the lock date is not changed it is set to the maximal date.')` |
| `sale_lock_date` | `` | `Date(string='Sales Lock Date', compute='_compute_lock_dates', search='_search_sale_lock_date', help='The date the Sale Lock Date is set to by this exception. If the lock date is not changed it is set to the maximal date.')` |
| `purchase_lock_date` | `` | `Date(string='Purchase Lock Date', compute='_compute_lock_dates', search='_search_purchase_lock_date', help='The date the Purchase Lock Date is set to by this exception. If the lock date is not changed it is set to the maximal date.')` |

## 🔍 Model: `AccountPayment`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `name` | `` | `Char(string='Number', compute='_compute_name', store=True)` |
| `date` | `` | `Date(default=fields.Date.context_today, required=True, tracking=True)` |
| `journal_id` | `` | `Many2one(comodel_name='account.journal', compute='_compute_journal_id', store=True, readonly=False, precompute=True, check_company=True, index=False, required=True)` |
| `company_id` | `` | `Many2one(comodel_name='res.company', compute='_compute_company_id', store=True, readonly=False, precompute=True, index=False, required=True)` |
| `state` | `` | `Selection(selection=[('draft', 'Draft'), ('in_process', 'In Process'), ('paid', 'Paid'), ('canceled', 'Canceled'), ('rejected', 'Rejected')], required=True, default='draft', compute='_compute_state', store=True, readonly=False, tracking=True, copy=False)` |
| `is_sent` | `` | `Boolean(string='Is Sent', readonly=True, copy=False)` |
| `memo` | `` | `Char(string='Memo', tracking=True)` |
| `company_currency_id` | `` | `Many2one(string='Company Currency', related='company_id.currency_id')` |
| `invoice_ids` | `` | `Many2many(string='Invoices', comodel_name='account.move', relation='account_move__account_payment', column1='payment_id', column2='invoice_id', copy=False)` |
| `payment_receipt_title` | `` | `Char(compute='_compute_payment_receipt_title')` |
| `need_cancel_request` | `` | `Boolean(related='move_id.need_cancel_request')` |
| `duplicate_payment_ids` | `` | `Many2many(comodel_name='account.payment', compute='_compute_duplicate_payment_ids')` |
| `attachment_ids` | `` | `One2many('ir.attachment', 'res_id', string='Attachments')` |

### ➖ Removed Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `is_internal_transfer` | `Boolean(string='Internal Transfer', readonly=False, store=True, tracking=True, compute='_compute_is_internal_transfer')` | `` |
| `destination_journal_id` | `Many2one(comodel_name='account.journal', string='Destination Journal', domain="[('type', 'in', ('bank','cash')), ('id', '!=', journal_id)]", check_company=True)` | `` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `move_id` | `Many2one(comodel_name='account.move', string='Journal Entry', required=True, readonly=True, ondelete='cascade', index=True, check_company=True)` | `Many2one(comodel_name='account.move', string='Journal Entry', index=True, copy=False, check_company=True)` |
| `partner_id` | `Many2one(comodel_name='res.partner', string='Customer/Vendor', store=True, readonly=False, ondelete='restrict', compute='_compute_partner_id', domain="['|', ('parent_id','=', False), ('is_company','=', True)]", tracking=True, check_company=True)` | `Many2one(comodel_name='res.partner', string='Customer/Vendor', store=True, readonly=False, ondelete='restrict', compute='_compute_partner_id', precompute=True, domain="['|', ('parent_id','=', False), ('is_company','=', True)]", tracking=True, check_company=True)` |

## 🔍 Model: `AccountTaxGroup`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `pos_receipt_label` | `` | `Char(string='PoS receipt label')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `preceding_subtotal` | `Char(string='Preceding Subtotal', help="If set, this value will be used on documents as the label of a subtotal excluding this tax group before displaying it. If not set, the tax group will be displayed after the 'Untaxed amount' subtotal.")` | `Char(string='Preceding Subtotal', help="If set, this value will be used on documents as the label of a subtotal excluding this tax group before displaying it. If not set, the tax group will be displayed after the 'Untaxed amount' subtotal.", translate=True)` |

## 🔍 Model: `AccountTax`

### ➕ Added Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `company_price_include` | `` | `Selection(related='company_id.account_price_include')` |
| `price_include_override` | `` | `Selection(selection=[('tax_included', 'Tax Included'), ('tax_excluded', 'Tax Excluded')], string='Included in Price', tracking=True, help="Overrides the Company's default on whether the price you use on the product and invoices includes this tax.")` |
| `invoice_legal_notes` | `` | `Html(string='Legal Notes', help='Legal mentions that have to be printed on the invoices.')` |
| `has_negative_factor` | `` | `Boolean(compute='_compute_has_negative_factor')` |

### 🔄 Modified Fields:

| Field | Odoo 17 | Odoo 18 |
|-------|---------|---------|
| `amount_type` | `Selection(default='percent', string='Tax Computation', required=True, tracking=True, selection=[('group', 'Group of Taxes'), ('fixed', 'Fixed'), ('percent', 'Percentage of Price'), ('division', 'Percentage of Price Tax Included')], help='\n    - Group of Taxes: The tax is a set of sub taxes.\n    - Fixed: The tax amount stays the same whatever the price.\n    - Percentage of Price: The tax amount is a % of the price:\n        e.g 100 * (1 + 10%) = 110 (not price included)\n        e.g 110 / (1 + 10%) = 100 (price included)\n    - Percentage of Price Tax Included: The tax amount is a division of the price:\n        e.g 180 / (1 - 10%) = 200 (not price included)\n        e.g 200 * (1 - 10%) = 180 (price included)\n        ')` | `Selection(default='percent', string='Tax Computation', required=True, tracking=True, selection=[('group', 'Group of Taxes'), ('fixed', 'Fixed'), ('percent', 'Percentage'), ('division', 'Percentage Tax Included')], help='\n    - Group of Taxes: The tax is a set of sub taxes.\n    - Fixed: The tax amount stays the same whatever the price.\n    - Percentage: The tax amount is a % of the price:\n        e.g 100 * (1 + 10%) = 110 (not price included)\n        e.g 110 / (1 + 10%) = 100 (price included)\n    - Percentage Tax Included: The tax amount is a division of the price:\n        e.g 180 / (1 - 10%) = 200 (not price included)\n        e.g 200 * (1 - 10%) = 180 (price included)\n        ')` |
| `description` | `Char(string='Description', translate=True)` | `Html(string='Description', translate=html_translate)` |
| `price_include` | `Boolean(string='Included in Price', default=False, tracking=True, help='Check this if the price you use on the product and invoices includes this tax.')` | `Boolean(compute='_compute_price_include', search='_search_price_include', help='Determines whether the price you use on the product and invoices includes this tax.')` |

