# Test the product
from lbmod.product import Product
from lbmod.lb_exceptions import *

import pytest

@pytest.fixture
def p():
    """Return a sample product."""
    args = {'product_id' : 1, 'sku': 'abc', 'upc': 'def',
        'name' : 'hello', 'description' : 'xfsef', 
        'category1' : 'sdfds', 'category2' : 'dsfssaa',
        'storage' : 'afas', 'keywords' : '32423ssdf', 
        'quantity' : 3240, 'price': 23234, 'item_weight' : 23423,
        'item_weight_unit' : 'aefewa', 'item_volume' : 12.3,
        'item_volume_unit' : 'sfds4', 'expiry_date': '02/02/20', 
        'items_per_case' : 2343, 
        'case_wt' : 324234, 'case_wt_unit' : 'safa', 'case_dim' : '3ags',
        'case_dim_unit' : 'sdfs', 'photo1' : 'sdfsf34', 'photo2' : 'sdfgs',
        'photo3' : 'sdgfsdrf', 'created' : '2020-01-02 34:23:34', 
        'last_updated' : '2024-34-34 34.12.34' }
    return Product(**args)

def test_product_default():
    args = {'product_id' : 1, 'sku': 'abc', 'upc': 'def',
        'name' : 'hello', 'description' : 'xfsef', 
        'category1' : 'sdfds', 'category2' : 'dsfssaa',
        'storage' : 'afas', 'keywords' : '32423ssdf', 
        'quantity' : 3240, 'price': 23234, 'item_weight' : 23423,
        'item_weight_unit' : 'aefewa', 'item_volume' : 12.3,
        'item_volume_unit' : 'sfds4', 'expiry_date': '02/02/20', 
        'items_per_case' : 2343, 
        'case_wt' : 324234, 'case_wt_unit' : 'safa', 'case_dim' : '3ags',
        'case_dim_unit' : 'sdfs', 'photo1' : 'sdfsf34', 'photo2' : 'sdfgs',
        'photo3' : 'sdgfsdrf', 'created' : '2020-01-02 34:23:34', 
        'last_updated' : '2024-34-34 34.12.34' }
    p = Product(**args)
    assert p.product_id == args['product_id']
    assert p.sku == args['sku']
    assert p.upc == args['upc']
    assert p.name == args['name']
    assert p.quantity == args['quantity']
    assert p.price == args['price']
    assert p.items_per_case == args['items_per_case']
    assert len(p.fields) == len(args)
    assert set(p.fields) == set(args.keys())

def test_set(p):
    p.price = 212
    assert p.price == 212
    p.sku = '1234'
    assert p.sku == '1234'

def test_set_quantity_raises_exception(p):
    assert p.quantity == 3240
    with pytest.raises(SetProductQuantityError):
        p.quantity = 1

def test_set_shadow_quantity(p):
    p._quantity = 12321
    assert p.quantity == 12321