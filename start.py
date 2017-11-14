from flask import Flask,render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def show_tables():
    data = pd.read_excel('data123.xlsx')
    return render_template('hello.html',tables=[data.to_html()],titles = ['Year', 'Rape', 'Dowry Deaths','Importation of Girls'])  # males.to_html(classes='male')],

