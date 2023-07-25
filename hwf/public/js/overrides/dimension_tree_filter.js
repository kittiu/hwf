
frappe.provide('erpnext.accounts');

frappe.ui.form.on(cur_frm.doctype, {
	onload(frm) {
		let table_field = "items";
		if (cur_frm.doctype == "Expense Claim") {
			table_field = "expenses"
		}
		if (cur_frm.doctype == "Timesheet") {
			table_field = "time_logs"
		}
        frm.set_query("project", table_field, function() {
			return {
                filters: {
                    is_active: "Yes",
					status: "Open",
                }
			}
		});
        frm.set_query("project_line", table_field, function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
                filters: {
                    project: row.project ? row.project : "False",
					disabled: 0
                }
			}
		});
        frm.set_query("task_activity", table_field, function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				query: "hwf.hwf.doctype.task_activities.task_activities.get_activities_by_project_line",
				filters: { "project_line": row.project_line }
			}
		});
	},
});

frappe.ui.form.on(cur_frm.doctype + ' Item', {
    project(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "project_line", "")
    },
    task(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "task_activity", "")
    },
});

frappe.ui.form.on('Expense Claim Detail', {
    project(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "project_line", "")
    },
    task(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "task_activity", "")
    },
});

// ---- Override ----
// We no longer use Accounting Dimension Filters as it is

erpnext.accounts.dimensions = {
	// Function override
	setup_dimension_filters(frm, doctype) {
		this.accounting_dimensions = [];
		this.default_dimensions = {};
		this.fetch_custom_dimensions(frm, doctype);
	},

	fetch_custom_dimensions(frm, doctype) {
		let me = this;
		frappe.call({
			method: "erpnext.accounts.doctype.accounting_dimension.accounting_dimension.get_dimensions",
			args: {
				'with_cost_center_and_project': true
			},
			callback: function(r) {
				me.accounting_dimensions = r.message[0];
				me.default_dimensions = r.message[1];
			}
		});
	},

	// setup_filters(frm, doctype) {
	// 	if (this.accounting_dimensions) {
	// 		this.accounting_dimensions.forEach((dimension) => {
	// 			frappe.model.with_doctype(dimension['document_type'], () => {
	// 				let parent_fields = [];
	// 				frappe.meta.get_docfields(doctype).forEach((df) => {
	// 					if (df.fieldtype === 'Link' && df.options === 'Account') {
	// 						parent_fields.push(df.fieldname);
	// 					} else if (df.fieldtype === 'Table') {
	// 						this.setup_child_filters(frm, df.options, df.fieldname, dimension['fieldname']);
	// 					}

	// 					if (frappe.meta.has_field(doctype, dimension['fieldname'])) {
	// 						this.setup_account_filters(frm, dimension['fieldname'], parent_fields);
	// 					}
	// 				});
	// 			});
	// 		});
	// 	}
	// },

	// setup_child_filters(frm, doctype, parentfield, dimension) {
	// 	let fields = [];

	// 	if (frappe.meta.has_field(doctype, dimension)) {
	// 		frappe.model.with_doctype(doctype, () => {
	// 			frappe.meta.get_docfields(doctype).forEach((df) => {
	// 				if (df.fieldtype === 'Link' && df.options === 'Account') {
	// 					fields.push(df.fieldname);
	// 				}
	// 			});

	// 			frm.set_query(dimension, parentfield, function(doc, cdt, cdn) {
	// 				let row = locals[cdt][cdn];
	// 				return erpnext.queries.get_filtered_dimensions(row, fields, dimension, doc.company);
	// 			});
	// 		});
	// 	}
	// },

	// setup_account_filters(frm, dimension, fields) {
	// 	frm.set_query(dimension, function(doc) {
	// 		return erpnext.queries.get_filtered_dimensions(doc, fields, dimension, doc.company);
	// 	});
	// },

	update_dimension(frm, doctype) {
		if (this.accounting_dimensions) {
			this.accounting_dimensions.forEach((dimension) => {
				if (frm.is_new()) {
					if (frm.doc.company && Object.keys(this.default_dimensions || {}).length > 0
						&& this.default_dimensions[frm.doc.company]) {

						let default_dimension = this.default_dimensions[frm.doc.company][dimension['fieldname']];

						if (default_dimension) {
							if (frappe.meta.has_field(doctype, dimension['fieldname'])) {
								frm.set_value(dimension['fieldname'], default_dimension);
							}

							$.each(frm.doc.items || frm.doc.accounts || [], function(i, row) {
								frappe.model.set_value(row.doctype, row.name, dimension['fieldname'], default_dimension);
							});
						}
					}
				}
			});
		}
	},

	copy_dimension_from_first_row(frm, cdt, cdn, fieldname) {
		if (frappe.meta.has_field(frm.doctype, fieldname) && this.accounting_dimensions) {
			this.accounting_dimensions.forEach((dimension) => {
				let row = frappe.get_doc(cdt, cdn);
				frm.script_manager.copy_from_first_row(fieldname, row, [dimension['fieldname']]);
			});
		}
	}
};
// ---- End Override ----
