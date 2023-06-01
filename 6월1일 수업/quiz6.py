n = int(input())
x = 1
rs = []
for x in range(n):
    n -= 1
    rs.append(n)
    x += 1
result = sum(rs)
print(result)