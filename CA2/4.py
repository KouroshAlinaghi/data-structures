n_b = [int(x) for x in input().split()]
n, b = n_b[0], n_b[1]
h = [int(x) for x in input().split()]

boots = [tuple([int(x) for x in input().split()]) for _ in range(b)]
boots_ans = dict()
for boot in boots:
    boots_ans[boot] = 0
old_boots = boots.copy()
boots.sort()

l, r = 0, n - 1
first_boot = [(0 if height > boots[-1][0] else 1) for height in h]
bazez = list()
for i in range(1, n):
    if first_boot[i] == 1 and first_boot[i - 1] == 0:
        bazez.append((l, i - 1))
    if first_boot[i] == 0 and first_boot[i - 1] == 1:
        l = i
l, r, m = 0, -1, 0
for baze in bazez:
    m = max(m, baze[1] - baze[0] + 1)
    if m >= baze[1] - baze[0] + 1:
        l, r = baze[0], baze[1]


tools = [0] * n
tools[0] = 1 if first_boot[0] == 0 else 0
for i in range(1, n):
    if first_boot[i] == 1:
        tools[i] = 0
        if first_boot[i - 1] == 0:
            tools[i - tools[i - 1]] = tools[i - 1]
    else:
        if first_boot[i - 1] == 0:
            tools[i] = tools[i - 1] + 1
        else:
            tools[i] = 1

stack = list()
h.reverse()
for i in range(n):
    stack.append((h[i], i))

stack.sort()

ans = r - l + 1
for i in range(b - 1, -1, -1):
    while len(stack) and stack[-1][0] > boots[i][0]:
        index = stack[-1][1]
        if index == 0:
            tools[index] = tools[index + 1] + 1
            tools[index + tools[index + 1]] = tools[index]
        elif index == n - 1:
            tools[index] = tools[index - 1] + 1
            tools[index - tools[index - 1]] = tools[index]
        else:
            tools[index] = tools[index - 1] + tools[index + 1] + 1
            tools[index + tools[index + 1]] = tools[index]
            tools[index - tools[index - 1]] = tools[index]

        ans = max(ans, tools[index])
        stack.pop()

    if ans >= boots[i][1]:
        boots_ans[boots[i]] = 0
    else:
        boots_ans[boots[i]] = 1

for boot in old_boots:
    print(boots_ans[boot])
