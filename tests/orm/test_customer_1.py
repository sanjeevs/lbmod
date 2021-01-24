from lbmod.customer_mgr import CustomerMgr

def test_create_default_customer(cursor):
    dict = {'company_name' : 'company1', 'full_name' : 'full1',
             'phone_number' : 'phone1'}
    customer_mgr = CustomerMgr(cursor)
    customer = customer_mgr.create(**dict)
    assert customer.customer_id > 0