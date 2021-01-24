"""
CRUD operation on the products table.
"""

from lbmod.product import Product
from lbmod.lb_exceptions import DuplicateRecordError, SetProductQuantityError
import datetime

class ProductMgr:

    def __init__(self, cursor):
        self.cursor = cursor

    
    def create(self, sku, upc, name="", description="", category1="",
        category2="", storage="", keywords="", quantity=0, price=0, item_weight=0,
        item_weight_unit="lbs", item_volume=0.0, item_volume_unit="floz", expiry_date="",
        items_per_case=0, case_wt=0, case_wt_unit='lbs', case_dim="", case_dim_unit="inches", 
        photo1="", photo2="", photo3="") : 
    
        args = locals()
        del args['self']

        if args['expiry_date'] == "":
            # All products expire after max of 5 years
            max_expiry = datetime.datetime.now() + datetime.timedelta(5*365)
            args['expiry_date'] = max_expiry.strftime('%Y-%m-%d')

        args['created'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        args['last_updated'] = args['created']

        """Create a new product."""
        columns = ', '.join(str(x) + " " for x in args.keys())
        values  = ', '.join("'" + str(x) + "'" for x in args.values())
        stmt = "INSERT INTO %s (%s) VALUES (%s)" % ('products', columns, values)
        self.cursor.execute(stmt)

        args['product_id'] = self.cursor.lastrowid
        p = Product(**args)
        return p

    def find(self, product_id):
        """Return the matching row using primary key."""
        stmt = "SELECT * from products where product_id=%s"
        self.cursor.execute(stmt, (product_id,))
        row = self.cursor.fetchall()
        assert(len(row) == 1)
        return Product(**row[0])

    def find_by_sku(self, sku):
        stmt = ("""
            SELECT * from products where sku = %s
        """)

        self.cursor.execute(stmt, (sku,))
        rows = self.cursor.fetchall()
        if len(rows) > 1:
            raise DuplicateRecordError("Found multiple records with same sku")
       
        if len(rows) == 0:
            return None 

        return Product(**rows[0])
           

    def find_all(self):
        """Return all products."""
        stmt = ("""
            SELECT * from products
            """)
        self.cursor.execute(stmt)
        records = self.cursor.fetchall()
        
        products = []
        for d in records:
            products.append(Product(**d))

        return products

    def save(self, product):
        """Save the contents of the product to database."""
        product.last_updated = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pairs = []
        for col in product.fields:
            value = getattr(product, col)
            pairs.append(f"{col} = '{value}'")

        if len(pairs) == 1:
            stmt = f"UPDATE products SET {pairs[0]};"
        else:
            stmt = "UPDATE products SET"
            for i in range(len(pairs) -1):
                stmt += f" {pairs[i]},"
            stmt += f" {pairs[-1]};"
       
        self.cursor.execute(stmt)


    def decr_quantity(self, product, delta):
        """Decrement the qty. If it becomes less than 0
           then throw exception.
        """
        stmt = ("""
            UPDATE products 
            SET quantity = quantity - %s
            WHERE product_id = %s
            and quantity >= %s
        """)
        self.cursor.execute(stmt, (delta, product.product_id, delta))
        if self.cursor.rowcount != 1:
            raise SetProductQuantityError("Unable to change the quantity field")

        stmt= ("SELECT quantity from products WHERE product_id=%s")
        self.cursor.execute(stmt, (product.product_id,))
        row = self.cursor.fetchone()
        product._quantity = row['quantity']