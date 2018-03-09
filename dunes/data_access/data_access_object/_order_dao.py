from _mysql_exceptions import Error as _Error, Warning as _Warning
from ._base_dao import BaseDao as _BaseDao
from ..connection import get_connection as _get_connection
from ..data_access_entity.entity import Orders as _Orders

class OrdersDao(_BaseDao):

    __USP_ORDERS_CREATE = 'usp_Orders_Create'
    __USP_ORDERS_UPDATE = 'usp_Orders_Update'
    __USP_ORDERS_FIND_CURRENT = 'usp_Orders_Find_Current'

    def insert(self, obj):
        success = False
        try:
            conn = _get_connection()
            cur = conn.cursor()
            print(obj.order_date, obj.current_order, obj.customer_id)
            cur.callproc(OrdersDao.__USP_ORDERS_CREATE, (obj.order_date, obj.current_order, obj.customer_id))
            conn.commit()#FOR INSERT AND UPDATE I GUESS COMMIT IS NEEDED
            
            success = cur.rowcount == 1 #ROWCOUNT WORKS SOMEHOW EVENTHOU IT'S NOT IN THE MYSQLDB DOCS
            print('Rows' + str(cur.rowcount))
            print('Sucess' + str(success))
        except (_Error, _Warning) as ex:
            print('error')  
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()

        return success

    def update(self, obj):
        success = False
        try:
            conn = _get_connection()
            cur = conn.cursor()
            cur.callproc(OrdersDao.__USP_ORDERS_UPDATE, (obj.identifier, obj.current_order))#IF ID IS None NO EXCEPTION IS RAISED CUZ MYSQLEXECUTES IT ANYWAY
            conn.commit()#NEEDED REMEBER
            success = cur.rowcount == 1
        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()

        return success
    
    def delete(self, identifier):
        raise NotImplementedError('Not implemented yet')

    def find(self, identifier):
        raise NotImplementedError('Not implemented yet')
    
    def find_all(self, identifier=None):
        raise NotImplementedError('Not implemented yet')

    def find_current(self, identifier):
        order = None
        try:
            conn = _get_connection()
            cur = conn.cursor()
            cur.callproc(OrdersDao.__USP_ORDERS_FIND_CURRENT, (identifier,))#IF ARGS TUPLE IS DECLARED WITHOUT COMMA PYTHON EXPECTS AN ITERABLE

            result = cur.fetchone()

            if result:
                order = _Orders(result[0], result[1], result[2], result[3])
        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()
        return order