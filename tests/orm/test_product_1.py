import lbmod
import os
import mysql.connector

con = None
cursor = None

def setup_module(module):
    global con, cursor
    if not os.environ.get("LB_HOST"):
        print("\n")
        print("OOPS Undefined LB_HOST env variable!!")
        print("Did you source the database_setup.sh inside tests dir")
        exit(-1)

    con = mysql.connector.connect(host=os.environ.get("LB_HOST"),
                        user=os.environ.get("LB_USER"),
                        password=os.environ.get("LB_PASSWORD"),
                        database=os.environ.get("LB_DATABASE"),
                        port=os.environ.get("LB_PORT"))

    print(">>Connected to database ", os.environ.get("LB_DATABASE"))
    cursor = con.cursor(dictionary=True)

def teardown_module(module):
    cursor.close()
    con.close()

class BaseTest:
    def setup_method(self, method):
        self.product_mgr = lbmod.product_mgr.ProductMgr(cursor)

    def teardown_method(self, method):
        con.rollback()

class TestInsert1(BaseTest):
    def test_create_default_product(self):
        dict = {'sku' : 'sku1', 'upc' : 'upc1'}
        product = self.product_mgr.create(**dict)
        assert product.product_id > 0
        assert product.sku == 'sku1'
        assert product.upc == 'upc1'
        assert product.price == 0
        assert product.quantity == 0

    def test_create_name_product(self):
        dict = {'sku' : 'sku1', 'upc' : 'upc1', 'name': 'name1'}
        product = self.product_mgr.create(**dict)
        assert product.product_id > 0
        assert product.sku == 'sku1'
        assert product.upc == 'upc1'
        assert product.price == 0
        assert product.quantity == 0
        assert product.name == 'name1'

    def test_select_sku(self):
        dict = {'sku' : 'sku1', 'upc' : 'upc1'}
        p1 = self.product_mgr.create(**dict)
        p2 = self.product_mgr.find_by_sku('sku1')
        assert p2.upc == 'upc1' 