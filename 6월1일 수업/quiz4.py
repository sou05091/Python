time = int(input("분을 입력하세요: "))
d = time // (24*60)
h = (time//60) % 24
time = time % 60
print(f"{d}일 {h}시 {time}분")