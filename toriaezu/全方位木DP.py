"""
参考 URL https://algo-logic.info/tree-dp/

入力グラフ
     2    5
  ／   ／
1 － 3 ー 6
  ＼ 
     4 ー 7

根となる頂点を1つ選ぶ。その頂点から最も遠い点までの距離を求める。
これを全ての頂点について行う。
愚直にやると木DPをN回やるので O(N^2) だが、
モノイドの累積和を使った工夫により O(N) に抑える。

木を無向グラフとみなす。
まず頂点を一つ選び普通の木DPを一度行う。
ある頂点について、部分木の一つが持つ値は
他の部分木を merge した値になる。
この、他の部分木を merge するときに累積和（累積 merge）が利用でき、計算量が抑えられる。

"""
import sys
sys.setrecursionlimit(10**7)

N = 7
G = [[], [2,3,4], [1], [1,5,6], [1, 7], [3], [3], [4]]

dp = [[] for _ in range(N+1)] # dp[v][i] := v から出る i 番目の有向辺に対応する部分木の dp
ans = [-1 for _ in range(N+1)] # 頂点 v を根とする木の答え

identity = -1

def merge(u, v): # 2変数に何らかの演算を行う。ここでは max.
  return max(u, v)

def calc(tmp): # dp の遷移の計算に使う。ここでは +1 するだけ。
  return tmp + 1

# 帰りがけ順 = 部分木を全て終わらせてから最後に根を見る。
# for で子を調べて、再帰関数を呼び出し、その後に v 自身を記録する。
def dfs(v, parent):
  now = identity # 初期値はモノイドの単位元
  degree = len(G[v])
  # dp[v] は vから出る有向辺の本数分のDPを格納するリスト
  dp[v] = [identity for _ in range(degree)]
  for i in range(degree):
    u = G[v][i]
    if u == parent: continue
    dp[v][i] = dfs(u, v)
    now = merge(now, dp[v][i])
  return calc(now)

def dfs2(v, parent_dp, parent):
  degree = len(G[v])
  for i in range(degree):
    if G[v][i] == parent:
      dp[v][i] = parent_dp
  
  # 累積 merge をとる。
  cum_left = [identity for _ in range(degree + 1)]
  cum_right = [identity for _ in range(degree + 1)]
  for i in range(degree):
    cum_left[i+1] = merge(cum_left[i], dp[v][i])
  for i in range(degree - 1, -1, -1):
    cum_right[i] = merge(cum_right[i+1], dp[v][i])
  # 頂点 v の答え : 全ての子方向の dp を merge して（累積和の最後の値がそのままこれになる）calc したもの
  ans[v] = calc(cum_left[degree])
  # 隣接点について同様に計算する
  for i in range(degree):
    u = G[v][i]
    if u == parent: continue
    # その頂点以外の他の部分木を全て merge したやつ。累積 merge を使えば求められる。
    other_merge = merge(cum_left[i], cum_right[i+1])
    next_dp = calc(other_merge)
    dfs2(u, next_dp, v)


dfs(1, -1)
print(dp)
dfs2(1, identity, -1)
print(ans)
