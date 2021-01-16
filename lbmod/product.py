""" A product is a case of identical units identified by a unique sku.
    Each item in the case is identical and has a unique UPC code.
"""
class Product:
    def __init__(self, product_id, sku, upc, name, description, category1,
        category2, storage, keywords, quantity, price, item_weight,
        item_weight_unit, item_volume, item_volume_unit, expiry_date,
        items_per_case, case_wt, case_wt_unit, case_dim, case_dim_unit, 
        photo1, photo2, photo3, created, last_updated):

        for k, v in locals().items():
            setattr(self, k, v)