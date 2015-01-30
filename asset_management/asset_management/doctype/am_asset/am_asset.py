# Copyright (c) 2013, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.nestedset import NestedSet

class AMAsset(NestedSet):
	nsm_parent_field = 'parent_am_asset'
	pass
