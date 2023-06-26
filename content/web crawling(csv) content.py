import concurrent.futures
import requests
import csv
from bs4 import BeautifulSoup

data = []  # 데이터를 담을 리스트

def crawl(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    post_list = soup.find_all('div', id='tbArticle')

    for post in post_list:
        category_element = post.find('div', class_='articleCategory')
        content_element = post.find('div', id='powerbbsContent')

        if category_element and content_element:
            category = category_element.get_text(strip=True)
            content = content_element.get_text(strip=True)
            data.append({'카테고리': category, category: content})
        else:
            data.append({'카테고리': '게시글 정보를 찾을 수 없습니다.'})

# URL 리스트 생성
urls = ["https://www.inven.co.kr/board/lostark/5647/" + str(i) for i in range(93476, 95720)]

# ThreadPoolExecutor를 사용하여 병렬 처리
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(crawl, urls)

# CSV 파일 경로
csv_file = '리퍼(category_content).csv'

# 헤더 필드명
fieldnames = ['카테고리', '[잡담]', '[질문]', '[정보]','[기타]']

# CSV 파일 열기
with open(csv_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
    # CSV writer 생성
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 헤더 작성
    writer.writeheader()

    # 데이터 작성
    writer.writerows(data)

# 작업 완료
print(f'데이터가 {csv_file}에 저장되었습니다.')
