length = int(input("길이 입력: "))
if length < 0 :
    print("잘못된 길이 입니다.")
else:
    result = length / 2.54
    print(f"{length}cm는 {result}inch입니다.")