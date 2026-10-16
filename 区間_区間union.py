"""
# 区間_区間union

## 説明
(L, R) の配列で複数の区間が渡される。
それらを合成し、重複する区間・隣接する区間をまとめる。
まとめたもの（和集合）を返す。

例：
[(1,4), (2,5), (7,8), (9,12)]
→ [(1,5), (7,12)]

2種類作った。
1. オフライン処理。全ての区間を追加した最後の結果を返す。union_section という関数にしてある。
2. オンライン処理。区間が1つ追加されるたびに途中経過が保持される。print で出力させてる。

## 計算量
1. ソート部分が O(N logN)、ちなみにマージは O(N)
2. 全体で O(Q logQ) (※)

(※)
1クエリで多数の区間をマージする場合があるが、一度削除された区間は再登場しないため、全体では O(Q log Q)。

2. の方が高度だが遅い傾向にある。

## メモリ
1. O(N)
2. O(Q)

## 使われる問題
1. ABC478-D https://atcoder.jp/contests/abc478/tasks/abc478_d
2. ABC435-E https://atcoder.jp/contests/abc435/tasks/abc435_e

## 処理の概要
1. ソートし、右隣を1つずつ順に見ながらマージしていく。
2. 新たな (L, R) について
    1. L の入る位置を二分探索で求める。
    2. 右隣を1つずつ順に見ながら R を見比べ、マージしていく。
    既存区間との位置関係によって細かい場合分けがあるが、よく見ていけばかなり単純な条件で分けられる。
    L, R ともにそれぞれ 2 種類の場合分けしかない。

    
#########################################################
## ライブラリ本体 + 使用例
その1 
"""
# tuple (L, R) は区間 [L, R] を表し、必ず L <= R とする。
A = [(2, 5), (1, 4), (2, 5), (7, 8), (7, 9), (9, 12), (18, 20), (10, 13), (15, 19), (21, 22)]

def union_section(ary):
  ary = sorted(ary)
  leng = len(ary)
  #print(ary)
  # 左から見ていく。右隣とマージできるならする。
  # できないならいったん切って答えを格納し、次に移る。
  if leng <= 1:
    return ary
  
  i = 0
  ret = []
  while i <= leng - 1:
    (L1, R1) = ary[i]
    #print(f"{L1=}, {R1=}")
    j = i
    newR = ary[i][1]
    while ary[j][0] <= newR + 1:
      newR = max(newR, ary[j][1])
      j += 1
      if j == leng:
        break
    ret.append((L1, newR))
    #print(ret)
    i = j 
  
  return ret

print(union_section(A))


"""
その2

入力例
Q
L1 R1
L2 R2
......
LQ RQ

5
3 5
8 9
5 8
2 9
6 6
"""

from sortedcontainers import SortedList
Q = int(input())
INF = 10**20
intervals = SortedList([(-INF, -INF), (INF, INF)])

for _ in range(Q):
  L, R = map(int, input().split())
  removed = [] # マージされて消える予定の区間を記録しておく。後で消す。
  # L の入る位置を見つける
  l_idx = intervals.bisect_left((L, -INF)) - 1
  # (L, R) を越えない最大の intervals[l_idx] を求めることにより
  # これにより l_idx, (L, R), l_idx+1 という並びになる。  
  if L <= intervals[l_idx][1] + 1 : # L が l_idx とマージされる場合
    newL = intervals[l_idx][0]
    newR = max(R, intervals[l_idx][1])
    removed.append(l_idx)
  else: # されない場合
    newL, newR = L, R

  # R を右に動かし、入る位置を見つける
  r_idx = l_idx + 1
  while (intervals[r_idx][1] < INF):
    (l, r) = intervals[r_idx]
    if newR < l-1: # newL, newR, l, r の並び順。これ以上右は見なくてよい。
      break
    else:
      # newL, newR, l, r の並び順でくっつく場合、または
      # newL, l, newR, r もしくは newL, l, r, newR の並び順。既存区間とマージして次へ。
      newR = max(newR, r)
      removed.append(r_idx)
      r_idx += 1
  
  # マージされた既存区間を削除する
  for i in reversed(removed): # 後ろから消すことで index のズレを回避
    intervals.pop(i)
  intervals.add((newL, newR))
  print(intervals)



