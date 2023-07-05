// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Employee Leave View"] = {
	field_map: {
		"start": "from_date",
		"end": "to_date",
		"title": "subject",
	},
	options: {
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month'
		}
	},
	get_events_method: "hwf.hwf.doctype.employee_leave_view.employee_leave_view.get_events"
}
