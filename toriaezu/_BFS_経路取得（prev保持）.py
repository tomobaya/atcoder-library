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
que = deque([])
que.append((X, -1))

prev = [-1 for _ in range(N+1)] # 前にいた点を格納していく方式
seen = [False for _ in range(N+1)]

while (len(que)> 0):
  v, p = que.popleft()
  seen[v] = True
  prev[v] = p

  for neibor in G[v]:
    if seen[neibor]:
      continue

    que.append((neibor, v))

# Y から出発し、逆方向に prev をたどる。
root = list()
now = Y
while (now != -1):
  root.append(now)
  now = prev[now]
root.reverse()
print(*root)
