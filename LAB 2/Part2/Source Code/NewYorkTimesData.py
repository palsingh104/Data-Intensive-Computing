from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import csv


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


i=1
with open ('NewsData.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        html = urllib.request.urlopen(row[5]).read()
        outputfile = open("fb%s.txt" %i,"w")
        i+=1
        outputfile.write(text_from_html(html))
        outputfile.close()