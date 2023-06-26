# KNU 한국어 감성 사전 파일사용!

import pandas as pd
import json
import re

# JSON 파일 읽기
with open('SentiWord_info.json', mode='r', encoding='utf-8-sig') as file:
    json_data = json.load(file)

# JSON 데이터를 단어와 점수로 매핑하는 사전 생성
word_scores = {item['word']: int(item['polarity']) for item in json_data}

# CSV 파일 읽기
df = pd.read_csv('output.csv', encoding='utf-8-sig')

# 특정 단어 열에 대해 점수 매기기
word_column = '제목'  # 점수를 매길 열 이름
score_column = 'score'  # 점수를 저장할 열 이름

def get_word_score(text):
    words = re.findall(r'\b\w+\b', text)  # 단어 추출 (한국어는 형태소 분석기를 사용해야 정확한 단어 추출이 가능합니다.)
    scores = [word_scores.get(word, 0) for word in words]  # 단어에 해당하는 점수 매핑
    return sum(scores)  # 점수의 합 반환

df[score_column] = df[word_column].apply(get_word_score)

# 결과 출력
print(df[score_column])

