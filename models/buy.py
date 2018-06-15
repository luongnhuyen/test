from mongoengine import *

import mlab

class Buy(Document):
    name = StringField()
    type = StringField()
    price = IntField()
    link = StringField()
    picture = StringField()
