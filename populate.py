import mlab
from models.buy import Buy

mlab.connect()

buy = Buy(name="aaa",
             type="book",
             price=10000,
             link="tiki.com",
             picture="url")
buy.save()
