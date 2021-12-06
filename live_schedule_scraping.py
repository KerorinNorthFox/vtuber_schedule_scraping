from bs4 import BeautifulSoup
import requests, sys, random, time

URL = 'https://virtual-youtuber.userlocal.jp/schedules'

V_NAME = ['博衣こより', '勇凪エレナ']

class Schedule_Scraping:
    def __init__(self):
        alz = self.parse(URL)
        text = self.analyzing(alz)
        print(type(text))
        print(text)
        v_data = self.find_v(text)
        print(v_data)
        time.sleep(3)
    
    def parse(self, url):
        response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36'})
        alz = BeautifulSoup(response.text, 'html.parser')
        return alz

    def nubmer_of_a_tags(self, ):
        pass

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
        v_data = []
        for v_name in text:
            counter_2 += 1
            for needed_v_name in V_NAME:
                if v_name == needed_v_name:
                    v_data.append([v_name, counter_2])
                else:
                    pass
        return v_data

###START#######################################
if __name__ == "__main__":
    Schedule_Scraping()
    time.sleep(3)
    sys.exit()
