# 幅優先探索
# ABC270-Cがシンプルな探索問題。X から Y への経路を求める問題。

N, X, Y = 5, 2, 5
G = [[], [2, 3], [1], [1, 4, 5], [3], [3]]
"""
N, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)
"""

from collections import deque
dist = [-1 for _ in range(N+1)]
dist[X] = 0
que = deque([])
que.append(X)

while (len(que)> 0):
  v = que.popleft()
  for neibor in G[v]:
    if dist[neibor] == -1:
      dist[neibor] = dist[v] + 1
      que.append(neibor)
#print(dist)

# ゴールから dist の数値を頼りに逆にたどり、最後に配列を反転させて経路を取得する。
v = Y
root = [v]
while (dist[v] > 0):
  for neibor in G[v]:
    if dist[neibor] == dist[v] - 1:
      #print(neibor, end=" ")
      root.append(neibor)
      v = neibor
root.reverse()
print(*root)
  
