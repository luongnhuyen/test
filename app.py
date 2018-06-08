from flask import *
from mongoengine import *
import mlab
from models.customer import Customer
app = Flask(__name__)

app.secret_key = "123456789"

mlab.connect()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        goal = form['goal']
        month = form['month']
        saving = int(round(((int(goal)*0.05)/(pow(1.05,int(month))-1)),0))
        customer = Customer(income = income, goal = goal, month = month, saving = saving)
        customer.save()
        return redirect (url_for('customer'))

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
