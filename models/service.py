from mongoengine import *

import mlab

class Service(Document):
    name = StringField()
    type = StringField()
    price = IntField()
    link = StringField()
    picture = StringField()
