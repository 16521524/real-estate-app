frappe.ui.form.on("Mint Bank Statement Import", {
  refresh(frm) {
    frm.add_custom_button("Process via Google AI", () => {
      frm.call("process_file");
    });
  },
});
