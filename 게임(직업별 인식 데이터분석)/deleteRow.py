import csv

input_file = '소서(title).csv'
output_file = 'output.csv'
delete_word = '질문'

# CSV 파일 읽기
with open(input_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

# 특정 단어가 들어간 행 삭제
filtered_rows = [row for row in rows if delete_word not in row[0]]

# 변경된 데이터를 CSV 파일로 저장
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_rows)

print(f"특정 단어가 들어간 행이 삭제된 데이터가 {output_file}로 저장되었습니다.")
