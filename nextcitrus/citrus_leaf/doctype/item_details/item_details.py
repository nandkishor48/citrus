# Copyright (c) 2024, Nand and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemDetails(Document):
	@frappe.whitelist()
	def get_sales_invoice(self):
		doc =frappe.db.sql("""SELECT s.name,s.creation,i.item_code FROM `tabSales Invoice` as s
		left outer join `tabSales Invoice Item` 
		as i on s.name = i.parent ORDER BY i.creation DESC LIMIT 5;""",as_dict=1)
        
		for i in doc:
			self.append("item_details_table",{
				'sales_invoice':i.get('name'),
				'item':i.get('item_code'),
				'date':i.get('date')
			})
		frappe.sendmail(
        recipients=[self.email],
		subject="Sales Invoices",
        template="custom_email_template",
        args={"invoices": doc},
    )
