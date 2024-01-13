n, q = [int(x) for x in input().split()]

visited = [False] * (n + 2)
par = [-1] * (n + 2)
adj = [list()] * (n + 2)

meow = [int(x) for x in input().split()]
for i in range(n - 1):
    par[i + 2] = meow[i]
queries = [set([int(x) for x in input().split()][1:]) for _ in range(q)]
for v in range(2, n + 1):
    adj[par[v]].append(v)
    adj[v].append(par[v])

def dfs(v, i, changes):
    global visited
    visited[v] = True
    if v in queries[i]:
        if not changes & 1:
            changes += 1
    else:
        if changes & 1:
            changes += 1

    for u in adj[v]:
        if not visited[u]:
            changes = max(dfs(u, i, changes), changes - 1)

    return changes 

for i in range(q):
    visited = [False] * (n + 2)
    print(dfs(1, i, 0))
