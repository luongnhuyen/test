from mongoengine import *
import mlab

class Customer(Document):
    name = StringField()
    username = StringField()
    email = StringField()
    password = StringField()
    income = IntField()
    goal = IntField()
    month = IntField()
    saving = FloatField()
