import concurrent.futures
import requests
import csv
from bs4 import BeautifulSoup

data = []  # 데이터를 담을 리스트

def content(url):
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
            
def title(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    post_list = soup.find_all('td', class_='tit')  # 게시판 글 목록을 감싸는 태그를 선택합니다.

    for post in post_list:
        title_element = post.find('a', class_='subject-link')  # 게시글 제목을 담고 있는 <a> 태그를 선택합니다.
        title = title_element.get_text(strip=True)  # 게시글 제목을 가져옵니다.
        #print(title)
        
        # 딕셔너리에 데이터 추가
        data.append({'제목': title})
    

# URL 리스트 생성
urls = ["https://www.inven.co.kr/board/lostark/5647/" + str(i) for i in range(93476, 95720)]
urlt = ["https://www.inven.co.kr/board/lostark/5770?p=" + str(i) for i in range(50)]
# ThreadPoolExecutor를 사용하여 병렬 처리
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(content, urls)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(title, urlt)

# CSV 파일 경로
csv_file = '리퍼(category_content).csv'

# 헤더 필드명
fieldnames = ['카테고리', '제목', '게시판 내용']

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
