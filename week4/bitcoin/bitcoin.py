import sys
import requests
import json



link = "https://api.coindesk.com/v1/bpi/currentprice.json"


def get_data(link):
    while True:    
        try:
            json_data = requests.get(link).json()
            data = json.dumps(json_data, indent = 2)
            data = json.loads(data)
            return data
            break
        except requests.RequestException:
            continue


    
    

def get_price(data):    
    
    return float(data["bpi"]["USD"]["rate_float"])




def main():
    
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Missing command-line argument")
                break
            
            else:
                bitcoins = float(sys.argv[1])
                data = get_data(link)
                price = get_price(data)
                usd = price * bitcoins
                print(f"${usd:,.4f}")
                break

        except ValueError:
            sys.exit("Command-line argument is not a number")
            break
            


main()