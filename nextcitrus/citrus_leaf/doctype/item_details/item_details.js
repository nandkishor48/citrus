// Copyright (c) 2024, Nand and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Details', {
    refresh: function(frm) {
        frm.add_custom_button(__('Sent For Email'), function(){
        
            frm.call({
				doc:frm.doc,
				method:"get_sales_invoice",
			}).then(r =>{
				console.log(r)
			})
            
        },__('Action'));
    }
});

