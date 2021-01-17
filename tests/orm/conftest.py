import pytest
import mysql.connector
import os

@pytest.fixture(scope='module')
def con():
    con = mysql.connector.connect(host=os.environ.get("LB_HOST"),
                        user=os.environ.get("LB_USER"),
                        password=os.environ.get("LB_PASSWORD"),
                        database=os.environ.get("LB_DATABASE"),
                        port=os.environ.get("LB_PORT"))

    print(">>Connected to database ", os.environ.get("LB_DATABASE"))
    yield con
    con.close()


@pytest.fixture
def cursor(con):
    cursor = con.cursor(dictionary=True)
    yield cursor
    con.rollback()
    cursor.close()
