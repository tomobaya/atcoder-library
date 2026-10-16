"""
ABC167-D
https://atcoder.jp/contests/abc167/tasks/abc167_d

遷移の周期性を扱う問題。
グラフとして作ってそれを処理する関数にした。

町 1 からスタートして、A[i] にしたがって移動していく。
K 回の移動のあとどこに行くかを問われる問題。Kが大きいので周期性を利用して計算回数を減らす。
"""

def period_of_graph(graph, start):
  # 探索の開始地点を start とする。
  # 最初はループの値を 0 とする。移動した回数（通った辺の本数）が値となる。
  now = start
  next = graph[now]
  dist = [-1 for _ in range(len(graph)+1)]
  dist[now] = 0
  while (dist[next] == -1):
    dist[next] = dist[now] + 1
    now = next
    next = graph[now]
  # now : ループの終着点かつ開始点
  # loop_start : ループが開始する時点でのステップ数
  # loop_size : ループ1周あたりのステップ数
  loop_start = dist[next]
  loop_size = dist[now] - dist[next] + 1
  #print(dist)
  #print(now, next)
  #print(loop_start, loop_size)

  return loop_start, loop_size, dist


N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
#N, K = 4, 5
#A = [0, 3, 2, 4, 1] # 1 -> 3 -> 4 -> 1 のループ
#N, K = 6, 727202214173249351
#A = [0, 6, 5, 2, 5, 3, 2]

loop_start, loop_size, dist = period_of_graph(A, 1)
#print(loop_start, loop_size)

# 使い方
# 移動回数から loop_start を引く
# それを loop_size で割った余りにする（周回数の圧縮） 周回数は loop_size で割った商
# この余りに loop_start をくっつければ OK. O(N) 回で処理できるようになるはず。
if K >= loop_start:
  K -= loop_start
  loop_num = K // loop_size
  K %= loop_size
  K += loop_start

# あとは愚直に処理
now = 1
while (K > 0):
  #print(K, now)
  now = A[now]
  K -= 1
print(now)
