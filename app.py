import requests
from flask import Flask, jsonify, request, render_template, redirect, flash, session
from random import choice
# from flask_debugtoolbar import DebugToolbarExtension
from unittest import TestCase
app=Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

access_key='fdf7087eb3fc3227ef65d44d43688757'

@app.route('/home')
def home_page():
    # sort=request.args.get('sort')
    # return f'<h1>Search results for {sort}</h1>'
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result_page():
    convert_from=request.form['convert_from']
    convert_to=request.form['convert_to']
    amount=request.form['amount']

    api_url = f"https://api.exchangerate.host/convert?access_key={access_key}&from={convert_from}&to={convert_to}&amount={amount}&format=1"

    # Make the API request
    response = requests.get(api_url)
    print (response)

    # Check if the request was successful
    if response.status_code == 200:
        # data = response.json()
        # result_amount = data['result']
        return render_template('result.html', amount=amount, convert_from=convert_from, convert_to=convert_to)

    else:
        # Handle the error case (e.g., return an error message or raise an exception)
        return "Failed to retrieve exchange rate data."



