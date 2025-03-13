# Copyright (c) 2025, Kitti U. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class HWFActivityRequest(Document):
    
	def validate(self):
		self.compute_amount()

	def compute_amount(self):
		""" Validate the total amount of the activity request """
		# Calculate the total amount of the activity request
		pi_amount = 0
		adv_amount = 0
		for item in self.purchase_invoices:
			item.amount = item.quantity * item.rate
			pi_amount += item.amount
		for item in self.employee_advances:
			item.amount = item.quantity * item.rate
			adv_amount += item.amount
		self.pi_amount = pi_amount
		self.adv_amount = adv_amount
		self.total_amount = adv_amount + pi_amount

	def submit(self):
		# Check there are lines
		if not self.purchase_invoices and not self.employee_advances:
			frappe.throw(_("Please add at least one item to the activity request"))
		# Check valid approver
		if self.expense_approver != frappe.session.user:
			frappe.throw(_("Only Expense Approver can submit this document"))
		self.create_purchase_invoices()
		self.create_employee_advances()
		super().submit()

	def create_purchase_invoices(self):
		""" Create a purchase invoice for each item in activity request """
		if not self.purchase_invoices:
			return
		# Create a purchase invoice for each item in activity request
		for item in self.purchase_invoices:
			# Create a purchase invoice
			pi = frappe.new_doc("Purchase Invoice")
			pi.supplier = item.supplier
			pi.posting_date = item.date
			pi.due_date = item.date
			pi.company = self.company
			pi.remarks = self.purpose
			pi.custom_hwf_activity_request = self.name
			pi.append(
				"items",
    			{
					"item_code": item.item,
					"description": item.description,
					"qty": item.quantity,
					"uom": item.uom,
					"rate": item.rate,
					"amount": item.amount,
					"donor": item.donor,
					"project": self.project,
					"project_line": item.project_line,
					"task_activity": item.task_activity,
				}
			)
			pi.insert()
			# Update the item with the purchase invoice number
			item.purchase_invoice = pi.name

	def create_employee_advances(self):
		""" Create an employee advance for each item in activity request """
		if not self.employee_advances:
			return
		# Create an employee advance for each item in activity request
		adv = frappe.new_doc("Employee Advance")
		adv.employee = self.employee
		adv.posting_date = self.request_date
		adv.required_date = self.request_date
		adv.purpose = self.purpose
		adv.company = self.company
		adv.exchange_rate = 1
		adv.custom_hwf_activity_request = self.name
		adv.insert()
		for item in self.employee_advances:
			# Create an employee advance
			adv.append(
       			"items",
				{
					"expense_claim_type": item.expense_type,
					"description": item.description,
					"qty": item.quantity,
					"uom": item.uom,
					"amount": item.amount,
					"project": self.project,
					"project_line": item.project_line,
					"task_activity": item.task_activity,
					"donor": item.donor,
				}
			)
			# Update the item with the employee advance number
			item.employee_advance = adv.name
		adv.save()
  
  
  
  