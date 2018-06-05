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

@app.route('/question',methods = ['GET', 'POST'])
def input():
    if request.method == "GET":
        return render_template('input-page.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        saving = form['saving']
        month = form['month']
        # save service vào database
        new_customer = Customer(income = income, saving = saving, month = month)
        new_customer.save()
        return redirect (url_for('customer'))

if __name__ == '__main__':
  app.run(debug=True)
