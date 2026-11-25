"""
# 区間_MEX

## 説明
最小除外数 (MEX : Minimum EXcludant, Minimum EXcluded)
0 以上の整数の集合において、それに含まれない最小の整数をいう。
例:
[0, 1, 2, 3, 5] -> 4
[1, 2, 3] -> 0

大まかには範囲を区間で持つ工夫により、数字全てを見なくても区間の個数分だけ見ればよくなる。
それにより二分探索を使うこともできるようになる。
区間union と似たやり方。

オンライン処理を想定している。
つまり、配列が変化するたびに区間情報を更新し、問い合わせ時には二分探索を用いる。

用意するのはクラス MEX.
MEX.exist_num にタプルの配列を持つ。これにより持っている数字を表現する。
関数として
* mex_num ... 与えられた x 以上の数のうち、集合（MEX用配列）に存在しない最小の値を返す
* insert_one ... x を集合に加える
* insert_section ... [L, R] の範囲の数を集合に加える
* delete_one ... x を集合から消す
* delete_section ... [L, R] の範囲の数を集合から消す


## 計算量 
現在保持している区間の数を K とするとき、
* mex_num : O(log K)
* insert_one  : O(log K)
* insert_section : O((m+1) logK) らしい（mは結合対象の区間の個数）
* delete_one  : O(log K)
* delete_section : O((m+1) logK) らしい（mは削除対象の区間の個数）

* Q回の操作全体では概ね O(Q log Q) となる。

## メモリ O(K)


## 使われる問題


## 処理の概要
大まかには範囲を区間で持つ工夫により、数字全てを見なくても区間の個数分だけ見ればよくなる。
それにより二分探索を使うこともできるようになる。
やり方は区間_区間union.py の 2. と同様。

新たな (L, R) について
1.  L の入る位置を二分探索で求める。
2.  右隣を1つずつ順に見ながら R を見比べ、マージしていく。
    既存区間との位置関係によって細かい場合分けがあるが、よく見ていけばかなり単純な条件で分けられる。
    L, R ともにそれぞれ 2 種類の場合分けしかない。
    
これでできた区間を見て、X 以上の最小の MEX を求める際に二分探索を使えばよい。


    
#########################################################
## ライブラリ本体
"""

from sortedcontainers import SortedList
INF = 10**20
class MEX:
  def __init__(self):
    self.exist_num = SortedList([(-2, -2), (INF, INF)]) # 追加される整数が 0 以上 INF - 2 以下という前提

  # 配列 exist_num に存在しない数の内、x 以上で最小のものを求める
  def mex_num(self, x):
    idx = self.exist_num.bisect_right((x, INF)) - 1 # x 以下で最大の l を求める
    (l, r) = self.exist_num[idx]
    if l <= x <= r:
      return r+1
    else:
      return x
    
  # 配列に値を1つ追加する
  def insert_one(self, x):
    if x != self.mex_num(x):
      print(f"既に {x} は存在しています")
      return 
    self.insert_section(x, x)

  # 配列に値を範囲 [L, R] で追加する
  def insert_section(self, L, R):
    # 区間_区間union.py のオンライン処理をそのまま使用
    removed = [] # マージされて消える予定の区間を記録しておく。後で消す。
    # L の入る位置を見つける。左端が L 未満の中で最大の idx を求める。
    idx = self.exist_num.bisect_left((L, -INF)) - 1
    # [idx], (L, R), [idx+1] という並びになる。 
    if L <= self.exist_num[idx][1] + 1 : # L が l_idx とマージされる場合
      L = self.exist_num[idx][0]
      R = max(R, self.exist_num[idx][1])
      removed.append(idx)

    # L が確定したので次は R。1つずつ比べていってマージできる限り右へと伸ばす。
    idx += 1
    while (self.exist_num[idx][1] < INF):
      (yotei_l, yotei_r) = self.exist_num[idx]
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
      self.exist_num.pop(i)
    self.exist_num.add((L, R))
    #print(self.exist_num)

  # 配列から値を1つ削除する
  def delete_one(self, x):
    if x == self.mex_num(x):
      print(f"既に {x} は配列中に存在していません")
      return 
    self.delete_section(x, x)

  # 配列から[L, R]の値を削除する
  def delete_section(self, L, R):
    to_added = set()
    # L 未満の最大の左を求める。
    idx = self.exist_num.bisect_left((L, -INF)) - 1
    (ll, lr) = self.exist_num[idx]
    # idx から左、もしくは idx+1 から右が消える
    if L <= lr: # ll <= L <= lr 
      delete_from = idx
      if ll < L:
        to_added.add((ll, L-1))
    else: # ll <= lr < L
      delete_from = idx + 1

    # R 以下の最大の左を求める。
    idx = self.exist_num.bisect_right((R, INF)) - 1
    (rl, rr) = self.exist_num[idx]
    # idx から左が消える
    delete_to = idx
    if R < rr: # rl <= R < rr
      to_added.add((R+1, rr))
    
    for idx in range(delete_to, delete_from - 1, -1):
      self.exist_num.pop(idx)
    for ta in to_added:
      self.exist_num.add(ta)
    #print(self.exist_num)

"""
  # 配列から値を1つ削除する
  def delete_one(self, x):
    # x 未満の最大の左を求める。
    idx = self.exist_num.bisect_left((x, -INF)) - 1
    [l, r] = self.exist_num[idx]
    if not(l <= x <= r):
      print(f"{x} は集合内に存在していません")
    else:
      # 見つかった区間は削除し、新たな区間を追加する。
      # * 長さ1の区間に一致したら丸ごと削除する
      # * L, R に重なってたら1つ縮める
      # * L と R の間にあるなら新たに2つの区間が追加される
      self.exist_num.pop(idx) 
      if l == x and r != x:
        self.exist_num.add((l+1, r))
      elif l != x and r == x:
        self.exist_num.add((l, r-1))
      else:
        self.exist_num.add((l, x-1))
        self.exist_num.add((x+1, r))
"""

"""
## 使用例
"""
mex = MEX()
mex.insert_one(1)
mex.insert_one(2)
mex.insert_one(3)
mex.insert_one(3)
mex.insert_one(100)
mex.insert_one(99)
mex.insert_one(102)
mex.insert_one(101)
mex.insert_section(10, 14)
mex.insert_section(14, 19)
mex.insert_section(15, 19)
print(mex.exist_num)
mex.delete_one(13)
print(mex.exist_num)
mex.delete_section(11, 17)
print(mex.exist_num)
print("------")
print(mex.mex_num(0))
print(mex.mex_num(1))
print(mex.mex_num(9))
print(mex.mex_num(12))
print(mex.mex_num(14))
print(mex.mex_num(100))
print(mex.mex_num(102))
print(mex.mex_num(104))
print(mex.exist_num)
mex2 = MEX()
mex2.insert_section(1, 10**9)
print(mex2.exist_num)
