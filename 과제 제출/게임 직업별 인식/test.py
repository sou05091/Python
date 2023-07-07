import csv
import matplotlib.pyplot as plt
import pandas as pd

def read_price(file_path):
    rs = []
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            rs.append(row)
    return rs
            
def read_job(file_path):
    rs = []
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            rs.append(row)
    return rs

rp = read_price('./csv/price_final.csv')
rj = read_job('./csv/score_final.csv')

job_names = [rj[i][0] for i in range(len(rj))]
final_scores = []
for i in range(len(rp)):
    for j in range(len(rj)):
        if rp[i][0] == rj[j][0]:
            try:
                final_rp = (float(rp[i][1]) / 100) * (3.5 / 10)
                final_rp_round = round(final_rp, 2)
                final_rj = float(rj[j][1]) * (6.5 / 10)
                final_rj_round = round(final_rj, 2)
                final_score = final_rj_round - final_rp_round 
                final_score_round = round(final_score, 2)
                print(f"job is {rj[j][0]}, final score is {final_score_round}") 
                final_scores.append(final_score_round)
                
            except ValueError:
                continue

# 그래프 크기 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 12  # 전체 글자 크기 설정
fig, ax = plt.subplots(figsize=(8, 6))  # 그래프의 가로 8인치, 세로 6인치

# 막대 그래프 그리기
ax.bar(job_names, final_scores)
ax.set_title('Final Score', fontsize=14)  # 제목 글자 크기 설정
ax.set_xlabel('Job', fontsize=12)  # x축 레이블 글자 크기 설정
ax.set_ylabel('Score', fontsize=12)  # y축 레이블 글자 크기 설정
ax.tick_params(axis='x', rotation=90)  # x축 눈금 방향 설정

plt.show()
