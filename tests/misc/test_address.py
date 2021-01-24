# Test the address
from lbmod.address import Address
import pytest

@pytest.fixture
def a():
    """Retun a customer."""
    args = {'address_id' : 1, 'customer_id' : 2, 'contact_person': 'contact1',
            'street_address' : 'street1', 'city' : 'city1', 'state': 'state1',
            'zip_code' : 'zip1', 'phone_number' : 'phone1'}

    return Address(**args)

def test_set(a):
    assert a.address_id == 1
    assert a.customer_id == 2
    assert a.contact_person == 'contact1'
    assert a.street_address == 'street1'
    assert a.city == 'city1'
    assert a.state == 'state1'
    assert a.zip_code == 'zip1'
    assert a.phone_number == 'phone1'