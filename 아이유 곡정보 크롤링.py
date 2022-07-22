import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r'C:\\Users\\Hyeongkyu Park\\Desktop\\데이터분석\\아이유\\chromedriver.exe')

# 페이지 넘겨가며 크롤링
for page in range(1, 102, 50):
    driver.get("https://www.melon.com/search/song/index.htm?q=%EC%95%84%EC%9D%B4%EC%9C%A0&section=artist&searchGnbYn=Y&kkoSpl=Y&kkoDpType=#params%5Bq%5D=%25EC%2595%2584%25EC%259D%25B4%25EC%259C%25A0&params%5Bsort%5D=hit&params%5Bsection%5D=artist&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex="+str(page))
    time.sleep(3)
    dict = {}  
    num= 50
    
    for i in range(0, num):
        more_info_list = driver.find_elements_by_css_selector(".btn.btn_icon_detail")
        more_info_list[i].click()
        time.sleep(1)
        
        try :   
            music_info = {} 
            time.sleep(1)
            
            #제목
            overlays = ".song_name"
            tit = driver.find_element_by_css_selector(overlays)
            title = tit.text
            
            #가수
            overlays = ".artist"
            nick = driver.find_element_by_css_selector(overlays)
            artist_name = nick.text
            time.sleep(1)
            
            # #앨범명
            album_name = driver.find_element_by_xpath("//*[@id='downloadfrm']/div/div/div[2]/div[2]/dl/dd[1]/a")
            album_name = album_name.text

            # #발매날짜
            date = driver.find_element_by_xpath("//*[@id='downloadfrm']/div/div/div[2]/div[2]/dl/dd[2]")
            date = date.text

            #장르
            genre = driver.find_element_by_xpath("//*[@id='downloadfrm']/div/div/div[2]/div[2]/dl/dd[3]")
            genre = genre.text
            
            # 더보기 버튼 클릭
            driver.find_element_by_css_selector(".button_more.arrow_d").click()
            time.sleep(1)
            
            # 가사
            overlays = ".lyric.on"    
            contents = driver.find_elements_by_css_selector(overlays)
            
            content_list = []
            for content in contents:
                content_list.append(content.text)
            
            content_str = ' '.join(content_list)
            
            music_info['title'] = title
            music_info['artist'] = artist_name
            music_info['Lyric'] = content_str
            music_info['album_name'] = album_name
            music_info['ReleaseDate'] = date
            music_info['Genre'] = genre
            time.sleep(1)
            
            dict[i] = music_info
            print(i, title)
            driver.back()
              
        
        except:
            driver.back()
            time.sleep(1)
            continue 
    result_df = pd.DataFrame.from_dict(dict, 'index') 
    df_to_excel = result_df.to_csv("아이유전곡%d.csv"% page, encoding='cp949')



# # 엑셀파일 합치기

# df1 = pd.read_csv("C:\\Users\\Hyeongkyu Park\\Desktop\\데이터분석\\아이유\\아이유전곡1.csv", encoding='cp949')
# df1 = pd.DataFrame(df1)
# df2 = pd.read_csv("C:\\Users\\Hyeongkyu Park\\Desktop\\데이터분석\\아이유\\아이유전곡51.csv", encoding='cp949')
# df2 = pd.DataFrame(df2)
# df3 = pd.read_csv("C:\\Users\\Hyeongkyu Park\\Desktop\\데이터분석\\아이유\\아이유전곡101.csv", encoding='cp949')
# df3 = pd.DataFrame(df3)

# ndf = pd.concat([df1, df2])
# ndf = pd.concat([ndf, df3])
# ndf = ndf.drop(['Unnamed: 0'],axis=1)

# ndf = ndf.to_csv("아이유전곡최종.csv", encoding='cp949')

