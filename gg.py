from pytrends.request import TrendReq

pytrends = TrendReq()
suggestions = pytrends.suggestions(keyword='data science')

for s in suggestions:
    if s['type'] == 'Topic':
        print(s['mid'])