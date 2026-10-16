"""
BFS によるグリッド探索のテンプレート。
始点 (1,1) から各マスへの最短距離を表示する。
"""
#H, W = 4, 5
#S = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', '.', '.', '.', '.', '.'], [' ', '.', '#', '.', '#', '.'], [' ', '.', '.', '.', '#', '.'], [' ', '#', '#', '.', '.', '.']]

# 入力
H, W = map(int, input().split())
S = [[" " for _ in range(W+1)] for _ in range(H+1)]
for i in range(1, H+1):
  line = input()
  for j in range(1, W+1):
    S[i][j] = line[j-1]

# 表の出力
for i in range(1, H+1):
  for j in range(1, W+1):
    print(S[i][j], end=" ")
  print("")

# BFS
## 準備
from collections import deque
que = deque([])
INF = 10**20
dist = [[INF for _ in range(W+1)] for _ in range(H+1)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # グリッドの始点が左上として、それぞれ上下左右。 ["^", "v", "<", ">"]
## 初期化
que.append((1, 1))
dist[1][1] = 0
## 探索
while (que):
  q = que.popleft()
  x, y = q[0], q[1]
  for d in range(4):
    nx, ny = x + dx[d], y + dy[d]
    if 1 <= nx <= H and 1 <= ny <= W and S[nx][ny] != "#":
      if dist[nx][ny] > dist[x][y] + 1:
        dist[nx][ny] = dist[x][y] + 1
        que.append((nx, ny))
## 距離の出力
for i in range(1, H+1):
  for j in range(1, W+1):
    if dist[i][j] == INF:
      print("#", end=" ")
    else:
      print(dist[i][j], end=" ")
  print("")

