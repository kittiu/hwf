import frappe
from frappe.utils import flt


@frappe.whitelist()
def get_expense_claim(
    employee_name, company, employee_advance_name, posting_date, paid_amount, claimed_amount
):
    default_payable_account = frappe.get_cached_value(
        "Company", company, "default_expense_claim_payable_account"
    )
    default_cost_center = frappe.get_cached_value("Company", company, "cost_center")

    expense_claim = frappe.new_doc("Expense Claim")
    expense_claim.company = company
    expense_claim.employee = employee_name
    expense_claim.payable_account = default_payable_account
    expense_claim.cost_center = default_cost_center
    expense_claim.is_paid = 1 if flt(paid_amount) else 0
    expense_claim.append(
        "advances",
        {
            "employee_advance": employee_advance_name,
            "posting_date": posting_date,
            "advance_paid": flt(paid_amount),
            "unclaimed_amount": flt(paid_amount) - flt(claimed_amount),
            "allocated_amount": flt(paid_amount) - flt(claimed_amount),
        },
    )
	# HWF, copy advance lines
    advance = frappe.get_doc("Employee Advance", employee_advance_name)
    for item in advance.items:
        expense_claim.append(
            "expenses",
            {
                "expense_type": item.expense_claim_type,
                "description": item.description,
                "amount": item.amount,
                "donor": item.donor,
                "project": item.project,
                "project_line": item.project_line,
                "task_activity": item.task_activity
            }
        )
    # --

    return expense_claim
