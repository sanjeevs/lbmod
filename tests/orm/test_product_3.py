"""Adjust price and amount in product table."""
from lbmod.product_mgr import ProductMgr

def test_product_save(cursor):
    product_mgr = ProductMgr(cursor)
    dict1 = {'sku' : 'sku1', 'upc' : 'upc1', 'price' : 100}
    product_mgr = ProductMgr(cursor)
    product = product_mgr.create(**dict1)   
    product.price = 200
    product_mgr.save(product)
    p_1 = product_mgr.find(product.product_id)
    assert p_1.sku == 'sku1'
    assert p_1.price == 200


# def test_amount_update(cursor):
#     product_mgr = ProductMgr(cursor)
#     dict1 = {'sku' : 'sku1', 'upc' : 'upc1', 'price' : 100, 'amount': 10}
#     product_mgr = ProductMgr(cursor)
#     product = product_mgr.create(**dict1) 
#     delta = 5 
#     product_mgr.decr_amount(product, delta)