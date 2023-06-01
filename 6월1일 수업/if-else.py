# num = int(input("숫자를 입력하세요"))
# sign = "양수" if num > 0 else ("음수" if num < 0 else "0")
# print(sign)
import math

num = float(input("양수를 입력하세요: "))

result = math.sqrt(num) if num > 0 else "잘못된 입력입니다."

print("결과: ", result)
