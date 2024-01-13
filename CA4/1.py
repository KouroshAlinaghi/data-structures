n, m = [int(x) for x in input().split()]

visited = [False] * (n + 1)
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

a = list()
def dfs(v, h):
    visited[v] = True

    if h:
        a.append(v)

    for u in adj[v]:
        if not visited[u]:
            dfs(u, not h)

for v in range(1, n + 1):
    if not visited[v]:
        dfs(v, True)

print(len(a))
print(" ".join([str(x) for x in a]))
