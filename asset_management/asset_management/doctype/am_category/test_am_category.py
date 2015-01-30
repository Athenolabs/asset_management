# Copyright (c) 2013, Frappe Technologies and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('AM Category')

class TestAMCategory(unittest.TestCase):
	pass
