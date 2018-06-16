from flask import *
from mongoengine import *
import mlab
from models.service import Service
mlab.connect()
app = Flask(__name__)

app.secret_key = "123456789"

@app.route('/', methods = ['GET', 'POST'])
def index():
    error = 0
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        form = request.form
        income = form['income']
        goal = form['goal']
        month = form['month']
        max = form['max']
        bank = form['bank']
        if income == "" or goal == "" or month == "" or max == "" or bank == "":
            error = 1
            return render_template('error.html',error=error)
        elif float(max)> float(income):
            error = 3
            return render_template('error.html', error = error)
        else:
            saving = (int(goal)*float(bank)/12)/(pow((1+float(bank)/12),int(month))-1)
            session['income']= income
            session['goal']=goal
            session['saving']=saving
            session['bank']=bank
            session['month']=month

            if saving > float(max) :
                error = 2
                return render_template('error.html',error=error)
            else:
                return redirect (url_for('saving'))

@app.route('/saving')
def saving():
    colors = ["#f54844", "#dbdad3"]
    labels = ["Tiết kiệm","Thu nhập"]

    goal = int(session['goal'])
    month = int(session['month'])
    bank = float(session['bank'])
    saving = float(session['saving'])
    income = float(session['income'])
    ratio_save_income = round(saving/income*100,2)

    pie_labels = labels
    pie_values = [round(saving,2), session['income']]

    bar_values= []
    bar_labels = []
    max = goal +50
    var = 0
    for i in range(int(month)):
        name = "Tháng thứ " + str(i + 1)
        var = var + saving*(pow((1+bank/12),i))
        bar_labels.append(name)
        bar_values.append(round(var,2))

    return render_template('saving.html',saving=round(saving,2), max=max, set=zip(pie_values, labels, colors),labels=bar_labels, values=bar_values, ratio_save_income = ratio_save_income)

@app.route('/analysis', methods = ['GET', 'POST'])
def analysis():
    error = 0
    income = float(session['income'])
    saving = float(session['saving'])
    money = round(income - saving,2)
    if request.method == "GET":
        return render_template('detail.html', money = money)
    elif request.method == "POST":
        form = request.form
        n1 = form['n1']
        n2 = form['n2']
        n3 = form['n3']
        n4 = form['n4']
        n5 = form['n5']
        if n1 == "" or n2 == "" or n3 == "" or n4 == "" or n5 == "":
            error = 1
            return render_template('detail.html', money = money,error=error)
        else:
            n1 = int(form['n1'])
            n2 = int(form['n2'])
            n3 = int(form['n3'])
            n4 = int(form['n4'])
            n5 = int(form['n5'])
            if (n1 + n2 + n3 + n4 + n5) != 100:
                error = 2
                return render_template('detail.html', money = money,error=error)
            else:
                n1=round(n1*money/100,2)
                n2=round(n2*money/100,2)
                n3=round(n3*money/100,2)
                n4=round(n4*money/100,2)
                n5=round(n5*money/100,2)
                food = round(n1*money*0.5/100,2)
                go = round(n1*money*0.2/100,2)
                life = round(n1*money*0.2/100,2)
                other = round(n1*money*0.1/100,2)
                book = round(n2*money*0.4/100,2)
                training = round(n2*money*0.6/100,2)
                all_food = Service.objects(type = "food")
                all_drink = Service.objects(type = "drink",price__lte = food)
                all_book = Service.objects(type = "book",price__lte = book)
                all_training = Service.objects(type = "training",price__lte = training)
                return render_template('spending.html',
                money = money,
                n1=n1,
                n2=n2,
                n3=n3,
                n4=n4,
                n5=n5,
                food = food,
                go = go,
                life =life,
                other =other,
                book = book,
                training = training,
                all_food = all_food,
                all_drink = all_drink,
                all_book = all_book,
                all_training = all_training
                )

@app.route('/service')
def service():
    all_service = Service.objects()
    return render_template('service.html',all_service=all_service)

if __name__ == '__main__':
  app.run(debug=True)
