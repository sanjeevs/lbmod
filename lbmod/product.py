""" A product is a case of identical units identified by a unique sku.
    Each item in the case is identical and has a unique UPC code.
"""
from lbmod.lb_exceptions import SetProductQuantityError

class Product:
    def __init__(self, product_id, sku, upc, name, description, category1,
        category2, storage, keywords, quantity, price, item_weight,
        item_weight_unit, item_volume, item_volume_unit, expiry_date,
        items_per_case, case_wt, case_wt_unit, case_dim, case_dim_unit, 
        photo1, photo2, photo3, created, last_updated):

        # Keep a list of column names for sql ease
        self.fields = []
        for k, v in locals().items():
            if k != 'self':
                self.fields.append(k)
                # Dont allow changes to quantity. All modifications must
                # be done through the shadow variable.
                if k == "quantity":
                    setattr(self, '_quantity', v)
                else:
                    setattr(self, k, v)
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        raise SetProductQuantityError("Cannot change the quantity in product object")
    

    def __eq__(self, other):
        """Override the id compare."""
        if isinstance(other, Product):
            return self.product_id == other.product_id
        return False

    def __repr__(self):
        return f"product_id={self.product_id},sku={self.sku},upc={self.upc}"