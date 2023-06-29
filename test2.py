import requests
import csv
from bs4 import BeautifulSoup

data = []  # 데이터를 담을 리스트

for i in range(2):
    url = "https://www.inven.co.kr/board/lostark/5647?p=" + str(i)  # 크롤링하려는 웹 페이지의 URL
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    post_list = soup.find_all('td', class_='tit')  # 게시판 글 목록을 감싸는 태그를 선택합니다.
    for post in post_list:
        title_element = post.find('a', class_='subject-link')  # 게시글 제목을 담고 있는 <a> 태그를 선택합니다.
        title = title_element.get_text(strip=True)  # 게시글 제목을 가져옵니다.
        
        # 딕셔너리에 데이터 추가
        data.append({'제목': title})

    content_list_num = soup.find_all('td', class_='num')
    for content_num in content_list_num:
        num_element = content_num.find('a')  # 각 게시물의 링크를 선택합니다.
        content_url = "https://www.inven.co.kr/board/lostark/5647/" + str(content_num)  # 게시물의 URL을 생성합니다.
        content_response = requests.get(content_url)
        content_html = content_response.text
        content_soup = BeautifulSoup(content_html, 'html.parser')
        content_post = content_soup.find('div', class_='articleContent')  # 게시물 내용을 선택합니다.
        
        if content_post:
            content = content_post.get_text(strip=True)  # 게시물 내용을 가져옵니다.
            # 딕셔너리에 데이터 추가
            data.append({'게시판 내용': content})
        else:
            # 해당 게시물의 내용이 없는 경우 데이터에 빈 문자열로 추가합니다.
            data.append({'게시판 내용': '내용이 없습니다.'})


# CSV 파일 경로
csv_file = 'test.csv'

# CSV 파일 열기
with open(csv_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
    # CSV writer 생성
    writer = csv.DictWriter(csvfile, fieldnames=['제목', '게시판 내용'])

    # 헤더 작성
    writer.writeheader()

    # 데이터 작성
    writer.writerows(data)

# 작업 완료
print(f'데이터가 {csv_file}에 저장되었습니다.')
