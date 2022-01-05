from bs4 import BeautifulSoup
import requests, sys, time, csv

URL = 'https://schedule.hololive.tv/simple/hololive'
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
        v_Name_List = self.make_V_List()
        """htmlパース"""
        alz = self.parse(URL)
        """html解析"""
        result = self.analyzing(alz, 'a')
        time.sleep(1)
        """目的の名前検索"""
        v_Data = self.find_v(result, v_Name_List)
        """結果表示"""
        self.show(v_Data)
        time.sleep(1)
    
    @decorator_func("htmlパース")
    def parse(self, url):
        response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.114 Safari/537.36'})
        alz = BeautifulSoup(response.text, 'html.parser')
        return alz

    @decorator_func("html解析")
    def analyzing(self, alz, tag_Name):
        counter = 9
        text = []
        try:
            while(True):
                text.append(alz.find_all(tag_Name)[counter].contents[0].strip().replace(' ','').split())
                counter += 1
        except:
            pass
        text.remove(['通常版'])
        text.remove(['シンプル版'])
        return text
        
    @decorator_func("目的の名前検索")
    def find_v(self, text, V_NAME_LIST):
        v_Data = []
        for v_Name in text:
            for needed_V_Name in V_NAME_LIST:
                if needed_V_Name in v_Name[1]:
                    v_Data.append(v_Name)
        return v_Data

    def show(self, v_Data):
        print(f"\n{PARTITION}\n")
        for counter in range(len(v_Data)):
            print(f">>{v_Data[counter][0]}時: {v_Data[counter][1]}\n")
        print(PARTITION)

    @decorator_func("名前リスト作成")
    def make_V_List(self):
        with open('holov_name_list.csv', 'r', newline='', encoding='utf=8') as f:
            v_Name_List_Obj = csv.reader(f)
            for v_Name_List in v_Name_List_Obj:
                pass
            return v_Name_List

###START#######################################
if __name__ == "__main__":
    Schedule_Scraping()
    time.sleep(3)
    sys.exit()
