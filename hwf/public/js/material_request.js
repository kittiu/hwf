{% include "hwf/public/js/overrides/dimension_tree_filter.js" %}

// Disable existing
frappe.ui.form.off("Material Request Item", "qty") 
frappe.ui.form.off("Material Request Item", "rate")

frappe.ui.form.on("Material Request Item", {
	qty: function (frm, doctype, name) {
		const item = locals[doctype][name];
		if (flt(item.qty) < flt(item.min_order_qty)) {
			frappe.msgprint(__("Warning: Material Requested Qty is less than Minimum Order Qty"));
		}
	}
})