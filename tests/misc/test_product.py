# Test the product
from lbmod.product import Product

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
