sco = int(input("학점을 입력하세요"))
if sco < 40:
    print("1학년 입니다.")
elif 40 <= sco < 80:
    print("2학년 입니다.")
elif 80 <= sco:
    print("졸업반입니다.")