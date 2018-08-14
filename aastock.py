import requests
import time
import datetime
from datetime import datetime
from bs4 import BeautifulSoup
from tabulate import tabulate
import re
import sys
from contextlib import closing
from tools import contentSave
reload(sys)
sys.setdefaultencoding('utf8')


class aaStock():
    def __init__(self):
        self.cookie = {'mLang': 'EN'}
        self.url = "http://www.aastocks.com/en/stocks/news/aafn/latest-news"

    def getContent(self):
        r = requests.get(self.url,cookies=self.cookie)
        print r.content
        saver = contentSave.contentSaver("www")
        saver.save("www","iiii kwjndkwndkwnd")
        #get news from api



a = aaStock()
a.getContent()
