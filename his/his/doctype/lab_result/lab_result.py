# Copyright (c) 2022, Anfac and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_link_to_form, getdate

class LabResult(Document):
	pass

	# def after_insert(self):
	# 	if self.prescription:
	# 		frappe.db.set_value("Lab Prescription", self.prescription, "lab_test_created", 1)
	# 		if frappe.db.get_value("Lab Prescription", self.prescription, "invoiced"):
	# 			self.invoiced = True
	# 	if self.template:
	# 		self.load_test_from_template()
	# 		self.reload()
	# def load_test_from_template(self):
	# 	lab_test = self
	# 	create_test_from_template(lab_test)
	# 	self.reload()




def create_test_from_template(lab_test):
	template = frappe.get_doc("Lab Test Template", lab_test.template)
	patient = frappe.get_doc("Patient", lab_test.patient)

	lab_test.lab_test_name = template.lab_test_name
	lab_test.result_date = getdate()
	lab_test.department = template.department
	lab_test.lab_test_group = template.lab_test_group
	lab_test.legend_print_position = template.legend_print_position
	lab_test.result_legend = template.result_legend
	lab_test.worksheet_instructions = template.worksheet_instructions

	# lab_test = create_sample_collection(lab_test, template, patient, None)
	lab_test = load_result_format(lab_test, template, None, None)



def load_result_format(lab_test, template, prescription, invoice):
	if template.lab_test_template_type == "Single":
		create_normals(template, lab_test)

	elif template.lab_test_template_type == "Compound":
		create_compounds(template, lab_test, False)

	elif template.lab_test_template_type == "Descriptive":
		create_descriptives(template, lab_test)

	elif template.lab_test_template_type == "Grouped":
		# Iterate for each template in the group and create one result for all.
		for lab_test_group in template.lab_test_groups:
			# Template_in_group = None
			if lab_test_group.lab_test_template:
				template_in_group = frappe.get_doc("Lab Test Template", lab_test_group.lab_test_template)
				if template_in_group:
					if template_in_group.lab_test_template_type == "Single":
						create_normals(template_in_group, lab_test)

					elif template_in_group.lab_test_template_type == "Compound":
						normal_heading = lab_test.append("normal_test_items")
						normal_heading.lab_test_name = template_in_group.lab_test_name
						normal_heading.require_result_value = 0
						normal_heading.allow_blank = 1
						normal_heading.template = template_in_group.name
						create_compounds(template_in_group, lab_test, True)

					elif template_in_group.lab_test_template_type == "Descriptive":
						descriptive_heading = lab_test.append("descriptive_test_items")
						descriptive_heading.lab_test_name = template_in_group.lab_test_name
						descriptive_heading.require_result_value = 0
						descriptive_heading.allow_blank = 1
						descriptive_heading.template = template_in_group.name
						create_descriptives(template_in_group, lab_test)

			else:  # Lab Test Group - Add New Line
				normal = lab_test.append("normal_test_items")
				normal.lab_test_name = lab_test_group.group_event
				normal.lab_test_uom = lab_test_group.group_test_uom
				normal.secondary_uom = lab_test_group.secondary_uom
				normal.conversion_factor = lab_test_group.conversion_factor
				normal.normal_range = lab_test_group.group_test_normal_range
				normal.allow_blank = lab_test_group.allow_blank
				normal.require_result_value = 1
				normal.template = template.name

	if template.lab_test_template_type != "No Result":
		if prescription:
			lab_test.prescription = prescription
			if invoice:
				frappe.db.set_value("Lab Prescription", prescription, "invoiced", True)
		lab_test.save(ignore_permissions=True)  # Insert the result
		return lab_test


def create_compounds(template, lab_test, is_group):
	lab_test.normal_toggle = 1
	for normal_test_template in template.normal_test_templates:
		normal = lab_test.append("normal_test_items")
		if is_group:
			normal.lab_test_event = normal_test_template.lab_test_event
		else:
			normal.lab_test_name = normal_test_template.lab_test_event

		normal.lab_test_uom = normal_test_template.lab_test_uom
		normal.secondary_uom = normal_test_template.secondary_uom
		normal.conversion_factor = normal_test_template.conversion_factor
		normal.normal_range = normal_test_template.normal_range
		normal.require_result_value = 1
		normal.allow_blank = normal_test_template.allow_blank
		normal.template = template.name




def create_normals(template, lab_test):
	lab_test.normal_toggle = 1
	normal = lab_test.append("normal_test_items")
	normal.lab_test_name = template.lab_test_name
	normal.lab_test_uom = template.lab_test_uom
	normal.secondary_uom = template.secondary_uom
	normal.conversion_factor = template.conversion_factor
	normal.normal_range = template.lab_test_normal_range
	normal.require_result_value = 1
	normal.allow_blank = 0
	normal.template = template.name

