from flask import *
from mongoengine import *
<<<<<<< HEAD
import mlab
import jinja2
from os import path
from models.customer import Customer
=======

>>>>>>> 2fcbc8147cf5c3fb81e4cfd026c0d7f1e837175b
app = Flask(__name__)

app.secret_key = "123456789"

<<<<<<< HEAD
# jinja_environment = jinja2.Environment(
#   loader=jinja2.FileSystemLoader(['templates', 'templates/homepage'])
# )

mlab.connect()

@app.route('/', methods = ['GET', 'POST'])
def index():
=======
@app.route('/', methods = ['GET', 'POST'])
def index():
    error = 0
>>>>>>> 2fcbc8147cf5c3fb81e4cfd026c0d7f1e837175b
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        goal = form['goal']
        month = form['month']
        max = form['max']
<<<<<<< HEAD

        saving = round(((int(goal)*0.005)/(pow(1.005,int(month))-1)),3)
        session['income']= income
        session['goal']=goal
        session['saving']=saving
        if max > income:
            return "Ngáo quá! Bạn tiết kiệm nhiều hơn cả thu nhập. Nhập lại thôi"
        if saving > float(max) :
            return "Ồ, bạn thật là tham vọng, để đạt được mục tiêu cần thêm thời gian hoặc tìm cách tăng thêm thu nhập."
        else:
            customer = Customer(income = income, goal = goal, month = month, saving = saving)
            customer.save()
            return redirect (url_for('saving'))

@app.route('/saving')
def saving():
    return render_template('saving.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)
=======
        bank = form['bank']
        if income == "" or goal == "" or month == "" or max == "" or bank == "" :
            error = 1
            return render_template('error.html',error=error)
        else:
            saving = round(((int(goal)*float(bank)/12)/(pow((1+float(bank)/12),int(month))-1)),3)
            session['income']= income
            session['goal']=goal
            session['saving']=saving
            if saving > float(max) :
                error = 2
                return render_template('error.html',error=error)
            else:
                return redirect (url_for('saving'))

@app.route('/saving')
def saving():
    colors = ["#f54844", "#dbdad3"]
    labels = ["Thu nhập","Tiết kiệm"]
    pie_labels = labels
    pie_values = [session['income'], session['saving']]
    bar_labels = labels
    bar_values=[session['income'], session['saving']]
    return render_template('saving.html', max=200, set=zip(pie_values, labels, colors), labels=bar_labels, values=bar_values)
>>>>>>> 2fcbc8147cf5c3fb81e4cfd026c0d7f1e837175b

if __name__ == '__main__':
  app.run(debug=True)
