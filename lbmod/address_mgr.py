"""
CRUD operations on the addresses table.
"""

from lbmod.address import Address
from lbmod.customer import Customer

class AddressMgr:

    def __init__(self, cursor):
        self.cursor = cursor

    def create(self, customer, contact_person, street_address, 
                city, state, zip_code, phone_number):
        """Return the address belonging to a customer."""
        columns = 'customer_id, contact_person, street_address, city,\
                   state, zip_code, phone_number'
        values = customer.customer_id + ', %s, %s, %s, %s, %s, %s'
        stmt = "INSERT INTO %s (%s) VALUES (%s)" % ('addresses', columns, values)
        self.cursor.execute(stmt)

        return Address(address_id=cursor.lastrowid, 
                      customer_id=customer.customer_id,
                      contact_person=contact_person,
                      street_address=street_address,
                      city=city,
                      state=state,
                      zip_code=zip_code,
                      phone_number=phone_number)

