# ワーシャルフロイド法
# ・全ての頂点間の最短経路を求める。
# ・負の辺を含むグラフでも使用できる。
# ・計算量は頂点数を V として O(V^3) なので使える場面はそれなりに限られる。

# 参考：https://atcoder.jp/contests/abc208/tasks/abc208_d
# N 個の都市と M 本の道路がある。
# 都市 A[i] から都市 B[i] へ繋がる一方通行の道があり、移動にはそれぞれ C[i] かかる。
# 
"""
N, M = map(int, input().split())
A = [0 for _ in range(M+1)]
B = [0 for _ in range(M+1)]
C = [0 for _ in range(M+1)]
for i in range(1, M+1):
  A[i], B[i], C[i] = map(int, input().split())
print(A)
print(B)
print(C)
"""
N, M = 5, 20
A = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
B = [0, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4]
C = [0, 6, 10, 4, 1, 5, 9, 8, 6, 5, 1, 7, 9, 4, 6, 4, 8, 2, 5, 6, 5]
# 1. 初期化：
#       グラフ上のすべての頂点の間の距離を初期化します。
#       自分同士は距離 0 、道が無いところは INF
INF = 10 ** 9
dist = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
  dist[i][i] = 0
for i in range(1, M+1):
  dist[A[i]][B[i]] = C[i]

# 試しに出力
for i in range(1, N+1):
  for j in range(1, N+1):
    if dist[i][j] == INF: print("INF", end=" ") 
    else: print(dist[i][j], end=" ")
  print("")
print("")

# 2. ループ：
#       すべての頂点について、他のすべての頂点までの最短距離を更新します。
ans = 0
for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      # 3. 最短距離の更新：
      #       更新された距離を使用して、各頂点の他の頂点への最短距離を更新します。

      # i - j 間の距離 = i - k 間の距離 + k - j 間の距離
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 全頂点間の距離を出力
for i in range(1, N+1):
  for j in range(1, N+1):
    if dist[i][j] == INF: print("INF", end=" ") 
    else: print(dist[i][j], end=" ")
  print("")
print("")

#######################################################################
# 次に、これを応用して N 頂点ではなく
# H * W のマス目を移動する場合を考える。
# 頂点数が H * W になり
# 道は H * (W-1) + (H-1) * W 本になる。
#
# 全てのマス = 頂点に番号を振る。1 から H * W まで。
# (i, j) = W * (i-1) + j になる。

H, W = 4, 5
S = [
  ["-", "-", "-", "-", "-", "-"],
  ["-", ".", "#", ".", "#", "#"],
  ["-", ".", ".", ".", ".", "#"],
  ["-", "#", ".", ".", ".", "."],
  ["-", ".", ".", "#", ".", "."]
]
"""
.#.##
....#
#....
..#..
"""
# 1. 初期化
dist = [[INF for _ in range(H * W + 1)] for _ in range(H * W + 1)]
for i in range(1, H * W + 1):
  dist[i][i] = 0
# 全てのマスについて、隣接マスへの移動ができるかどうかを調べる。
# グラフでいうと、頂点から辺を張っていく。
for i in range(1, H+1):
  for j in range(1, W+1):
    for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
      nx = i + d[0]
      ny = j + d[1]
      if 1 <= nx <= H and 1 <= ny <= W and S[nx][ny] == ".":
          # (i, j) -> (nx, ny) に辺を張る。コストは 1。
          dist[W * (i - 1) + j][W * (nx - 1) + ny] = 1

for k in range(1, H*W+1):
  for i in range(1, H*W+1):
    for j in range(1, H*W+1):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 全頂点間の距離を出力
for i in range(1, H*W+1):
  for j in range(1, H*W+1):
    if i % W == 0:
      x, y = i // W, W
    else:
      x, y = (i // W) + 1, i % W
    if S[x][y] == ".":
      if dist[i][j] == INF: print("INF", end=" ")
      else: print(dist[i][j], end=" ")
    else:
      print("#", end="")
  print("")
print("")





