n = int(input())

visited = [False] * (n + 1)
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

perm = [int(x) for x in input().split()]
par = [-1 for _ in range(n + 1)]
h = [-1 for _ in range(n + 1)]

ans = list()

def dfs(v, height):
    visited[v] = True
    h[v] = height

    for u in adj[v]:
        if not visited[u]:
            par[u] = v
            dfs(u, height + 1)

dfs(1, 0)

cur = perm[0]
while cur != 1:
    ans.append(cur)
    cur = par[cur]
ans.append(1)
ans.reverse()

for i in range(1, len(perm)):
    src, dest = perm[i - 1], perm[i]
    b = [dest]
    if h[src] > h[dest]:
        for _ in range(h[src] - h[dest]):
            src = par[src]
            ans.append(src)
    else:
        for _ in range(h[dest] - h[src]):
            dest = par[dest]
            b.append(dest)

    while src != dest:
        src = par[src]
        dest = par[dest]
        ans.append(src)
        b.append(dest)

    ans.pop()
    b.reverse()
    ans += b

cur = ans[-1]
ans.pop()
while cur != 1:
    ans.append(cur)
    cur = par[cur]

if len(ans) == 2 * n - 2:
    print(" ".join([str(x) for x in ans]))
else:
    print(-1)
