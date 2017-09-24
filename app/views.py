from flask import render_template, flash, redirect, jsonify, Flask, request
from app import app
from Calc import *
# from .forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        start = int(request.form['startingSR'])
        target = int(request.form['targetSR'])
        result = calcStandardPrice(start, target)
        return 'Standard price: %s' % result
           
           
						  

