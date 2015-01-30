frappe.ui.form.on("AM Asset", "refresh", function(frm) {
	frm.set_df_property("location", "read_only", !frm.doc.__islocal);
	
	frm.set_query("asset_category", function() {
			return {
				"filters": {
					"is_group": "No"
				}
			};
		});
})