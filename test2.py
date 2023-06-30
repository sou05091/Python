import requests
import csv
from bs4 import BeautifulSoup

job_list_num = [5343, 5339, 5341, 5558, 5995, 5342, 5340, 5344, 5434, 5709, 5345, 5349, 5347, 5631, 5708, 5350, 5348, 5346, 5770, 5497, 5498, 5647, 5996, 5861, 5862]
key_value_dict = {
    "디스트로이어": 5343,
    "워로드": 5339,
    "버서커": 5341,
    "홀리나이트": 5558,
    "슬레이어": 5995,
    "배틀마스터": 5342,
    "인파이터": 5340,
    "기공사": 5344,
    "창술사": 5434,
    "스트라이커": 5709,
    "데빌헌터": 5345,
    "블래스터": 5349,
    "호크아이": 5347,
    "스카우터": 5631,
    "건슬링어": 5708,
    "바드": 5350,
    "서머너": 5348,
    "아르카나": 5346,
    "소서리스": 5770,
    "블레이드": 5497,
    "데모닉": 5498,
    "리퍼": 5647,
    "소울이터": 5996,
    "도화가": 5861,
    "기상술사": 5862
}

for job, number in key_value_dict.items():
    data = []  # 각 작업마다 독립적인 데이터 리스트 생성

    for i in range(1):
        url = f"https://www.inven.co.kr/board/lostark/{number}?p={i}"
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        post_list = soup.find_all('td', class_='tit')
        content_list_num = soup.find_all('td', class_='num')

        for post, content_num in zip(post_list, content_list_num):
            title_element = post.find('a', class_='subject-link')
            title = title_element.get_text(strip=True)

            content_num_test = content_num.find('span')
            num = content_num_test.get_text(strip=True)
            content_url = f"https://www.inven.co.kr/board/lostark/{number}/{num}"
            print(num)
            content_response = requests.get(content_url)
            content_html = content_response.text
            content_soup = BeautifulSoup(content_html, 'html.parser')
            content_post = content_soup.find('div', id='powerbbsContent')

            if content_post:
                content = content_post.get_text(strip=True)
            else:
                content = '내용이 없습니다.'

            data.append({'제목': title, '게시판 내용': content})

    csv_file = f'test_{job}.csv'

    with open(csv_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['제목', '게시판 내용'])
        writer.writeheader()
        writer.writerows(data)

    print(f'데이터가 {csv_file}에 저장되었습니다.')
