# ダイクストラ法（ヒープを用いた高速化版）
# 使用条件は各辺の重みがマイナスではないこと。計算量は O((N+M)logN)
# 負の辺があるときはベルマンフォード法などを使う。
"""
## 概要
辺に重みがない場合は幅優先探索で解けるが、
辺に重みがある場合は全通りを計算しなくてはいけなくなり、
辺 M 個に対し O(M!) となってしまう。そこをうまくやる。

## 手順
1. 始点を最短距離 0 とする。
2. まだ訪れていない頂点のうち、最短距離がわかっている頂点の中で最も短い頂点に移動する。
3. 2. で移動してきた頂点の隣接点について最短距離を設定、または更新する。
4. 全ての頂点の最短距離がわかったら終わり。

## Priority Queue, もしくは heap を用いた工夫
手順 2. で最短距離が最も短い頂点を求める際、これらを使って求めておくことができる。


"""

import heapq

def dijkstra(start, G):
  n = len(G)
  # 初期化
  INF = 10**18
  d = [INF for _ in range(n)] # 頂点 1 から頂点 i までの distance (暫定最短)
  d[start] = 0
  f = [False for _ in range(n)] # 頂点 i までの距離が確定したかどうか
  prev = [-1 for _ in range(n)] # 最短路の直前の頂点

  # 根が最小値になるようなヒープを作る
  d_heap = list()
  heapq.heapify(d_heap)

  # ヒープの初期化
  #for v in range(1, N+1):
  #  heapq.heappush(d_heap, (d[v], v))
  d_heap = [(0, start)] # これだけでいいらしい

  while (len(d_heap) > 0):
    u = heapq.heappop(d_heap)[1] # 常に距離が最短となる頂点を取り出す
    if f[u]: continue
    for neibor in G[u]:
      t, w = neibor[0], neibor[1]
      if d[t] > d[u] + w:
        d[t] = d[u] + w
        heapq.heappush(d_heap, (d[t], t))
        # 経路復元が必要ならここに prev[t] = u を書く
        prev[t] = u
    f[u] = True

  # prev[i] は頂点 start から頂点 i に向かう最短経路において、i の直前にいた頂点の番号を格納する
  return d, prev

# 経路復元
# prev[i] を用いて 頂点 i から最短経路を逆順に辿っていく。当然、最短経路分の辺数だけ計算量がかかる。
def get_path(t, prev):
  path = []
  while t != -1:
    path.append(t) # t が start になるまで prev[t] をたどる
    t = prev[t]
  path.reverse()
  return path

#N, M = map(int, "4 3".split())
#U = [-1 for _ in range(M+1)]
#V = [-1 for _ in range(M+1)]
#W = [-1 for _ in range(M+1)]
#U[1], V[1], W[1] = 2, 4, 6
#U[2], V[2], W[2] = 1, 2, 11
#U[3], V[3], W[3] = 2, 3, 7

file = open(__file__ + "\\..\\_dijkstra_input.txt")
N, M = map(int, file.readline().split())
U = [-1 for _ in range(M+1)]
V = [-1 for _ in range(M+1)]
W = [-1 for _ in range(M+1)]
G = [[] for _ in range(N+1)]
for i in range(1, M+1):
  u, v, w = map(int, file.readline().split())
  U[i], V[i], W[i] = u, v, w
  # u, v, w = U[i], V[i], W[i]
  G[u].append([v, w])
file.close()

d, pre = dijkstra(1, G)
for i in range(1, N+1):
  print(d[i])
  path = get_path(i, pre)
  print(path)

