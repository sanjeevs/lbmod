"""
CRUD operation on the customers table.
"""

from lbmod.customer import Customer
import datetime

class CustomerMgr:

    def __init__(self, cursor):
        self.cursor = cursor

    def create(self, company_name, full_name="", phone_number=""):
        """Return a customer object backed by db."""
        args = locals()
        del args['self']

        args['created'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        args['last_updated'] = args['created']

        """Create a new customer."""
        columns = 'company_name, full_name, phone_number'
        values = f"'{company_name}', '{full_name}', '{phone_number}'"
        stmt = "INSERT INTO %s (%s) VALUES (%s)" % ('customers', columns, values)
        self.cursor.execute(stmt)

        args['customer_id'] = self.cursor.lastrowid
        return Customer(**args)