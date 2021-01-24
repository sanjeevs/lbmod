# Test the customer
from lbmod.customer import Customer
import pytest

@pytest.fixture
def c():
    """Retun a customer."""
    args = {'customer_id' : 1, 'company_name': 'company1', 'full_name': 'full1',
            'phone_number' : 'phone1', 'created' : '23', 'last_updated' : '34'}

    return Customer(**args)

def test_set(c):
    assert c.customer_id == 1
    assert c.company_name == 'company1'
    assert c.full_name == 'full1'
    assert c.phone_number == 'phone1'
    assert c.created == '23'
    assert c.last_updated == '34'