// Copyright (c) 2025, Kitti U. and contributors
// For license information, please see license.txt

frappe.ui.form.on("HWF Activity Request", {
    refresh(frm) {
		// Purchase Invoices
        frm.set_query("project_line", "purchase_invoices", function(doc, cdt, cdn) {
            return {
                filters: {
                    project: doc.project ? doc.project : "False",
					disabled: 0
                }
            };
        });
        frm.set_query("task_activity", "purchase_invoices", function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				query: "hwf.hwf.doctype.task_activities.task_activities.get_activities_by_project_line",
				filters: { "project_line": row.project_line }
			}
		});

		// Employee Advances
        frm.set_query("project_line", "employee_advances", function(doc, cdt, cdn) {
            return {
                filters: {
                    project: doc.project ? doc.project : "False",
					disabled: 0
                }
            };
        });
        frm.set_query("task_activity", "employee_advances", function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				query: "hwf.hwf.doctype.task_activities.task_activities.get_activities_by_project_line",
				filters: { "project_line": row.project_line }
			}
		});
	},
    
    project_type(frm) {
        frm.set_value("project", "");
        if (frm.doc.project_type) {
            frm.set_query("project", function() {
                return {
                    filters: {
                        "project_type": frm.doc.project_type,
						"is_active": "Yes",
						"status": "Open",
                    }
                };
            });
        }
    },

    project: function(frm) {
        // Clear project_line in all child tables when project changes
        frm.doc.purchase_invoices.forEach(function(item) {
            frappe.model.set_value(item.doctype, item.name, 'project_line', '');
            frappe.model.set_value(item.doctype, item.name, 'task_activity', '');
        });
        frm.doc.employee_advances.forEach(function(item) {
            frappe.model.set_value(item.doctype, item.name, 'project_line', '');
            frappe.model.set_value(item.doctype, item.name, 'task_activity', '');
        });
        frm.refresh_field('purchase_invoices');
        frm.refresh_field('employee_advances');
    }

});


frappe.ui.form.on("HWF Activity Request To Supplier", {
    project_line: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'task_activity', '');
    }
});

frappe.ui.form.on("HWF Activity Request To Employee", {
    project_line: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'task_activity', '');
    }
});