"""Mulitple entry product table."""
from lbmod.product_mgr import ProductMgr


def test_100_product(cursor):
    product_mgr = ProductMgr(cursor)
    dict1 = [{'sku': f"sku{i}", 'upc' : f"upc{i}"} for i in range(100)]
    for row in dict1:
        product_mgr.create(**row)

    for i in range(100):
        p_1 = product_mgr.find_by_sku(f"sku{i}")
        assert p_1.upc == f"upc{i}"

    products = product_mgr.find_all()
    assert len(products) == 100
    for i in range(100):
        assert products[i].sku == f"sku{i}"
        assert products[i].upc == f"upc{i}"

