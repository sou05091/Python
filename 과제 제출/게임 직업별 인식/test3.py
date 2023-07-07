import csv
import matplotlib.pyplot as plt
import pandas as pd

def write_to_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['직업', '평균가격'])
        writer.writerows(data)

def plot_bar_graph_price(file_path):
    # CSV 파일에서 데이터 읽기
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # 데이터 추출
    job_prices = {}  # 직업별 가격을 저장할 딕셔너리
    for item in data:
        job = item['직업']
        price = float(item['가격'])
        if job in job_prices:
            # 이미 해당 직업이 딕셔너리에 있는 경우
            # 현재 가격과 기존 가격을 비교하여 낮은 가격과 높은 가격으로 갱신
            if price < job_prices[job]['낮은가격']:
                job_prices[job]['낮은가격'] = price
            if price > job_prices[job]['높은가격']:
                job_prices[job]['높은가격'] = price
        else:
            # 해당 직업이 딕셔너리에 없는 경우
            # 새로운 직업과 해당 가격으로 딕셔너리에 추가
            job_prices[job] = {'낮은가격': price, '높은가격': price}

    # 평균 가격 계산을 위한 데이터 프레임 생성
    df = pd.DataFrame({'직업': [], '낮은가격': [], '높은가격': []})
    for job, prices in job_prices.items():
        df = pd.concat([df, pd.DataFrame({'직업': [job], '낮은가격': [prices['낮은가격']], '높은가격': [prices['높은가격']]})])

    # 평균 가격 계산
    df['평균가격'] = (df['낮은가격'] + df['높은가격']) / 2
    test = df['평균가격']/100
    # csv파일 저장
    save_df = df[['직업','평균가격']].values.tolist()
    write_to_csv('price_test.csv', save_df)

    # pivot_table 생성
    plt.rcParams['font.family'] = 'Malgun Gothic'
    pivot_table = df.pivot_table(index='직업', values=['낮은가격', '높은가격', '평균가격'])

    # 그래프 그리기
    pivot_table.plot(kind='bar', figsize=(15, 6))
    plt.xlabel('직업')
    plt.ylabel('가격')
    plt.title('가격 분포')
    plt.legend(title='구분')
    plt.show()

# CSV 파일로 막대 그래프 그리기
plot_bar_graph_price('./csv/test.csv')
