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
        print(v_Data)from bs4 import BeautifulSoup
import requests, sys, time, csv

URL = 'https://virtual-youtuber.userlocal.jp/schedules'
PARTITION = '-----------------------------------------'

def decorator_func(x):
    def decorator_func(f):
        def wrapper(*args):
            print(f">>{x}開始")
            value = f(*args)
            print(f">>{x}終了")
            return value
        return wrapper
    return decorator_func

@decorator_func("プログラム")
class Schedule_Scraping(object):
    def __init__(self):
        """名前リスト作成"""
        v_Name = self.make_V_List()
        """htmlパース"""
        alz = self.parse(URL)
        """名前解析"""
        v_Names_Text = self.analyzing(alz, '.no-propagation')
        """時間解析"""
        hours_Text = self.analyzing(alz, '.hour')
        time.sleep(1)
        """目的の名前検索"""
        v_Data = self.find_v(v_Names_Text, v_Name)
        """結果表示"""
        self.show(v_Data, hours_Text)
        time.sleep(1)
    
    @decorator_func("htmlパース")
    def parse(self, url):
        response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36'})
        alz = BeautifulSoup(response.text, 'html.parser')
        return alz

    @decorator_func("html解析")
    def analyzing(self, alz, tag_Name):
        counter = 0
        text = []
        try:
            while(True):
                text.append(alz.select(tag_Name)[counter].text)
                counter += 1
        except:
            pass
        return text
        
    @decorator_func("目的の名前検索")
    def find_v(self, text, V_NAME):
        counter = 0
        v_Data = []
        for v_Name in text:
            counter += 1
            for needed_V_Name in V_NAME:
                if needed_V_Name in v_Name:
                    v_Data.append([v_Name, counter])
        return v_Data

    def show(self, v_Data, hours_Text):
        counter = 0
        print(f"\n{PARTITION}")
        print(f'>>{hours_Text[0]}から\n')
        for x in range(len(v_Data)):
            print(f">>{v_Data[counter][0]}、{v_Data[counter][1]}番目\n")
            counter += 1
        print(PARTITION)

    @decorator_func("名前リスト作成")
    def make_V_List(self):
        with open('v_name_list.csv', 'r', newline='', encoding='utf=8') as f:
            v_Name_List_Obj = csv.reader(f)
            for v_Name_List in v_Name_List_Obj:
                pass
            return v_Name_List

###START#######################################
if __name__ == "__main__":
    Schedule_Scraping()
    time.sleep(3)
    sys.exit()

        time.sleep(1)
    
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
    print(">>開始")
    time.sleep(3)
    Schedule_Scraping()
    print("終了")
    time.sleep(3)
    sys.exit()
