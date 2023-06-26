import requests
import csv
from collections import Counter
from bs4 import BeautifulSoup

word_count = Counter()
data = []  # 데이터를 담을 리스트

for i in range(50):
    url = "https://www.inven.co.kr/board/lostark/5770?p=" + str(i)  # 크롤링하려는 웹 페이지의 URL
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

# CSV 파일 경로
csv_file = '소서(title).csv'

# CSV 파일 열기
with open(csv_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
    # CSV writer 생성
    writer = csv.DictWriter(csvfile, fieldnames=['제목'])

    # 헤더 작성
    writer.writeheader()

    # 데이터 작성
    writer.writerows(data)
    
# 작업 완료
print(f'데이터가 {csv_file}에 저장되었습니다.')
