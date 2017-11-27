from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from twython import TwythonStreamer
import pymongo
from pprint import pprint
import urllib.request
import pickle
import json
import time
analyzer = SentimentIntensityAnalyzer()

url = (r'https://www.reddit.com/r/london/.json')

with urllib.request.urlopen(url) as response:
    UberLondon = response.read()

LondonUberD = json.loads(UberLondon)

con = pymongo.MongoClient("mongodb://localhost")

db = con.uber.UberLondon

titles = {}
for article in LondonUberD['data']['children']:
    if 'London' in article['data']['title']:
        titles[article['data']['id']]=time.strftime("%a, %d %b %Y %H:%M:%S %Z",\n
        time.localtime(article['data']['created']))[0:25], article['data']['title'],\n
        analyzer.polarity_scores(article['data']['title'])['compound']

db.insert_one(titles)

