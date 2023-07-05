# Copyright (c) 2023, Kitti U. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeeLeaveView(Document):
	pass

@frappe.whitelist()
def get_events(start, end, filters=None):
	data = frappe.db.sql("""
	SELECT from_date, to_date, CONCAT(employee_name, ' (', leave_type, ')') as subject
	FROM `tabLeave Application` WHERE status = 'Approved'
	""", as_dict=True)
	return data