# Copyright (c) 2013, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AMAssetTransfer(Document):
	def on_submit(self):
		frappe.db.set_value("AM Asset", self.asset, "location", self.source_location)