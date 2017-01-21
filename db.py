from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

admin = Admin()
db = SQLAlchemy()
migrate = Migrate()
N=50

class Review_URL(db.Model):
    __tablename__ = "Product"
    url = db.Column(db.String(N*4), primary_key=True)
    name = db.Column(db.String(N), nullable=False)

class Product(db.Model):
    name = db.Column(db.String(N), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)

admin.add_view(ModelView(Review_URL, db.session))
admin.add_view(ModelView(Product, db.session))
