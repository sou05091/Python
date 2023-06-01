kor = int(input("국어 성적"))
eng = int(input("영어 성적"))
math = int(input("수학 성적"))
if 100 >= kor >= 0 and 100 >= eng >= 0 and 100 >= math >= 0:
    print(f"성적 결과 국어: {kor} 영어: {eng} 수학: {math}")
    평균점수 = (kor * 0.4 + eng * 0.4 + math * 0.2)
    print(f"평균점수는 : {평균점수:.2f}")
    if 평균점수 >= 90:
        grade = "A"
    elif  90 > 평균점수 >= 80:
        grade = "B"
    elif 80 > 평균점수 >= 70:
        grade = "C"
    elif 70 > 평균점수 >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"학점은: {grade}")
else:
    print("점수를 잘못입력하였습니다.")