frappe.ui.form.on('Employee Advance',  {
    validate: function(frm) {
        var total = 0;
        $.each(frm.doc.items,  function(i,  d) {
            total += flt(d.amount);
        });
        frm.set_value("advance_amount", total);
    } 
});