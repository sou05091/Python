import csv
import matplotlib.pyplot as plt
import pandas as pd

job = []
avg = []

def write_to_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['직업', '점수'])
        writer.writerows(data)
        
read_job = ["디스트로이어",
        "워로드",
        "버서커",
        "홀리나이트",
        "슬레이어",
        "배틀마스터",
        "인파이터",
        "기공사",
        "창술사",
        "스트라이커",
        "데빌헌터",
        "블래스터",
        "호크아이",
        "스카우터",
        "건슬링어",
        "바드",
        "서머너",
        "아르카나",
        "소서리스",
        "블레이드",
        "데모닉",
        "리퍼",
        "소울이터",
        "도화가",
        "기상술사"]
for read in read_job:
    csv_file = './csv/test_'+read+'.csv'
    score_file = './csv/score.csv'

    filtered_data = []
    total_scores = []
    negative_scores = []

    # CSV 파일 열기
    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        filtered_data = [row for row in reader if '?' not in row['제목'] and '?' not in row['게시판 내용']]

    # 점수 데이터 로딩 및 사전 형태로 변환
    with open(score_file, 'r', encoding='utf-8-sig') as csvfile:
        score_reader = csv.DictReader(csvfile)
        score_mapping = {row['단어']: int(row['점수']) for row in score_reader}

    # 데이터 분석 및 점수 계산
    for row in filtered_data:
        total_score = 0
        negative_score = 0
        count = 0

        for word, score in score_mapping.items():
            if word in row['제목'] or word in row['게시판 내용']:
                total_score += score
                count += 1
                if score < 0:
                    negative_score += score

        if count > 0:
            row['점수'] = total_score / count
            negative_scores.append(negative_score)
        else:
            row['점수'] = 0

        total_scores.append(total_score)

    # 수정된 데이터를 새로운 CSV 파일에 저장
    output_file = './csv/modified_data.csv'
    fieldnames = filtered_data[0].keys()

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)

    # 데이터 분석 결과 출력
    #for row in filtered_data:
    #   if row['점수'] != 0:
    #      print(f"제목: {row['제목']}, 게시판 내용: {row['게시판 내용']}, 점수: {row['점수']}")

    # 부정적인 말들의 점수 평균
    # if negative_scores:
    #    negative_avg = sum(negative_scores) / len(negative_scores)
    #    print(f"직업 : {read} 부정적인 말들의 점수 평균: {negative_avg}")
    # else:
    #    print("부정적인 말들의 점수가 없습니다.")

    # 점수가 매겨진 행들의 점수 평균
    if total_scores:
        total_avg = sum(total_scores) / len(total_scores)
        print(f"직업 : {read} 점수 평균: {(total_avg * 100)}")
        job.append(read)
        avg.append(total_avg * 100)
        
    else:
       print("점수가 매겨진 행들이 없습니다.")
print(job, avg)
df = pd.DataFrame({'직업': job, '점수': avg})
#save_df = job,avg
# csv파일 저장
save_df = df[['직업','점수']].values.tolist()
write_to_csv('./csv/score_final.csv', save_df)
