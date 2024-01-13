n = int(input())
a = list()
maxn = 1e9
leftest = [maxn] * int(1e7)
rightest = [-maxn] * int(1e7)

a.append(int(input()))
leftest[a[-1]] = min(leftest[a[-1]], 0)
rightest[a[-1]] = max(rightest[a[-1]], 0)
index = 1

for i in range(n - 1):
    inp = int(input())
    if inp != a[-1]:
        a.append(inp)
        leftest[inp] = min(leftest[inp], index)
        rightest[inp] = max(rightest[inp], index)
        index += 1

s = set()
rightest_left = maxn
ans = 1

if max(a) == 0:
    print(0)
    exit(0)

for i in range(len(a)):
    x = a[i]
    if x == 0:
        continue
    
    if not x in s:
        s.add(x)
        ans = max(ans, len(s))

    if i == rightest[x]:
        s.remove(x)

for i in range(len(a)):
    x = a[i]

    if x != 0:
        rightest_left = min(rightest_left, rightest[x])

    if i == 0:
        continue

    if rightest_left > i and rightest[x] > rightest_left and leftest[x] == i:
        print(-1)
        exit(0)

    if x == 0 and i < rightest_left:
        print(-1)
        exit(0)

print(ans)
