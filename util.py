import requests
from config import SECRET_KEY
from pymongo import MongoClient
import json

def data_from_remote():
    payload = {'access_token': SECRET_KEY}
    # headers = {'access_token': SECRET_KEY}
    # url = 'https://api-pyatigorsk.mkplitka.ru/api/brands'
    # url = 'https://api-pyatigorsk.mkplitka.ru/api/collections'
    url = 'https://api-pyatigorsk.mkplitka.ru/api/products'

    # r = requests.get(url, headers=headers)
    r = requests.get(url, params=payload)
    rez = r.json()
    return rez

def save_data_to_file(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def use_mongo():
    client = MongoClient('localhost', 27017)

def read_data_from_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

if __name__ == '__main__':
    # save_data_to_file('test_file.txt', data_from_remote())
    data = read_data_from_file('test_file.txt')
    print(data)