from flask import *
from mongoengine import *
import mlab
from models.customer import Customer
app = Flask(__name__)

app.secret_key = "123456789"

mlab.connect()


#bảng biểu

# values.append(session[''])
# values.append(income)

colors = [
        "#F7464A", "#46BFBD"]

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = [session['income'], session['saving']]
    bar_labels=labels
    bar_values=[session['income'], session['saving']]
    return render_template('pie_chart.html', title='Kết quả ', max=200, set=zip(pie_values, labels, colors), labels=bar_labels, values=bar_values)

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=[session['goal'], session['saving']]
    return render_template('bar_chart.html', title='', max=20000, labels=bar_labels, values=bar_values)

#hết
labels = ["income","saving"]

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        goal = form['goal']
        month = form['month']
        saving = round(((int(goal)*0.005)/(pow(1.005,int(month))-1)),3)

        session['income']= income
        session['goal']=goal
        session['saving']=saving


        if saving > int(20*int(income)/100) :
            return "Ồ, bạn thật là tham vọng, để đạt được mục tiêu cần thêm thời gian hoặc tìm cách tăng thêm thu nhập."
        else:
            customer = Customer(income = income, goal = goal, month = month, saving = saving)
            customer.save()
            return redirect (url_for('pie'))



@app.route('/saving')
def saving():
    return render_template('saving.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
