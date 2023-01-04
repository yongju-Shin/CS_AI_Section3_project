# 셀레니움 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

# 크롬 제어를 위한 드라이버 설정
# Chrome 을 대문자로 적지 않아서 TypeError: 'module' object is not callable 로 시간을 썼다. 
driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32 (1)/chrmedriver')

# 웹 로드를 위한 웨이트 3초 
driver.implicitly_wait(3)
#url 접근
# 커피 정보를 활용한 프로젝트를 위해 원두 사이트를 크롤링 
driver.get('https://www.koke.kr/coffee')

before_h= driver.execute_script('return window.scrollY')

while True:
    # 맨 아래로 스크롤 내림 (html의 body마다 멈춤) 
    # css 선택자로 body 선택하고 키보드의 end 키 클릭
    driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h

wait = WebDriverWait(driver, 10)

tastylist=[]
namelist=[]
pricelist=[]
targetlist=[]
categorylist=[]
coffeelist=[]



for i in range(1,300):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__next"]/div[1]/main/div/div/div/div[2]/div[2]/div[2]/div/ul/li[{i}]')))
    element.click()
    time.sleep(3)
    tasty = driver.find_elements(By.CLASS_NAME, "style_characters__ERH9Q")
    for t in tasty:
        if t.text.strip():
            tastylist.append(t.text.strip())
    name = driver.find_elements(By.CLASS_NAME, "style_name__TCWF_")
    for n in name:
        if n.text.strip():
            namelist.append(n.text.strip())
    price = driver.find_elements(By.CLASS_NAME, "style_offer__ZEhC8")
    for p in price:
        if p.text.strip():
            pricelist.append(p.text.strip())
    target= driver.find_elements(By.CLASS_NAME, "style_title__aYoBr")
    tarlist=[]
    for tar in target:
        if tar.text.strip():
            tarlist.append(tar.text.strip())
    targetlist.append(tarlist)
    category= driver.find_elements(By.CLASS_NAME, "style_wrapper__nxg2I")
    catelist=[]
    for c in category:
        if c.text.strip():
            catelist.append(c.text.strip())
    categorylist.append(catelist)
    coffee = driver.find_elements(By.CLASS_NAME, 'style_itemDesc__Z9aB3')
    colist=[]
    for cof in coffee:
        if cof.text.strip():
            colist.append(cof.text.strip())
    coffeelist.append(colist)
    driver.back()

data = {"tasty" : tastylist,"name":namelist, "price":pricelist, "target":targetlist, "category":categorylist, 'coffee':coffeelist}
df = pd.DataFrame(data)

print(df.head(5))
df.to_csv("coffee.csv", encoding = "utf-8-sig")