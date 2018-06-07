from models.customer import Customer
import mlab
mlab.connect()
customer = Customer(name="chung",
            username="chung",
            email="chung@gmail.com",
            password="chung",
            income=1000000,
            saving=500000)
customer.save()
