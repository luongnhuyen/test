from flask import *
from mongoengine import *
import mlab
from models.customer import Customer
app = Flask(__name__)

app.secret_key = "123456789"

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

# @app.route('/login', methods=["GET","POST"])
# def login():
#     if ("loggedin-customer" in session):
#         return render_template("error.html")
#     else:
#         if request.method == "GET":
#             return render_template("login.html")
#         elif request.method == "POST":
#             form = request.form
#             username = form['username']
#             password = form['password']
#             if username=='' and password=='':
#                 return render_template("error.html")
#             customer = Customer.objects(username = username, password = password)
#             if customer:
#                 session['loggedin-customer'] = 'customer'
#                 session['username'] = 'username'
#                 session['password'] = 'password'
#                 return redirect(url_for('index'))
#             else:
#                 return render_template('error.html')
#
# @app.route('/signin', methods= ['GET', 'POST'])
# def signin():
#     if request.method == 'GET':
#         return render_template('signin.html')
#     if request.method == 'POST':
#         form = request.form
#         name = form['name']
#         email = form['email']
#         username = form['username']
#         password = form['password']
#         if name == '' or email=='' or username=='' or password=='':
#             return render_template('error.html')
#         customer = Customer.objects(username = username)
#         if customer:
#             return render_template('error.html')
#         else:
#             customer = Customer(name=name, email=email, username=username, password=password)
#             customer.save()
#             if customer:
#                 session['loggedin-customer'] = "customer"
#                 session['username']= username
#                 session['password']= password
#                 return redirect(url_for('index'))
#             else:
#                 return render_template('error.html')
#
# @app.route('/logout')
# def logout():
#     if 'loggedin-customer' in session:
#         del session['loggedin-customer']
#         del session['username']
#         del session['password']
#         return redirect(url_for('index'))
#     else:
#         return render_template('error.html')

@app.route('/question',methods = ['GET', 'POST'])
def input():
    if request.method == "GET":
        return render_template('input-page.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        saving = form['saving']
        month = form['month']
        new_customer = Customer(income = income, saving = saving, month = month)
        new_customer.save()
        return redirect (url_for('customer'))

if __name__ == '__main__':
  app.run(debug=True)
