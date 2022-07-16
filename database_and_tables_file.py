from  peewee import *
from  os import path
# This is how to specify the path where the db is to be stored
db_connection_path = path.dirname(path.realpath(__file__))
# This is how to create our DB
db = SqliteDatabase(path.join(db_connection_path,"emobilis.db"))
# Start creating tables
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    # This is how to put our table into our database
    class Meta:
        database = db

class Product(Model):
    name = CharField()
    quantity = DoubleField()
    price = DoubleField()
    class Meta:
        database = db

# Finally create the two tables
User.create_table(fail_silently=True)
Product.create_table(fail_silently=True)










