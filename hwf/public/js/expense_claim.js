{% include "hwf/public/js/overrides/dimension_tree_filter.js" %}

frappe.ui.form.on('Expense Claim', {

    refresh: function(frm) {
        // For sactioned_amount = amount
        frm.doc.expenses.forEach(function(d) {
            d.sanctioned_amount = d.amount
		})
        frm.refresh_field("expenses")
    }

})