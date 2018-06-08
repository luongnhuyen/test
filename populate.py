from models.customer import Customer
import mlab
mlab.connect()
customer = Customer(name="chung",
            username="chung",
            email="chung@gmail.com",
            password="chung",
            income=10,
            goal = 100,
            month = 10,)
customer.save()
