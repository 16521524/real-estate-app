

# import frappe
from frappe.model.document import Document


class MintSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		automatically_run_rules_on_unreconciled_transactions: DF.Check
		bank_statement_gdoc_processor: DF.Data | None
		google_processor_location: DF.Literal["us", "eu"]
		google_project_id: DF.Data | None
		google_service_account_json_key: DF.Password | None
	# end: auto-generated types
	pass
