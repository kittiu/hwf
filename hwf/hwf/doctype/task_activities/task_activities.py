# Copyright (c) 2023, Kitti U. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TaskActivities(Document):
	pass


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_activities_by_task(doctype, txt, searchfield, start, page_len, filters):
	if not filters:
		return []
	task = frappe.get_doc("Task", filters["task"])
	return [(x.task_activity, ) for x in task.activities]
