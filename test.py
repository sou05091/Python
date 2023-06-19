n = int(input())
a = input().split()
m = int(input())
b = input().split()
rs = []
res = 0
for x in b:
    for y in a:
        if x == y:
            res += 1
    rs.append(res)
print(rs)