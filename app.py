from flask import *
from mongoengine import *
import jinja2
from os import path
app = Flask(__name__)

app.secret_key = "123456789"

# jinja_environment = jinja2.Environment(
#   loader=jinja2.FileSystemLoader(['templates', 'templates/homepage'])
# )

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        goal = form['goal']
        month = form['month']
        max = form['max']

        saving = round(((int(goal)*0.005)/(pow(1.005,int(month))-1)),3)
        session['income']= income
        session['goal']=goal
        session['saving']=saving
        # if max > income:
        #     return "Ngáo quá! Bạn tiết kiệm nhiều hơn cả thu nhập. Nhập lại thôi"
        if saving > float(max) :
            return "Ồ, bạn thật là tham vọng, để đạt được mục tiêu cần thêm thời gian hoặc tìm cách tăng thêm thu nhập."
        else:
            customer = Customer(income = income, goal = goal, month = month, saving = saving)
            # customer.save()
            return redirect (url_for('saving'))

@app.route('/saving')
def saving():
    return render_template('saving.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
