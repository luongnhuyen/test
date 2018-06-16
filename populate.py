import mlab
from models.service import Service

mlab.connect()

service = Service(name="aaa",
             type="book",
             price=10000,
             link="tiki.com",
             picture="url")
service.save()
