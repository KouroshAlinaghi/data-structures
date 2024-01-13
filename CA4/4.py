from collections import deque

n, m, k = [int(x) for x in input().split()]
adjs = dict()

def add_adj(key, value):
    if key in adjs:
        adjs[key].add(value)
    else:
        adjs[key] = {value}

    if value in adjs:
        adjs[value].add(key)
    else:
        adjs[value] = {key}

lights = set()
for _ in range(k):
    y, x = [int(x) for x in input().split()]
    lights.add((x, y))

visited = set()
min_x, min_y, max_x, max_y = 10000, 10000, -1, -1

def dfs(v):
    global min_x, min_y, max_x, max_y
    min_x, min_y, max_x, max_y = min(v[0], min_x), min(v[1], min_y), max(v[0], max_x), max(v[1], max_y)
    visited.add(v)
    x, y = v

    for u in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
        if u in lights and u not in visited:
            min_x, min_y, max_x, max_y = min(u[0], min_x), min(u[1], min_y), max(u[0], max_x), max(u[1], max_y)
            dfs(u)

comps = list()
for light in lights:
    if light not in visited:
        dfs(light)
        comps.append((min_x, min_y, max_x, max_y))
        min_x, min_y, max_x, max_y = 10000, 10000, -1, -1

for comp in comps:
    min_x, min_y, max_x, max_y = comp
    
    for i in range(min_x - 1, max_x + 2):
        for j in range(i, max_x + 2):
            add_adj((i, -1), (j, -1))

    for i in range(min_y - 1, max_y + 2):
        for j in range(i, max_y + 2):
            add_adj((-1, i), (-1, j))

    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            add_adj((x, -1), (-1, y))

dist = {(1, -1): 1}

def bfs(src):
    visited = set()
    queue = deque([src])
    visited.add(src)

    while queue:
        v = queue.popleft()

        for c in adjs[v]:
            if c[0] == 0 or c[0] == m + 1 or c[1] == 0 or c[1] == n + 1:
                continue
            if c not in visited:
                visited.add(c)
                dist[c] = dist[v] + 1
                queue.append(c)

ans = list()

def get_dist():
    ans1 = 1e11
    if (m, -1) in dist:
        ans1 = dist[(m, -1)]
    if (-1, n) in dist:
        ans1 = min(ans1, dist[(-1, n)])
    return ans1

visited = set()
dfs((1, 1))

for sotoon in range(1, max_x + 1):
    dist = {(sotoon, -1): 0}
    bfs((sotoon, -1))
    ans.append(get_dist())

for satr in range(1, max_y + 1):
    dist = {(-1, satr): 0}
    bfs((-1, satr))
    ans.append(get_dist())

chipi = min(ans)

print(chipi if chipi != 1e11 else -1)
