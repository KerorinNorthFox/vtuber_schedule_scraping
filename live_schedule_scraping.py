from _typeshed import _VT
from bs4 import BeautifulSoup
import requests, sys, random, time

URL = 'https://virtual-youtuber.userlocal.jp/schedules'

V_NAME = '博衣こより'

class Schedule_Scraping:
    def __init__(self):
        alz = self.parse(URL)
        text = self.analyzing(alz)
        print(type(text))
        print(text)
        self.find_v(text)
        time.sleep(3)
    
    def parse(self, url):
        response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36'})
        alz = BeautifulSoup(response.text, 'html.parser')
        return alz

    def analyzing(self, alz):
        counter_1 = 0
        text = []
        try:
            while(True):
                text.append(alz.select('.no-propagation')[counter_1].text)
                counter_1 += 1
        except:
            print(">>finish analyzing")
        return text

    def find_v(self, text):
        counter_2 = 0
        for v_name in text:
            counter_2 += 1
            if v_name == V_NAME:
                print(f">>{v_name}発見、{counter_2}番目")
                break
            else:
                pass

###START#######################################
if __name__ == "__main__":
    Schedule_Scraping()
    time.sleep(3)
    sys.exit()