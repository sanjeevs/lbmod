#Timeline

## Requirement
Must install MySql version locally and update the configuration file below.
```
mysql -V
mysql  Ver 14.14 Distrib 5.7.32, for Linux (x86_64) using  EditLine wrapper
cat sql/database_setup.sh
```
## Jan16,2020: Added Products table
```
source sql/database_setup.csh
pytest
```

This should run the 4 tests and report.
```
======================================== test session starts =========================================
platform linux -- Python 3.6.10, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/sanjeev/lily_bridge/lbmod
plugins: pep8-1.0.6, concurrent-0.2.2
collected 4 items                                                                                     

tests/misc/test_product.py .                                                                    [ 25%]
tests/orm/test_product_1.py ...                                                                 [100%]


```

