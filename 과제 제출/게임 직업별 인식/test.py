# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
import csv


# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')
driver = webdriver.Chrome('chromedriver.exe') 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://loawa.com/shop/trade-shop')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(10)
def crw():
    # 데이터 추출
    post_list = driver.find_elements_by_css_selector('td.item-name.text-left.text-grade4')
    job_name = [item.text for item in post_list]
    job_price = driver.find_elements_by_css_selector('td.item-transaction.text-right')
    prices = [item.text for item in job_price]

    # 결과 출력
    for name, price in zip(job_name, prices):
        #print(name, price)
        if '[' in name and ']' in name:
            print(name,price)
    return name, price

def write_to_csv(file_path,crw):
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['직업','각인','가격'])
        writer.writeheader()
        writer.writerows(crw)

# 웹드라이버 종료
driver.quit()
