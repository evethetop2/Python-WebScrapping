import os
import time #서버와 통신할 때 시간을 지연
from tqdm.notebook import tqdm
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\\Users\\Hyeongkyu Park\\Desktop\\python\\chromedriver.exe')

driver.get('http://www.melon.com')
time.sleep(2)  # 2초간 정지

# 멜론차트 클릭
driver.find_element_by_css_selector(".menu_bg.menu01").click()
time.sleep(2)

# 일간차트 클릭
driver.find_element_by_css_selector(".menu_chart.m2").click()

dict = {}    # 전체 크롤링 데이터를 담을 그릇

number = 2  # 수집할 글 갯수 정하기

for i in range(0,number):
    # 곡정보 더보기 버튼 클릭
    more_info_list = driver.find_elements_by_css_selector(".btn.button_icons.type03.song_info")
    more_info_list[i].click()
    time.sleep(1)
    # 크롤링
    try : 
        music_info = {}  # 개별 블로그 내용을 담을 딕셔너리 생성
        time.sleep(1)
        
        # 제목 크롤링
        overlays = ".song_name"                                 
        tit = driver.find_element_by_css_selector(overlays)          # title
        title = tit.text

        # 가수 크롤링
        overlays = ".artist"                              
        nick = driver.find_element_by_css_selector(overlays)         # nickname
        artist_name = nick.text
        time.sleep(1)

    
        # 더보기 버튼 클릭
        driver.find_element_by_css_selector(".button_more.arrow_d").click()
        time.sleep(3)
        
        # 가사 크롤링
        overlays = ".lyric.on"                                 
        contents = driver.find_elements_by_css_selector(overlays)    # contents
        
        content_list = []
        for content in contents:
            content_list.append(content.text)
 
        content_str = ' '.join(content_list)                         # content_str

        # 글 하나는 target_info라는 딕셔너리에 담기게 되고,
        music_info['title'] = title
        music_info['artist'] = artist_name
        music_info['Lyric'] = content_str
        time.sleep(1)
        # 각각의 글은 dict라는 딕셔너리에 담기게 됩니다.
        dict[i] = music_info
        
        # 크롤링이 성공하면 글 제목을 출력하게 되고,
        print(i, title)

        # 글 하나 크롤링 후 뒤로가기
        driver.back()  
    
    # 에러처리 : 에러나면 뒤로가기하고 다음 글(i+1)로 이동합니다.
    except:
        driver.back()
        time.sleep(1)
        continue
    
result_df = pd.DataFrame.from_dict(dict, 'index')

df_to_excel = result_df.to_csv("깃허브용.csv", encoding='cp949')

#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(4)

#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(6)
