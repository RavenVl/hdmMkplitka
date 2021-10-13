import requests
from config import SECRET_KEY


def data_from_remote():
    payload = {'access_token': SECRET_KEY}
    headers = {'access_token': SECRET_KEY}
    url = 'https://api-pyatigorsk.mkplitka.ru/api/users/hdm'
    # r = requests.get('https://api-pyatigorsk.mkplitka.ru/api', params=payload)

    # r = requests.get(url, headers=headers)
    r = requests.get(url, params=payload)
    print(r.text)

if __name__ == '__main__':
    data_from_remote()