from flask import *
from mongoengine import *
import mlab
from random import randint, choice
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
                food = round(n1*0.6,2)
                go = round(n1*0.1,2)
                life = round(n1*0.2,2)
                other = round(n1*0.1,2)
                book = round(n2*0.4,2)
                training = round(n2*0.6,2)


                all_food = Service.objects(type = "food",price__lte = food*1000000/90).limit(6)

                all_book = Service.objects(type = "book",price__lte = n2*1000000).limit(6)
                all_luxury = Service.objects(type = "luxury",price__lte = n3*1000000).limit(6)
                all_charity = Service.objects(type = "charity",price__lte = n4*1000000).limit(6)
                all_invest = Service.objects(type = "invest",price__lte = n5*1000000).limit(6)
                count_food = len(all_food)
                count_book = len(all_book)
                count_luxury = len(all_luxury)
                count_charity = len(all_charity)
                count_invest = len(all_invest)
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
                                        all_book = all_book,
                                        all_luxury = all_luxury,
                                        all_charity = all_charity,
                                        all_invest = all_invest,
                                        count_food = count_food,
                                        count_book = count_book,
                                        count_luxury = count_luxury,
                                        count_charity = count_charity,
                                        count_invest = count_invest
                                        )

@app.route('/service')
def service():
    all_service = Service.objects()
    return render_template('service.html',all_service=all_service)

@app.route('/new_service_input', methods= ["GET", "POST"])
def new_service_input():
    if request.method == "GET":
        return render_template('new_service_input.html')
    elif request.method == "POST":
        form = request.form
        name  = form ['name']
        type = form ['type']
        price = form ['price']
        link = form ['link']
        picture = form ['picture']
        service = Service(name=name, type=type, price=price, link=link, picture=picture)
        service.save()
        all_service = Service.objects()
        return render_template('service.html',all_service=all_service)

if __name__ == '__main__':
  app.run(debug=True)
