# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _


def execute(filters=None):

	if not filters:
		filters = {}
	columns = get_columns()
	stock = get_total_stock(filters)

	return columns, stock


def get_columns():
	columns = [
		
		_("Item") + ":Link/Item:350",
		
		_("Current Qty") + ":Float:300",
	]

	return columns


def get_total_stock(filters):
	conditions = ""
	columns = ""

	if filters.get("group_by") == "Warehouse":
		if filters.get("company"):
			conditions += " AND warehouse.company = %s" % frappe.db.escape(
				filters.get("company"), percent=False
			)

		conditions += " GROUP BY ledger.warehouse, item.item_code"
		columns += "'' as company, ledger.warehouse"
	else:
		conditions += " GROUP BY warehouse.company, item.item_code"
		columns += " warehouse.company, '' as warehouse"

	return frappe.db.sql(
		"""
			SELECT
			
				item.item_code,
			
				sum(ledger.actual_qty) as actual_qty
			FROM
				`tabBin` AS ledger
			INNER JOIN `tabItem` AS item
				ON ledger.item_code = item.item_code
			INNER JOIN `tabWarehouse` warehouse
				ON warehouse.name = ledger.warehouse
			WHERE
				ledger.actual_qty != 0 %s"""
		% (conditions)
	)
