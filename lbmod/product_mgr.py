"""
CRUD operation on the products table.
"""

from lbmod.product import Product
from lbmod.lb_exceptions import DuplicateRecordError
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

        stmt = ("""
            SELECT product_id from products where sku = %s
        """)

        self.cursor.execute(stmt, (sku,))
        rows = self.cursor.fetchall()
        
        if len(rows) > 1:
            raise DuplicateRecordError("Found multiple records with same sku")
        if len(rows) == 0:
            raise NoRecordFoundError("OOPS! inserted a record but no trace found")

        
        args['product_id'] = rows[0]['product_id']
        p = Product(**args)
        return p


    def find_by_sku(self, sku):
        row_headers = [d[0] for d in self.cursor.description]
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
        
        row_headers = [x[0] for x in self.cursor.products]
        dicts = []
        for row in records:
            dicts.append(dict(zip(row_headers, row)))

        products = []
        for d in dicts:
            products.append(Product(**d))

        return products
