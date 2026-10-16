"""
N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)
print(G)
"""

N = 3
G = [[], [2, 3], [1], [1]]


from collections import deque
seen = [False for _ in range(N+1)]
seen[1] = True
que = deque([1])
parent = [-1 for _ in range(N+1)]
parent[1] = 0
children = [[] for _ in range(N+1)]
while (que):
  v = que.popleft()
  for v2 in G[v]:
    if seen[v2]:
      continue
  
    seen[v2] = True
    children[v].append(v2)
    parent[v2] = v
    que.append(v2)
    
print(parent)
print(children)