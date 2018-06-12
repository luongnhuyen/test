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
            saving = round(((int(goal)*float(bank)/12)/(pow((1+float(bank)/12),int(month))-1)),3)
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
    labels = ["Thu nhập","Tiết kiệm"]
    pie_labels = labels
    pie_values = [session['income'], session['saving']]

    bar_values= []
    bar_labels = []

    month = int(session['month'])
    bank = float(session['bank'])
    saving = float(session['saving'])
    var = 0
    for i in range(int(month)):
        name = "Tháng thứ " + str(i + 1)
        var = round(var + saving*(pow((1+bank/12),i)),3)
        bar_labels.append(name)
        bar_values.append(var)
    print(bar_values)

    return render_template('saving.html', max=200, set=zip(pie_values, labels, colors),labels=bar_labels, values=bar_values)
>>>>>>> f95ca651f9bc22e8de25110d5f11dff4e0824067

if __name__ == '__main__':
  app.run(debug=True)
