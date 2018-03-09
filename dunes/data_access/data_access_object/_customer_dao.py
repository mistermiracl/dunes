from .. import connection as _connection
from ._base_dao import BaseDao as _BaseDao
from ..data_access_entity.entity import Customer as _Customer
from MySQLdb.cursors import Cursor as _Cursor
from _mysql_exceptions import Error as _Error, Warning as _Warning

class CustomerDao(_BaseDao):
    
    __USP_CUSTOMER_LOGIN = 'usp_Customer_Login'
    __USP_CUSTOMER_CREATE = 'usp_Customer_Create'

    def insert(self, obj):
        success = False
        try:
            conn = _connection.get_connection()
            cur: _Cursor = conn.cursor()

            cur.callproc(CustomerDao.__USP_CUSTOMER_CREATE, (obj.username, obj.password, obj.name, 
                obj.last_name, obj.birthday, obj.email, obj.profile_pic))
            
            conn.commit()
            
            success = cur.rowcount == 1

        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()
        return success

    def update(self, obj):
        raise NotImplementedError('Not implemented yet')
    
    def delete(self, identifier):
        raise NotImplementedError('Not implemented yet')

    def find(self, identifier):
        raise NotImplementedError('Not implemented yet')
    
    def find_all(self, identifier=None):
        raise NotImplementedError('Not implemented yet')

    def login(self, username, password):
        customer = None
        try:
            conn = _connection.get_connection()
            cur: _Cursor = conn.cursor()
            cur.callproc(CustomerDao.__USP_CUSTOMER_LOGIN, (username, password))

            result = cur.fetchone()

            #[print(obj) for obj in result]
            
            if result:
                customer = _Customer(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

        except Exception as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()
        return customer
        