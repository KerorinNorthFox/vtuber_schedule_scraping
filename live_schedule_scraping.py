from bs4 import BeautifulSoup
import requests, sys, random, time

URL = 'https://virtual-youtuber.userlocal.jp/schedules'

V_NAME = ['白百合リリィ', '勇凪エレナ', '泡沫メモリ', '猫芒ベル', 'クロノロク']

class Schedule_Scraping:
    def __init__(self):
        alz = self.parse(URL)
        v_Names_Text = self.analyzing(alz)
        hours_Text = self.hours(alz)
        print(type(v_Names_Text))
        print(v_Names_Text)
        print(hours_Text)
        v_Data = self.find_v(v_Names_Text)
        print(v_Data)
        time.sleep(3)
    
    def parse(self, url):
        response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36'})
        alz = BeautifulSoup(response.text, 'html.parser')
        return alz

    def hours(self, alz):
        counter = 0
        text = []
        try:
            while(True):
                text.append(alz.select('.hour')[counter].text)
                counter += 1
        except:
            print(">>finish analyzing hours")
        return text

    def analyzing(self, alz):
        counter = 0
        text = []
        try:
            while(True):
                text.append(alz.select('.no-propagation')[counter].text)
                counter += 1
        except:
            print(">>finish analyzing names")
        return text

    def find_v(self, text):
        counter = 0
        v_Data = []
        for v_Name in text:
            counter += 1
            for needed_V_Name in V_NAME:
                if needed_V_Name in v_Name:
                    v_Data.append([v_Name, counter])
                else:
                    pass
        return v_Data

###START#######################################
if __name__ == "__main__":
    Schedule_Scraping()
    time.sleep(3)
    sys.exit()
