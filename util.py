import requests
from config import SECRET_KEY
from pymongo import MongoClient
import json
from pysondb import db

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
    client = MongoClient('mongodb+srv://ravenvl:Q2w3e4r5t6@cluster0.5m8xq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client['test1']
    products = db['products']

    rez = products.find_one({"weight": "11.667"})
    # rez = products.find_one()
    print(rez)

def save_file_to_mongo():
    client = MongoClient(
        'mongodb+srv://ravenvl:Q2w3e4r5t6@cluster0.5m8xq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client['test1']
    products = db['products']
    new_data = read_data_from_file('test_file.json')
    for el in new_data:
        post_id = products.insert_one(el).inserted_id
        print(post_id)


def read_data_from_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

if __name__ == '__main__':
    # save_data_to_file('test_file.txt', data_from_remote())
    use_mongo()
