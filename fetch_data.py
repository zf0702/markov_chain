#!/bin/python

<<<<<<< HEAD
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import unicodedata
import ast
import requests
import re

def test():
  html = requests.get("http://www.winespectator.com/dailypicks/category/catid/1/page/").content 
  wineReviews = BeautifulSoup(html)
  lines = []
  for page in xrange(1, 2):
      for headLine in wineReviews.find_all("div", { "class" : "paragraph" }):
              txt1 = headLine.get_text()
              txt1 = re.sub('[ \t]+', ' ', txt1).strip()
              lines.append(txt1)
  with open("/home/zf/data/winereviews.txt", "w") as f:
      f.write(u'\n\n'.join(lines).encode('utf-8'))

=======
import urllib2
import requests
import scrapy
from markov_python.cc_markov import MarkovChain
>>>>>>> cca82f63da4849c6ea6619ee775c9665f542b029
