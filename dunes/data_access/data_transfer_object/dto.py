#from ..data_access_entity.entity import Orders, OrderDetails

class OrdersDto:
    
    def __init__(self, order_details_dto, full_price, order=None, identifier=None, order_date=None, current_order=None, customer_id=None):
        if order:
            self.identifier = order.identifier
            self.order_date = order.order_date
            self.current_order = order.current_order
            self.customer_id = order.customer_id
            self.order_details_dto = order_details_dto
            self.full_price = full_price
        else:
            self.identifier = identifier
            self.order_date = order_date
            self.current_order = current_order
            self.customer_id = customer_id
            self.order_details_dto = order_details_dto
            self.full_price = full_price

class OrderDetailsDto:
    
    def __init__(self, product, total_price, order_detail=None, identifier=None, order_id=None, quantity=None, unit_price=None):
        if order_detail:
            self.identifier = order_detail.identifier
            self.order_id = order_detail.order_id
            self.product = product
            self.quantity = order_detail.quantity
            self.unit_price = order_detail.unit_price
            self.total_price = total_price
        else:
            self.identifier = identifier
            self.order_id = order_id
            self.product = product
            self.quantity = quantity
            self.unit_price = unit_price
            self.total_price = total_price
