n = int(input())
pos = [0] * (n + 1)
permutation = [int(x) for x in input().split()]
for i in range(n):
    pos[permutation[i]] = i

st = list()
prv = [-1] * (n + 1)
for k in range(n, 0, -1):
    while len(st) and st[-1] > pos[k]:
        st.pop()
    if len(st):
        prv[pos[k]] = st[-1]
    st.append(pos[k])

st = list()
ans = 0

for x in range(n + 1):
    while len(st) and st[-1] > pos[x]:
        if (prv[st[-1]] != -1) and (len(st) <= 1 or prv[st[-1]] != prv[st[-2]]):
            ans -= 1
        st.pop()

    if (prv[pos[x]] != -1) and (len(st) == 0 or prv[pos[x]] != prv[st[-1]]):
        ans += 1

    st.append(pos[x])
    print(ans)
