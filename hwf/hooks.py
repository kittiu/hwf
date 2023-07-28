from . import __version__ as app_version

app_name = "hwf"
app_title = "HWF"
app_publisher = "Kitti U."
app_description = "HWF"
app_email = "kittiu@gmail.com"
app_license = "MIT"
required_apps = ["erpnext", "hrms"]

# monkey patch
import hrms.hr.doctype.expense_claim.expense_claim
import hwf.overrides.expense_claim

hrms.hr.doctype.expense_claim.expense_claim.get_expense_claim = (
	hwf.overrides.expense_claim.get_expense_claim
)

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": [
			[
				"name",
				"in",
				(
                    # Expense Claim Detail
                    "Expense Claim Detail-donor",
                    "Expense Claim Detail-column_break_bqsg1",
                    "Expense Claim Detail-project_line",
                    "Expense Claim Detail-task_activity",
                    # Material Request Item
                    "Material Request Item-donor",
                    "Material Request Item-project_line",
                    "Material Request Item-task_activity",
                    # Supplier Quotation Item
                    "Supplier Quotation Item-donor",
                    "Supplier Quotation Item-column_break_fo4xe",
                    "Supplier Quotation Item-project_line",
                    "Supplier Quotation Item-task_activity",
					# Purchase Order Item
                    "Purchase Order Item-donor",
                    "Purchase Order Item-project_line",
                    "Purchase Order Item-task_activity",
                    # Purchase Invoice Item
                    "Purchase Invoice Item-donor",
                    "Purchase Invoice Item-project_line",
                    "Purchase Invoice Item-task_activity",
					# Others
                    "Purchase Order-requester",
                    "Purchase Order-requester_name",
                    "Employee Advance-section_break_bigan",
                    "Employee Advance-items",
                    "Material Request-requester",
                    "Employee Advance-required_date",
                    "Payment Entry-party_bank_account_number",
                    "Expense Claim Detail-attachment",
                    "Material Request-total_amount",
				),
			]
		],
	},
	{
		"doctype": "Property Setter",
		"filters": [
			[
				"name",
				"in",
				(
					"Supplier Quotation Item-project-reqd",
                    "Material Request Item-project-reqd",
                    "Expense Claim-accounting_dimensions_section-hidden",
                    "Purchase Invoice-accounting_dimensions_section-hidden",
                    "Expense Claim Detail-project-reqd",
                    "Expense Claim Detail-cost_center-hidden",
                    "Purchase Invoice Item-project-reqd",
                    "Purchase Order Item-project-reqd",
                    "Purchase Order Item-cost_center-hidden",
                    "Expense Claim-project-hidden",
                    "Expense Claim-task-hidden",
                    "Purchase Invoice-project-hidden",
                    "Material Request Item-cost_center-hidden",
                    "Purchase Invoice Item-cost_center-hidden",
                    "Purchase Order-project-hidden",
                    "Purchase Order-accounting_dimensions_section-hidden",
                    "Employee Advance-advance_amount-read_only",
                    "Material Request Item-accounting_dimensions_section-collapsible",
                    "Supplier Quotation Item-ad_sec_break-collapsible",
                    "Purchase Order Item-accounting_dimensions_section-collapsible",
                    "Purchase Invoice Item-accounting_dimensions_section-collapsible",
                    "Payment Entry-cost_center-hidden",
                    # Payment entry, required cheque reference
                    "Payment Entry-reference_date-mandatory_depends_on",
                    "Payment Entry-reference_no-mandatory_depends_on",
                    # --
                    "Employee Advance-mode_of_payment-hidden",
				),
			]
		],
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hwf/css/hwf.css"
# app_include_js = "/assets/hwf/js/hwf.js"

# include js, css files in header of web template
# web_include_css = "/assets/hwf/css/hwf.css"
# web_include_js = "/assets/hwf/js/hwf.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hwf/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}

doctype_js = {
	"Material Request": "public/js/material_request.js",
	"Purchase Order": "public/js/purchase_order.js",
	"Supplier Quotation": "public/js/supplier_quotation.js",
	"Purchase Invoice": "public/js/purchase_invoice.js",
	"Expense Claim": "public/js/expense_claim.js",
    "Employee Advance": "public/js/employee_advance.js",
    "Timesheet": "public/js/timesheet.js",
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

calendars = ["Employee Leave View"]

# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hwf.utils.jinja_methods",
#	"filters": "hwf.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hwf.install.before_install"
# after_install = "hwf.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hwf.uninstall.before_uninstall"
# after_uninstall = "hwf.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hwf.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Employee Advance": {
		"validate": "hwf.hwf.doctype.employee_advance_item.employee_advance_item.sum_total",
    },
	"Material Request": {
		"validate": "hwf.overrides.material_request.sum_total",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"hwf.tasks.all"
#	],
#	"daily": [
#		"hwf.tasks.daily"
#	],
#	"hourly": [
#		"hwf.tasks.hourly"
#	],
#	"weekly": [
#		"hwf.tasks.weekly"
#	],
#	"monthly": [
#		"hwf.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "hwf.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "hwf.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hwf.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hwf.utils.before_request"]
# after_request = ["hwf.utils.after_request"]

# Job Events
# ----------
# before_job = ["hwf.utils.before_job"]
# after_job = ["hwf.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hwf.auth.validate"
# ]
