from flask import Flask, Markup, render_template
from mongoengine import *
import mlab
from models.customer import Customer


app = Flask(__name__)

mlab.connect()

list_labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC','JAN',
    'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC','JAN'
]

labels = []

all_customer = Customer.objects(id='5b1a824b4219893708530a03')
for index, customer in enumerate(all_customer):
    a = customer['month']
labels=[]
i=0
for _ in range (a):
    b = list_labels[i]
    i+=1
    labels.append(b)

values = [
    967.67, 1190.89,
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=20000, labels=bar_labels, values=bar_values)


@app.route('/')
def index2():
    return render_template('index2.html')

@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))

if __name__ == '__main__':
    app.run(debug=True)
