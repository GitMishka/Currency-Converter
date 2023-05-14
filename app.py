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
def main():
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the base currency: ")
        to_currency = input("Enter the currency to convert to: ")

        result = convert_currency(amount, from_currency, to_currency)

        if result is not None:
            print(f"{amount} {from_currency} is equal to {result} {to_currency}")
        else:
            print("Conversion failed.")
    except ValueError:
        print("Invalid amount. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

