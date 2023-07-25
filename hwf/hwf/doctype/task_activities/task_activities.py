# Copyright (c) 2023, Kitti U. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TaskActivities(Document):
	pass


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_activities_by_project_line(doctype, txt, searchfield, start, page_len, filters):
	if not filters:
		return []
	project_line = frappe.get_doc("Project Line", filters["project_line"])
	return [(x.task_activity, ) for x in project_line.activities]
