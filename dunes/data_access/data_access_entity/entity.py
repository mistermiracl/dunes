
class Customer:
    
    def __init__(self, identifier, username, password, name, last_name, birthday, email, profile_pic):
        self.identifier = identifier
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.profile_pic = profile_pic

    def as_dict(self):
        return {
            'identifier': self.identifier,
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'last_name': self.last_name,
            'birthday': str(self.birthday),
            'email': self.email,
            'profile_pic': self.profile_pic
        }

class Product:
    
    def __init__(self, identifier, name, description, price, stock, image_path):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.image_path = image_path

class Orders:
    
    def __init__(self, identifier, order_date, current_order, customer_id):
        self.identifier = identifier
        self.order_date = order_date
        self.current_order = current_order
        self.customer_id = customer_id

class OrderDetails:

    def __init__(self, identifier, order_id, product_id, quantity, unit_price):
        self.identifier = identifier
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price




