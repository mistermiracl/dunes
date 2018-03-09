from ._customer_dao import CustomerDao as _CustomerDao
from ._order_dao import OrdersDao as _OrdersDao
from ._product_dao import ProductDao as _ProductDao
from ._order_detail_dao import OrderDetailsDao as _OrderDetailsDao

class DaoFactory:

    def __init__(self):
        raise Exception('Cannot instatiate factory class')

    @staticmethod
    def get_customer_dao():
        return _CustomerDao()

    @staticmethod
    def get_product_dao():
        return _ProductDao()

    @staticmethod
    def get_order_dao():
        return _OrdersDao()
    
    @staticmethod
    def get_order_details_dao():
        return _OrderDetailsDao()

