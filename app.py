import requests, json
from currency_symbols import CurrencySymbols
from flask import Flask, jsonify, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from unittest import TestCase
app=Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

access_key='fdf7087eb3fc3227ef65d44d43688757'

@app.route('/')
def home_page():

    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result_page():
    convert_from=request.form['convert_from']
    convert_to=request.form['convert_to']
    amount=request.form['amount']
    quote=convert_from+convert_to

    if isinstance(int(amount), str):
        flash(f"Not a valid amount: {amount}", 'error')
        return redirect('/')       


    api_url=f'http://api.exchangerate.host/live?access_key={access_key}&format=1'

    # Make the API request
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        data['source']=convert_from 
        currency_symbol=CurrencySymbols.get_symbol(convert_to)

        if not data['success']:
            flash(f"Not a valid code: {convert_from}", 'error')
        elif quote in data['quotes']:
            exchange_rate=data['quotes'][quote]
            result=round(float(exchange_rate)*float(amount), 2)
        else:
            flash(f"Not a valid code: {convert_to}, data['source']: {data['source']}, data: {data}", 'error')
            return redirect('/')

        return render_template('result.html', amount=amount, convert_from=convert_from, convert_to=convert_to, api_url=api_url, data=data, exchange_rate=exchange_rate, result=result, currency_symbol=currency_symbol)

    else:
        # Handle the error case (e.g., return an error message or raise an exception)
        return "Failed to retrieve exchange rate data."



