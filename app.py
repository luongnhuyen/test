from flask import *
from mongoengine import *
import mlab
from models.customer import Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
