import csv
import nytimesarticle
from nytimesarticle import articleAPI

api = articleAPI('943d65691e814b8b96e1193dcab0036e')


def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    if 'response' in articles:
        for i in articles["response"]["docs"]:
            dic = {}
            dic['id'] = i['_id']

            dic['headline'] = i['headline']['main'].encode("utf8")

            dic['date'] = i['pub_date'][0:10]  # cutting time of day.

            dic['source'] = i['source']
            dic['type'] = i['type_of_material']
            dic['url'] = i['web_url']
            dic['word_count'] = i['word_count']
            news.append(dic)
    return (news)


all_articles = []
for i in range(0,
               100):  # NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
    articles = api.search(q="Facebook",
                          begin_date=20180101,
                          end_date=20180331,
                          page=i)
    articles = parse_articles(articles)
    all_articles = all_articles + articles

import csv

keys = all_articles[0].keys()
outputfile = open('NewsData.csv', 'w', newline='')
dict_writer = csv.DictWriter(outputfile, keys)
dict_writer.writerows(all_articles)
outputfile.close()