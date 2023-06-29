import csv

# CSV 파일 경로
csv_file = 'test.csv'
score_file = 'score.csv'

# 수정된 데이터를 담을 리스트
filtered_data = []

# CSV 파일 열기
with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    # 각 행을 확인하며 '?'가 없는 행만 filtered_data에 추가합니다.
    for row in reader:
        if '?' not in row['제목'] and '?' not in row['게시판 내용']:
            filtered_data.append(row)

# 분석을 위해 수정된 데이터를 활용합니다.
with open(score_file, 'r', encoding='utf-8-sig') as csvfile:
    score_reader = csv.DictReader(csvfile)
    score_data = list(score_reader)  # score 데이터를 리스트로 변환합니다.

    for row in filtered_data:
        # 각 행의 데이터 분석 및 처리
        # 예시: 점수 계산, 키워드 추출 등
        # 점수 계산 예시
        for row_score in score_data:
            if row_score['단어'] in row['제목'] or row_score['단어'] in row['게시판 내용']:
                row['점수'] = int(row_score['점수'])  # 점수를 정수로 변환하여 할당합니다.
                break
        else:
            row['점수'] = 0

# 데이터 분석 결과 출력 예시
for row in filtered_data:
    if row['점수'] != 0:
        print(f"제목: {row['제목']}, 게시판 내용: {row['게시판 내용']}, 점수: {row['점수']}")

# 점수 합계 계산
total_score = sum(row['점수'] for row in filtered_data)
print(f"총 점수 합계: {total_score}")
