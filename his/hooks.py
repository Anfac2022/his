from . import __version__ as app_version

app_name = "his"
app_title = "His"
app_publisher = "Anfac"
app_description = "Customization for healthcare module"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "his@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/his/css/his.css"
app_include_js = "public/js/hidden.js"

# include js, css files in header of web template
# web_include_css = "/assets/his/css/his.css"
# web_include_js = "/assets/his/js/his.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "his/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Custom Jinja Filters
# ----------
jenv = {
	"methods": [
		"format_value:his.api.api.frappe_format_value"
	]
}


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "his.install.before_install"
# after_install = "his.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "his.uninstall.before_uninstall"
# after_uninstall = "his.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "his.notifications.get_notification_config"

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
	"Sales Invoice": {
		"on_submit": "his.api.create_lab_test.create_lab_tests",
		
	},
	"Patient Encounter" :{
		# "after_insert":"his.api.create_order.create_order",
		"on_update":"his.api.create_order.update_order",
		

	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"his.tasks.all"
#	],
#	"daily": [
#		"his.tasks.daily"
#	],
#	"hourly": [
#		"his.tasks.hourly"
#	],
#	"weekly": [
#		"his.tasks.weekly"
#	]
#	"monthly": [
#		"his.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "his.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "his.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "his.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"his.auth.validate"
# ]



fixtures = [
    {"dt":"Custom Field", "filters": [["dt", "in", ("Customer", "Contact")], ["fieldname", "in", ("disable_customer_statements", "is_customer_statement_contact")]]}
]

