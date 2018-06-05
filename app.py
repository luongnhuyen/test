from flask import *
from mongoengine import *
import mlab
from models.customer import Customer
app = Flask(__name__)

app.secret_key = "super secret"

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

@app.route('/login', methods=["GET","POST"])
def login():
    if ("loggedin" in session) and ("loggedin-customer" in session):
        return render_template("error.html")
    else:
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            form = request.form
            username = form['username']
            password = form['password']
            if username=='' and password=='':
                return render_template("error.html")
            if username=="admin" and password=="admin":
                session['loggedin'] == "admin"
                return redirect(url_for("admin.html"))
            else:
                customer = Customer.objects(username = username, password = password)
                if customer:
                    session['loggedin-customer'] = 'customer'
                    session['username'] = 'username'
                    session['password'] = 'password'
                    return redirect(url_for('index'))
                else:
                    return render_template('error.html')


@app.route('/signin', methods= ['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    if request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']
        if name == '' or email=='' or username=='' or password=='':
            return render_template('error.html')
        if username =='admin' and password == 'admin':
            return render_template('error.html')
        else:
            customer = Customer.objects(username = username)
            if customer:
                return render_template('error.html')
            else:
                customer = Customer(name=name, email=email, username=username, password=password)
                customer.save()
                if customer:
                    session['loggedin-customer'] = "customer"
                    session['username']= username
                    session['password']= password
                    return redirect(url_for('index'))
                else:
                    return render_template('error.html')
    # print(username)
if __name__ == '__main__':
  app.run(debug=True)
