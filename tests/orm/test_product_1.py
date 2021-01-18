
from lbmod.product_mgr import ProductMgr
from lbmod.lb_exceptions import SetProductQuantityError

def test_create_default_product(cursor):
    dict = {'sku' : 'sku1', 'upc' : 'upc1'}
    product_mgr = ProductMgr(cursor)
    product = product_mgr.create(**dict)
    assert product.product_id > 0
    assert product.sku == 'sku1'
    assert product.upc == 'upc1'
    assert product.price == 0
    assert product.quantity == 0

def test_create_name_product(cursor):
    dict = {'sku' : 'sku1', 'upc' : 'upc1', 'name': 'name1'}
    product_mgr = ProductMgr(cursor)
    product = product_mgr.create(**dict)
    assert product.product_id > 0
    assert product.sku == 'sku1'
    assert product.upc == 'upc1'
    assert product.price == 0
    assert product.quantity == 0
    assert product.name == 'name1'

def test_select_sku(cursor):
    dict = {'sku' : 'sku1', 'upc' : 'upc1'}
    product_mgr = ProductMgr(cursor)
    p1 = product_mgr.create(**dict)
    p2 = product_mgr.find_by_sku('sku1')
    assert p2.upc == 'upc1' 