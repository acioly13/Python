from zipfile import *

with ZipFile('test.zip', 'w') as myzip:
    myzip.write('test_zipfile.py')
