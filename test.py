def make(x,y):
    n = 1
    b = 1
    while n <= x:
        x += 1
        while b <= y:
            res = [x,y]
            b += 1
    return res
x = int(input())
y = int(input())
result = make(x,y)
print(result)

