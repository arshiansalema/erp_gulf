# from frappe.model.document import Document
# import frappe

# class MyBank(Document):

#     def validate(self):
#         if len(self.swift_number) < 11:
#             frappe.msgprint("Swift number must be more than 11 digits")


# from frappe.model.document import Document
# import frappe
# from erpnext.accounts.doctype.bank.bank import Bank


# class MyBank(Bank):

#     def validate(self):

#         if self.swift_number and not self.swift_number[:3].isalpha():
#             frappe.throw("First three characters should be alphabets")

#         super(MyBank, self).validate()


from erpnext.accounts.doctype.bank.bank import Bank
import frappe


class MyBank(Bank):

    def validate(self):
        if self.swift_number and not self.swift_number[:3].isalpha():
            frappe.throw("First three characters should be alphabets")

        self.write_something()

    def write_something(self):
        frappe.msgprint("write something here")


@frappe.whitelist(allow_guest=True)
def get_user_info():
    return {
        "user": "I am dummy user",
        "user_type": "my user is dummy",
    }