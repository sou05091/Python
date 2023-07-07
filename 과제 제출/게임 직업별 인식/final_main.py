import csv
import matplotlib.pyplot as plt
import pandas as pd

def read_price(file_path):
    rs = []
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            rs.append(row)
            #try:
             #   rs = (float(row[1])/100)*(7/10)
              #  rs_round = round(rs,2)
               # print(rs_round)
            #except ValueError:
             #   continue
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
count = 0
for i in range(len(rp)):
    for j in range(len(rp)):
        if rp[i][0] == rj[j][0]:
            #print(rp[i][0],rj[j][0])
            try:
                final_rp = (float(rp[i][1])/100)*(2/10)
                final_rp_round = round(final_rp,2)
                print(final_rp_round)
                final_rj = (float(rj[j][1]))*(8/10)
                final_rj_round = round(final_rj,2)
                print(final_rj_round)
                final_score = final_rj_round - final_rp_round 
                final_score_round = round(final_score,2)
                print(f"job is {rj[j][0]}, final score is {final_score_round}") 
                
                # 그래프 그리기
                plt.rcParams['font.family'] = 'Malgun Gothic'
                plt.rcParams['font.size'] = 13
                plt.bar(rj[j][0],final_score_round, color='gray')
                plt.title('Final Score')
                plt.xlabel('Job')
                plt.ylabel('Negative Score')
                plt.xticks(rotation=70)
            except ValueError:
                continue                
plt.show()
        #print(rp[i][0],rj[i][0])