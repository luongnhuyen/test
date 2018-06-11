from flask import *
from mongoengine import *

app = Flask(__name__)

app.secret_key = "123456789"

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
        bank = form['bank']
        if income == "" or goal == "" or month == "" or max == "" or bank == "" :
            return "Nhập lỗi"
        else:
            saving = round(((int(goal)*float(bank)/12)/(pow((1+float(bank)/12),int(month))-1)),3)
            session['income']= income
            session['goal']=goal
            session['saving']=saving
            if saving > float(max) :
                return "Ồ, bạn thật là tham vọng, để đạt được mục tiêu cần thêm thời gian hoặc tìm cách tăng thêm thu nhập."
            else:
                return redirect (url_for('saving'))

@app.route('/saving')
def saving():
    colors = ["#f54844", "#dbdad3"]
    labels = ["income","saving"]
    pie_labels = labels
    pie_values = [session['income'], session['saving']]
    bar_labels = labels
    bar_values=[session['income'], session['saving']]
    return render_template('saving.html', max=200, set=zip(pie_values, labels, colors), labels=bar_labels, values=bar_values)

if __name__ == '__main__':
  app.run(debug=True)
