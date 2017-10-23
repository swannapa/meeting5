# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "meeting5"
app_title = "Meeting5"
app_publisher = "swannapa"
app_description = "test"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "swannapa@simpletech.co.th"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting5/css/meeting5.css"
# app_include_js = "/assets/meeting5/js/meeting5.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting5/css/meeting5.css"
# web_include_js = "/assets/meeting5/js/meeting5.js"

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

# Website user home page (by function)
# get_website_user_home_page = "meeting5.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "meeting5.install.before_install"
# after_install = "meeting5.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting5.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "User": {
        "on_update": "meeting5.api.make_orientation_meeting"
    }
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"meeting5.tasks.all"
# 	],
# 	"daily": [
# 		"meeting5.tasks.daily"
# 	],
# 	"hourly": [
# 		"meeting5.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meeting5.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meeting5.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meeting5.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meeting5.event.get_events"
# }
