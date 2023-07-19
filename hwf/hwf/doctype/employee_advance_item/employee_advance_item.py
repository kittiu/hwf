# Copyright (c) 2023, Kitti U. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class EmployeeAdvanceItem(Document):
	pass

def sum_total(doc, method=None):
	# sum lines
	doc.advance_amount = sum(list(map(lambda x: x.amount, doc.items)))
