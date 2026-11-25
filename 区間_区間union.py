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
  
  """
  ### 処理の概要
  ary を見ながら、返り値 ret を作っていく。
  i, j を右へと動かしていく。どちらも左へは戻らない。
  j = i+1 とし、+1 ずつ動かす。マージできる間はマージし続け、できなくなったらそこで終了。
  最後に i = j として、今進んだ分だけ i を一気に加算する。

  最終的に追加される範囲 (L, nextR) について。
  L は固定。なぜなら、追加範囲の左端を nextL とすると、L が居る以上少なくとも L < nextL にはならない。
  じゃあ nextL < L はどうかというと、そうなるような場合は以前の while ループの中で既に飛び越してしまっている。
  なので、L はその時点での配列 ret 内の最大値より必ず 2 以上大きい。よって、新たな追加範囲 nextL は必ず L になる。
  
  変数 nextR は
  L----------R
          L[a]--------R[a]
            L[b]----R[b]
  だったら nextR = R[a] で、
  L-------------------------R
          L[a]--------R[a]
            L[b]----R[b]
  だったら nextR = R
  a まで見た後、b を見て、 b <= nextR + 1 であることを確認してさらに j を伸ばす。
  結果、次のループはその次を L[c] とすると、 i=c から始まることとなる。

  """
  i = 0
  ret = []
  while i <= leng - 1:
    (L, R) = ary[i]
    nextR = R
    #print(f"{L1=}, {R1=}")
    
    j = i + 1 # 比較先を右へと伸ばしていく
    while j < leng and ary[j][0] <= nextR + 1: # 比較先の L が暫定 nextR とくっつくようなら次々伸ばしていく
      nextR = max(nextR, ary[j][1])
      j += 1
    ret.append((L, nextR))
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
  idx = intervals.bisect_left((L, -INF)) - 1
  # (L, R) を越えない最大の intervals[idx] を求めることにより
  # これにより [idx], (L, R), [idx+1] という並びになる。  
  if L <= intervals[idx][1] + 1 : # L が l_idx とマージされる場合
    L = intervals[idx][0]
    R = max(R, intervals[idx][1])
    removed.append(idx)

  # L が確定したので次は R。1つずつ比べていってマージできる限り右へと伸ばす。
  idx += 1
  while (intervals[idx][1] < INF):
    (yotei_l, yotei_r) = intervals[idx]
    if R+1 < yotei_l:
      # L < R < R+1 < yotei_l < yotei_r の並びになる場合、マージされないので R もこれで確定
      break
    else:
      # マージされる場合
      # * L < R < R+1 == yotei_l < yotei_r のとき、マージされて (L, yotei_r)
      # * L < yotei_l <= R < R+1 < yotei_r のとき、マージされて (L, yotei_r)
      # * L < yotei_l < yotei_r < R のとき、マージされて (L, R)
      R = max(R, yotei_r)
      removed.append(idx)
      idx += 1
  
  # マージされた既存区間を削除する
  for i in reversed(removed): # 後ろから消すことで index のズレを回避
    intervals.pop(i)
  intervals.add((L, R))
  print(intervals)

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
"""


