"""
# 木_重心

## 説明
木の重心とは、おおまかには頂点数を半々に割ることができる位置にある頂点のイメージ。
厳密には、頂点 v を取り除いたときにできる各連結成分の頂点数が
すべて N/2 以下になる頂点が重心である。
1個または2個ある。このコードではそれらを配列で得る。

## 計算量 O(N)
## メモリ O(N)

## 使われる問題
ABC479-E https://atcoder.jp/contests/abc479/tasks/abc479_e

## 処理の概要
1. 適当な頂点、たとえば1を根にして木を根付き木にする。
2. DFSで各頂点の部分木サイズ part_size[v] を求める。v 自身も含める。
3. 各頂点 v について、「vを消したとき各方向に何頂点あるか」を調べる。
      * 子 u の方向 → part_size[u]
      * 親の方向 → N - part_size[v] （子全体の和 + 自身 =  part_size[v] なので）
4. その最大値が N // 2 以下なら v が重心。

#########################################################
## ライブラリ本体 + 使用例

### 入力例
9
4 6
2 3
1 5
7 8
2 9
5 6
2 6
7 9

N = int(input())
G = [[] for _ in range(N+1)]
for i in range(1, N):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)
"""

import sys
sys.setrecursionlimit(10**7)
N = 9
G = [[], [5], [3, 9, 6], [2], [6], [1, 6], [4, 5, 2], [8, 9], [7], [2, 7]]
# 部分木の大きさを求める
part_size = [1 for _ in range(N+1)]
parent = [-1 for _ in range(N+1)]

def dfs_part_size(v, p): # 部分木のサイズを求める関数
  parent[v] = p
  ret = 1
  for v2 in G[v]:
    if v2 == p:
      continue
    ret += dfs_part_size(v2, v)
  part_size[v] = ret
  return ret

dfs_part_size(1, -1)

# v を削除したときに残る連結成分が、いずれも N //2 以下の大きさなら v は重心である
gravs = []
for v in range(1, N+1):
  max_part_size = N - part_size[v] # 親
  for v2 in G[v]: # 子たち
    if v2 == parent[v]:
      continue
    max_part_size = max(max_part_size, part_size[v2])
  if max_part_size <= N // 2:
    gravs.append(v)

print(gravs)
