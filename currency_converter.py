import requests
from currency_symbols import CurrencySymbols

def is_valid_amount(amount):
    if amount and amount.isdigit():
        return amount
        
def is_valid_currency_from(data):
    if data['success']:
        return True
    return False
    
    
def get_exchange_rate(convert_from, convert_to, access_key, amount):
    quote=convert_from+convert_to
    api_url=f'http://api.exchangerate.host/live?access_key={access_key}&format=1&source={convert_from}'
    response = requests.get(api_url)

    data = response.json()

    if is_valid_amount(amount) and is_valid_currency_from(data):
        if data['success'] and convert_from==convert_to:
            print(data['success'], convert_to, convert_from)
            return amount
        elif quote in data['quotes']:
            exchange_rate=data['quotes'][quote]
            result=round(float(exchange_rate)*float(amount), 2)
            return result
        return False
    return False
        


def get_currency_symbol(convert_to):
    currency_symbol=CurrencySymbols.get_symbol(convert_to)
    return currency_symbol





    
