from collections import deque
import math

n = int(input())
t = int(input())

dist = {"abcdefgh"[:n]: 0}

def bfs(src):
    visited = set()
    queue = deque([src])
    visited.add(src)

    while queue:
        v = queue.popleft()

        for l in range(n):
            for r in range(l + 1, n):
                u = v[:l]
                for i in range(r, l - 1, -1):
                    u += v[i]
                u += v[r + 1:]

                if u not in visited:
                    visited.add(u)
                    dist[u] = dist[v] + 1
                    queue.append(u)


bfs("abcdefgh"[:n])

for _ in range(t):
    s1, s2 = input().split()
    transition_table = dict()
    for i in range(n):
        transition_table[s1[i]] = "abcdefgh"[i]
    s = str()
    for c in s2:
        s += transition_table[c]
    print(int(math.fabs(dist[s])))
