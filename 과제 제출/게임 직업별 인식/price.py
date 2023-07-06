import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def crw():
    # 크롬드라이버 실행
    driver = webdriver.Chrome('chromedriver.exe')
    # 크롬 드라이버에 url 주소 넣고 실행
    driver.get('https://loawa.com/shop/trade-shop')
    # 페이지가 완전히 로딩되도록 3초동안 기다림
    time.sleep(10)

    # 데이터 추출
    post_list = driver.find_elements_by_css_selector('td.item-name.text-left.text-grade4')
    job_name = [item.text for item in post_list]
    job_price = driver.find_elements_by_css_selector('td.item-transaction.text-right')
    prices = [item.text for item in job_price]

    # 추출한 데이터를 리스트 형태로 저장
    extracted_data = []
    for name, price in zip(job_name, prices):
        if '[' in name and ']' in name:
            extracted_data.append({'직업': name.split(']')[0][1:], '각인': name.split(']')[1][1:], '가격': price})

    # 웹드라이버 종료
    driver.quit()

    return extracted_data

def write_to_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['직업', '각인', '가격'])
        writer.writeheader()
        writer.writerows(data)

# 데이터 추출 및 CSV 파일로 저장
data = crw()
write_to_csv('test.csv', data)
