import dearpygui.dearpygui as dpg
import hololive_schedule_scraping, time
from holov_name_list import v_Name_List
from holov_name_list import v_EN_List

# 初期化
dpg.create_context()

# ローマ字変換
def change_name(v_Data):
    for x in range(len(v_Data)):
        num = v_Name_List.index(v_Data[x][1])
        v_Data[x][1] = v_EN_List[num]
    return v_Data

# 出力テキスト生成
def make_result_text(v_Data):
    text_list = []
    for num in range(len(v_Data)):
        text_list.append(f"\n>>{v_Data[num][0]}: {v_Data[num][1]}\n")
    return ''.join(text_list)

# スクレイピング処理
def scraping(sender, app_data, user_data):
    Obj = hololive_schedule_scraping.Schedule_Scraping()
    alz = Obj.parse(hololive_schedule_scraping.URL)
    result = Obj.analyzing(alz, 'a')
    v_Data = Obj.find_v(result, v_Name_List)
    v_Data_editted = change_name(v_Data)
    finally_text = make_result_text(v_Data_editted)
    dpg.set_value(user_data, finally_text)
    time.sleep(2)
    
# フォント設定
with dpg.font_registry():
    with dpg.font(file="./fonts/NotoSansJP-Medium.otf", size=20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    dpg.bind_font(default_font)

# ウィンドウ設定
with dpg.window(label='main_window', tag='main_window'):
    dpg.add_button(label='Click to get schedule!', tag='button', callback=scraping, user_data='result_text')
    dpg.add_separator()
    dpg.add_text(tag='result_text')

# 後処理
dpg.create_viewport(title="dear_pygui", width=150, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('main_window', True)
dpg.start_dearpygui()
dpg.destroy_context()