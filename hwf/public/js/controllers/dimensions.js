frappe.ui.form.on(cur_frm.doctype, {
	onload(frm) {
        frm.set_query("project", "items", function() {
			return {
                filters: {
                    is_active: "Yes"
                }
			}
		});
        frm.set_query("task", "items", function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
                filters: {
                    project: row.project
                }
			}
		});
        frm.set_query("task_activity", "items", function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				query: "hwf.hwf.doctype.task_activities.task_activities.get_activities_by_task",
				filters: { "task": row.task }
			}
		});
	},
})


frappe.ui.form.on(cur_frm.doctype + ' Item', {
    project(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "task", "")
    },
    task(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "task_activity", "")
    }
});