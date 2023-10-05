import requests
from currency_symbols import CurrencySymbols

def is_valid_amount(amount):
    if amount.isdigit():
        return True 
    
def get_exchange_rate(convert_from, convert_to, access_key, amount):
    quote=convert_from+convert_to
    api_url=f'http://api.exchangerate.host/live?access_key={access_key}&format=1'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        data['source']=convert_from 

        if is_valid_amount(amount):
            if quote in data['quotes']:
                exchange_rate=data['quotes'][quote]
                result=round(float(exchange_rate)*float(amount), 2)
                return result
            return False
        


def get_currency_symbol(convert_to):
    currency_symbol=CurrencySymbols.get_symbol(convert_to)
    return currency_symbol


    
def is_valid_currency_from(data):
    print(data)
    if not data['success']:
        return None

    
