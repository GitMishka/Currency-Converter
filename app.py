import requests

def get_rates(base_currency):
    API_KEY = '0fbeecd24adf270c0218f472'  
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()

    if data['result'] == 'success':
        return data['conversion_rates']
    else:
        print(f"Error: {data['error-type']}")
        return None

#print(get_rates('USD'))
def convert_currency(amount, from_currency, to_currency):
    rates = get_rates(from_currency)
    if rates:
        if to_currency in rates:
            return amount * rates[to_currency]
        else:
            print(f"Error: Could not find the currency {to_currency}")
            return None
    else:
        return None

print(convert_currency(100, 'USD', 'EUR'))

