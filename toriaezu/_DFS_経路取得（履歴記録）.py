# 深さ優先探索
# ABC270-Cがシンプルな探索問題。X から Y への経路を求める問題。

"""
file = open(__file__ + "\\..\\input.txt")
N, X, Y = map(int, file.readline().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = map(int, file.readline().split())
  G[u].append(v)
  G[v].append(u)
file.close()

"""
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

# 深さ優先探索のときはこれをつけるように！
# また、PyPy は再帰が遅いので CPython を使うように！
import sys
sys.setrecursionlimit(10**6)

def dfs(v, d):

  for neibor in G[v]:
    if d[neibor] != -1:
      continue
    
    d[neibor] = d[v] + 1
    dfs(neibor, d)

dist = [-1 for _ in range(N+1)]
dist[X] = 0
dfs(X, dist)
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
  
