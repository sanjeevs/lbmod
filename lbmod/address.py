"""Address in US"""

class Address:
    def __init__(self, address_id, customer_id, contact_person, street_address, 
                city, state, zip_code, phone_number):
        self.fields = []
        for k, v in locals().items():
            if k != 'self':
                setattr(self, k, v)

    def __eq__(self, other):
        """Override the id compare."""
        if isinstance(other, Address):
            return self.address_id == other.address_id
        return False

    def __repr__(self):
        return f'address_id={self.address_id},customer_id={self.customer_id},\
                 contact_person={self.contact_person},\
                 street_address={self.street_address},city={self.city},\
                 state={self.state},zip_code={self.zip_code}\
                 phone_number={self.phone_number}'