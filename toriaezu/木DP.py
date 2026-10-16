"""
参考 URL https://algo-logic.info/tree-dp/

入力グラフ
     2    5
  ／   ／
1 － 3 ー 6
  ＼ 
     4 ー 7

根となる頂点を1つ選ぶ。その頂点から最も遠い点までの距離を求める。
木を有向グラフとみなし、根から帰りがけ順に探索していく。
O(N) かかる。

"""

import sys
sys.setrecursionlimit(10**7)

N = 7
G = [[], [2,3,4], [], [5,6], [7], [], [], []] # 有向グラフと見なす
#G = [[], [2,3,4], [1], [1,5,6], [1, 7], [3], [3], [4]]

def merge(u, v): # 2変数に何らかの演算を行う。ここでは max.
  return max(u, v)

def calc(tmp): # dp の遷移の計算に使う。ここでは +1 するだけ。
  return tmp + 1

# 帰りがけ順 = 部分木を全て終わらせてから最後に根を見る。
# for で子を調べて、再帰関数を呼び出し、その後に v 自身を記録する。
def dfs(v, parent):
  if len(G[v]) == 0:
    dp[v] = 0
    return 
  tmp = 0 # 何らかの演算の初期値。例えば今は正整数の max を求めるので 0 にしておく。
  for v2 in G[v]:
    if v2 == parent: continue
    dfs(v2, v)
    tmp = merge(tmp, dp[v2])
  dp[v] = calc(tmp)

dp = [-1 for _ in range(N+1)]
dfs(1, -1)
print(dp)
