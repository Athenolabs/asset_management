from frappe import _
def get_data():
	return [{ 
			"label": _("Tree Views"),
			"icon": "icon-star",
			"items": [{
				"type": "page",
				"label": _("AM Locaton"),
				"name": "Sales Browser",
				"icon": "icon-sitemap",
				"link": "Sales Browser/AM Location",
				"description": _("Manage Location Tree."),
				"doctype": "AM Location",
				}]
	}]

