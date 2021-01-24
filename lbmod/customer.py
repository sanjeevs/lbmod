""" A customer orders items. """

class Customer:
    def __init__(self, customer_id, company_name, full_name, phone_number,
                 created, last_updated):
        self.customer_id = customer_id
        self.company_name = company_name
        self.full_name = full_name
        self.phone_number = phone_number
        self.created = created
        self.last_updated = last_updated
        self.addresses = []

    def __eq__(self, other):
        """Override id compare."""
        if isinstance(other, Customer):
            return self.customer_id == other.customer_id
        return False

    def __repr__(self):
        return f'customer_id={self.customer_id},company_name={self.company_name},\
                full_name={self.full_name},phone_number={self.phone_number}'