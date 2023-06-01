time = int(input("초를 입력해주세요."))
min = time // 60
sec = time % 60
print(f"{min:.0f}분 {sec}초 입니다")