import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv', encoding='utf-8-sig')

# 문자열 형식으로 변환
df['제목'] = df['제목'].astype(str)

# 정규 표현식을 사용하여 '[...]' 형식의 텍스트 제거
df['제목'] = df['제목'].str.replace(r'\[.*?\]', '', regex=True)

# 특정 단어 삭제
# 특정 단어 추가하여 삭제
delete_words = ['소서', '환류', '점화','진짜', '이제','는','그냥','가','좀','팔찌','세팅','근데']  # 삭제할 단어 리스트
for word in delete_words:
    df['제목'] = df['제목'].str.replace(word, '')

# 단어별 등장 횟수 계산
word_counts = df['제목'].str.split().explode().value_counts()

# 상위 10개 단어 선택
top_10_words = word_counts.head(10)

# 막대 그래프 그리기
plt.rc('font', family='Malgun Gothic')
plt.bar(top_10_words.index, top_10_words.values)
plt.xlabel('단어')
plt.ylabel('등장 횟수')
plt.title('상위 10개 단어 등장 횟수')
plt.xticks(rotation=45)
plt.show()
