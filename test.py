n = int(input())
rs = []
for _ in range(n):
    m = int(input())
    rs.append(m)
res = sorted(rs)
for r in res:
    print(r)