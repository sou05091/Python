import pandas as pd

df = pd.read_csv('output.csv', encoding='utf-8')

delete_word = '소서','환류','점화'

# 문자열 메서드를 사용하여 특정 단어 삭제
df['제목'] = df['제목'].str.replace(delete_word, '')

# 수정된 DataFrame을 새로운 CSV 파일로 저장
df.to_csv('output1.csv', index=False, encoding='utf-8-sig')
