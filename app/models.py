from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True )
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String)
    allergens = db.Column(db.String)
    price = db.Column(db.Numeric)
    prod_image = db.Column(db.String)
    size = db.Column(db.String)
    

    def __init__(self, food_name, allergens, price, prod_image, size):
        self.food_name = food_name
        self.allergens = allergens
        self.price = price
        self.size = size
        self.prod_image = prod_image

    def save_food(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return{
            'id' : self.id,
            'food_name' : self.food_name,
            'allergens' : self.allergens,
            'price' : self.price,
            'size' : self.size,
            'prod_image' : self.prod_image
        }

# class CartItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)

#     def __init__(self, product_id, quantity):
#         self.product_id = product_id
#         self.quantity = quantity

#     def save_items(self):
#         db.session.add(self)
#         db.session.commit()


#     def to_dict(self):
#         product = Products.query.get(self.product_id)
#         return {
#             'id': self.id,
#             'product': product,
#             'quantity': self.quantity
#         }










