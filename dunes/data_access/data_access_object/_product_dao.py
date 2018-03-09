from MySQLdb.cursors import Cursor as _Cursor# TO DISCOVER METHODS AND ATTRIBUTES FOR CURSOR OBJECT
from _mysql_exceptions import Error as _Error, Warning as _Warning #FOR SOME REASON CANT IMPORT THESE FROM MySQLdb MODULE
from .. import connection as _connection
from ._base_dao import BaseDao as _BaseDao
from ..data_access_entity.entity import Product

class ProductDao(_BaseDao):

    __USP_PRODUCT_FIND = 'usp_Product_Find'
    __USP_PRODUCT_FINDALL = 'usp_Product_FindAll'

    def find(self, identifier):
        product = None
        try:
            conn = _connection.get_connection()
            cur: _Cursor = conn.cursor()
            cur.callproc(ProductDao.__USP_PRODUCT_FIND, (identifier, ))
            
            result = cur.fetchone()

            if result:
                product = Product(result[0], result[1], result[2], result[3], result[4], result[5])

        except (_Error, _Warning) as ex:
            print(ex)

        finally:
            if conn.open:
                conn.close()

        return product

    
    def find_all(self, identifier=None):
        products = []
        try:
            #with connection.get_connection() as conn CAN'T USE THIS OTHERWISE WEIRD EXCEPTION IS THROWN IDK WHY US FINALLY INSTEAD
            conn = _connection.get_connection()
            cur: _Cursor = conn.cursor()
            cur.callproc(ProductDao.__USP_PRODUCT_FINDALL)
            #c.nextset() NEXT SET NOT NEEDED AFTER ALL

            result = cur.fetchall()

            if result.__len__() > 0:
                [products.append(Product(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])) for obj in result]

        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()

        return products
