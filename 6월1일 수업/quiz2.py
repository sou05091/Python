apples = int(input("사과의 갯수를 입력해주세요: "))
price = int(input("사과의 가격을 입력해주세요: "))
tax = int(input("부과세율을 입력해주세요"))/10 
# tax = (apples * price)/100*10
result = (apples * price) * tax
print(f"총 가격은 {result:.0f}원 입니다.(부과세 10%)")