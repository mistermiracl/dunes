from _mysql_exceptions import Error as _Error, Warning as _Warning
from ..connection import get_connection as _get_connection
from ._base_dao import BaseDao as _BaseDao
from ..data_access_entity.entity import OrderDetails as _OrderDetails

class OrderDetailsDao(_BaseDao):

    __USP_ORDER_DETAILS_CREATE = 'usp_OrderDetails_Create'
    __USP_ORDER_DETAILS_DELETE = 'usp_OrderDetails_Delete'
    __USP_ORDER_DETAILS_FIND_ALL = 'usp_OrderDetails_FindAll'
    __USP_ORDER_DETAILS_UPDATE = 'usp_OrderDetails_Update'

    def insert(self, obj: _OrderDetails):
        success = False
        try:
            conn = _get_connection()
            cur = conn.cursor()
            cur.callproc(OrderDetailsDao.__USP_ORDER_DETAILS_CREATE, 
                (obj.order_id, obj.product_id, obj.quantity, obj.unit_price))
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
        success = False
        try:
            conn = _get_connection()
            cur = conn.cursor()
            cur.callproc(OrderDetailsDao.__USP_ORDER_DETAILS_UPDATE, (obj.identifier, obj.quantity))
            conn.commit()
            success = cur.rowcount == 1
        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()
        return success

    def delete(self, identifier):
        success = False
        try:
            conn = _get_connection()
            cur = conn.cursor()
            cur.callproc(OrderDetailsDao.__USP_ORDER_DETAILS_DELETE, (identifier,))
            conn.commit() #ONLY SELECTS DO NOT NEED COMMIT
            success = cur.rowcount == 1
        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()
        return success

    def find(self, identifier):
        """Not implemented yet"""
        raise NotImplementedError('Not implemented yet')
    
    def find_all(self, identifier=None):
        details = []
        try:
            conn = _get_connection()
            cur = conn.cursor()
            if identifier:
                cur.callproc(OrderDetailsDao.__USP_ORDER_DETAILS_FIND_ALL, (identifier,)) #ALWAYS COMMA WHEN USING VARIABLE ON TUPLE
            else:
                raise _Error('ID is required')
            results = cur.fetchall()

            if results:
                [details.append(_OrderDetails(det[0], det[1], det[2], det[3], det[4])) for det in results]

        except (_Error, _Warning) as ex:
            print(ex)
        finally:
            if conn.open:
                cur.close()
                conn.close()
        return details
