"""
# 区間_MEX

## 説明
最小除外数 (MEX : Minimum EXcludant, Minimum EXcluded)
0 以上の整数の集合において、それに含まれない最小の整数をいう。

例:
[0, 1, 2, 3, 5] -> 4
[1, 2, 3] -> 0

オンライン処理を想定している。
つまり、配列が変化するたびに新たに計算し直す。

## 計算量 
現在保持している区間の数を K とするとき、
* mex_num(x) : O(log K)
* insert(x)  : O(log K)
* delete(x)  : O(log K)
* Q回の操作全体では概ね O(Q log Q) 
となる。

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
## ライブラリ本体 + 使用例
"""

from sortedcontainers import SortedList
MEXMAX = 10**9
INF = 10**20
class MEX:
  def __init__(self):
    self.exist_num = SortedList([(-1, -1), (INF+1, INF+1)])

  # 配列 exist_num に存在しない数の内、x 以上で最小のものを求める
  def mex_num(self, x):
    idx = self.exist_num.bisect_right((x, INF)) - 1 # x 以下で最大の l を求める
    [l, r] = self.exist_num[idx]
    if l <= x <= r:
      return r+1
    else:
      return x
    
  # 配列への値の追加（単発）
  def insert(self, x):
    m = self.mex_num(x)
    if m != x:
      print(f"既に {x} は {self.mex_num} の中に存在しています")
      return 
    
    idx = self.exist_num.bisect_right((x, INF)) # x より大きい最小の l を求める
    next = self.exist_num[idx][0]
    prev = next - 1
    if x == self.exist_num[prev][1] + 1 and x == self.exist_num[next][0] - 1: # prev + x + next
      self.exist_num[prev][1] = self.exist_num[next][1]
      self.exist_num.pop(next)
      self.l_list.pop(next)
    elif x == self.exist_num[prev][1] + 1: # prev + x, next
      self.exist_num[prev][1] = x
    elif x == self.exist_num[next][0] - 1: # prev, x + next
      self.exist_num[next][0] = x
      del self.l_list[next]
      self.l_list.add(x)
    else: # prev, x, next
      self.exist_num.add([x, x])
      self.l_list.add(x)

  # MEX 用配列から値を削除する。
  def delete(self, x):
    idx = self.l_list.bisect_right(x) - 1 # x 以下の最大の左を求める。
    [l, r] = self.exist_num[idx]
    if not(l <= x <= r):
      print(f"{x} は配列 MEX に存在していません")
    elif l == x == r:
      self.exist_num.pop(idx)
      self.l_list.remove(x)
    elif l == x:
      self.exist_num.pop(idx)
      self.l_list.remove(l)
      self.exist_num.add([l+1, r])
      self.l_list.add(l+1)
    elif x == r:
      self.exist_num.pop(idx)
      self.exist_num.add([l, r-1])
    else:
      #print(l, r)
      self.exist_num.pop(idx)
      self.exist_num.add([l, x-1])
      self.exist_num.add([x+1, r])
      self.l_list.add(x+1)

  # MEX 用配列に値を範囲で追加する。(l から r まで)
  def insert_section(self, l, r):
    next = self.l_list.bisect_left(r) # r より大きい最小の 左 を求める
    prev = next - 1
    if l <= self.exist_num[prev][1]:
      print("範囲が重複します")
      return

    if l == self.exist_num[prev][1] + 1 and r == self.exist_num[next][0] - 1: # prev + [l, r] + next
      self.exist_num[prev][1] = self.exist_num[next][1]
      self.exist_num.pop(next)
      self.l_list.pop(next)
    elif l == self.exist_num[prev][1] + 1: # prev + [l, r], next
      self.exist_num[prev][1] = r
    elif r == self.exist_num[next][0] - 1: # prev, [l, r] + next
      self.exist_num[next][0] = l
      del self.l_list[next]
      self.l_list.add(l)
    else: # prev, x, next
      self.exist_num.add([l, r])
      self.l_list.add(l)

mex = MEX()
mex.insert(1)
mex.insert(2)
mex.insert(3)
mex.insert(100)
mex.insert(99)
mex.insert(102)
mex.insert(101)
mex.insert_section(10, 14)
mex.insert_section(14, 19)
mex.insert_section(15, 19)
print(mex.exist_num)
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
