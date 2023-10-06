import requests, json
from currency_symbols import CurrencySymbols
from flask import Flask, jsonify, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from unittest import TestCase
app=Flask(__name__, static_folder='static')

from currency_converter import get_exchange_rate, get_currency_symbol, is_valid_amount, is_valid_currency_from

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

access_key='fdf7087eb3fc3227ef65d44d43688757'



@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result_page():
    convert_from=request.form.get('convert_from')
    convert_to=request.form.get('convert_to')
    amount=request.form.get('amount')

    api_url=f'http://api.exchangerate.host/live?access_key={access_key}&format=1&source={convert_from}'
    response = requests.get(api_url)

    if not is_valid_amount(amount):
        flash(f"Not a valid amount: {amount}", 'error')
        return redirect('/')       


    data = response.json()
    currency_symbol=get_currency_symbol(convert_to)

    if not is_valid_currency_from(data):
        flash(f"Not a valid code: {convert_from}", 'error')
        return redirect('/')

    if get_exchange_rate(convert_from, convert_to, access_key, amount):
        result=get_exchange_rate(convert_from, convert_to, access_key, amount)
    else:
        flash(f"Not a valid code: {convert_to}", 'error')
        return redirect('/')

    
    return render_template('result.html', amount=amount, convert_from=convert_from, convert_to=convert_to, api_url=api_url, data=data, result=result, currency_symbol=currency_symbol)





