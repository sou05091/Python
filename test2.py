n = int(input())
a = set(input().split())
m = int(input())
b = input().split()

results = []

for x in b:
    if x in a:
        results.append(1)
    else:
        results.append(0)

print(*results, sep='\n')
