// Copyright (c) 2017, swannapa and contributors
// For license information, please see license.txt
frappe.ui.form.on('Meeting Attendee', {
	attendee: function(frm, cdt, cdn) {
		var attendee = frappe.model.get_doc(cdt, cdn);
		if (attendee.attendee) {
			frappe.call({
				method: "meeting5.meeting5.doctype.meeting.meeting.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "full_name", r.message);
				}
			});
		} else {
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
	}
});

frappe.ui.form.on('Meeting', {
	send_emails: function(frm) {
		if (frm.doc.status==="Planned") {
			frappe.call({
				method: "meeting5.api.send_invitaltion_emails",
				args: {
					meeting: frm.doc.name
				},
				callback: function(r){

				}
			})
		}
	}
});
