import requests
import random
import csv
import dotenv
import os

# Environment variables
dotenv.load_dotenv()
APIKEY = os.getenv('APIKEY')

# Some useragents to randomize request
USER_AGENTS = [
    "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"]


def get_exchange_rate(input_curr='USD', output_curr='RON'):
    conversion = f'{input_curr}_{output_curr}'

    url = f'https://free.currconv.com/api/v7/convert?q={conversion}&compact=ultra&apiKey={APIKEY}'

    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }

    try:
        r = requests.get(url, headers=headers)
    except Exception as e:
        print(e)
        return ""
    finally:
        r.close()

    if r.status_code != 200:
        return ""

    return f'{float(r.json()[conversion]):,}'


def get_currencies():
    url = f'https://free.currconv.com/api/v7/currencies?apiKey={APIKEY}'

    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }

    try:
        r = requests.get(url, headers=headers)
    except Exception as e:
        print(e)
        return []
    finally:
        r.close()

    if r.status_code != 200:
        return []

    return r.json()['results'].keys(), r.json()['results']


def write_currencies(*args):
    if len(args) < 2:
        return None

    try:
        with open('./currencies.csv', 'a') as currencies_file:
            writer = csv.writer(currencies_file, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            print(*args)
            writer.writerow([*args])
    except Exception as e:
        print(e)
        return None
    else:
        return True


if __name__ == '__main__':
    print(get_exchange_rate())
