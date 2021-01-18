"""Adjust price and amount in product table."""
import mysql.connector
import pytest
from lbmod.product_mgr import ProductMgr
from lbmod.lb_exceptions import DuplicateRecordError, SetProductQuantityError


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


def test_quantity_update(cursor):
    product_mgr = ProductMgr(cursor)
    dict1 = {'sku' : 'sku1', 'upc' : 'upc1', 'price' : 100, 'quantity': 10}
    product_mgr = ProductMgr(cursor)
    product = product_mgr.create(**dict1) 
    delta = 5 
    product_mgr.decr_quantity(product, delta)
    assert product.quantity == 5

def test_quantity_to_0(cursor):
    product_mgr = ProductMgr(cursor)
    dict1 = {'sku' : 'sku1', 'upc' : 'upc1', 'price' : 100, 'quantity': 10}
    product_mgr = ProductMgr(cursor)
    product = product_mgr.create(**dict1) 
    delta = 10
    product_mgr.decr_quantity(product, delta)
    assert product.quantity == 0

def test_quantity_to_raise_exception(cursor):
    product_mgr = ProductMgr(cursor)
    dict1 = {'sku' : 'sku1', 'upc' : 'upc1', 'price' : 100, 'quantity': 10}
    product_mgr = ProductMgr(cursor)
    product = product_mgr.create(**dict1) 
    delta = 11
    with pytest.raises(SetProductQuantityError):
        product_mgr.decr_quantity(product, delta)
   
