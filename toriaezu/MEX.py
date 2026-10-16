# minimum excludant (minimum excluded).
# 0 以上の整数の集合において、それに含まれない最小の整数

# 範囲を区間で持つ方法。区間の個数によって計算量が決まる。
from sortedcontainers import SortedList
MEXMAX = 10**9
class MEX:
  def __init__(self):
    self.exist_num = SortedList([[0, 0], [MEXMAX+1, MEXMAX+1]]) # 番兵を入れておく
    self.l_list = SortedList([0, MEXMAX+1])

  # X 以上で exist_num に存在しない数を求める。
  def mex_num(self, x):
    idx = self.l_list.bisect_right(x) - 1 # x 以下で最大の l を求める
    [l, r] = self.exist_num[idx]
    if l <= x <= r:
      return r+1
    else:
      return x
  # MEX 用配列に値を追加する。
  def insert(self, x):
    m = self.mex_num(x)
    if m != x:
      print(f"既に {x} は {self.mex_num} の中に存在しています")
      return 
    
    next = self.l_list.bisect_left(x) # x より大きい最小の 左 を求める
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

"""
# N が 10**9 とかだとこの方法はダメ
def mex(exist_set): # MEX を求める。N+1 が返ってきたら 0-N が全て埋まっていることになる。
  N = len(exist_set)
  for i in range(N+2):
    if i not in exist_set:
      return i
    
A = {0, 1, 2, 3}
print(mex(A))
B = {0, 1, 3, 6}
print(mex(B))
C = {0, 1, 2, 3, 4, 5, 6, 7, 90, 1000}
print(mex(C))
D = {100}
print(mex(D))
print("--")

# 範囲を区間で持つ方法。区間の個数によって計算量が決まる。
from sortedcontainers import SortedList
INF = 10**9
# X 以上で exist_num に存在しない数を求める。
def mex_using_section(exist_num, l_list, x):
  idx = l_list.bisect_right(x) - 1 # x 以下で最大の l を求める
  [l, r] = exist_num[idx]
  #print(f"{l=}, {x=}, {r=}")
  if l <= x <= r:
    return r+1
  else:
    return x
# MEX 用配列へ値を追加する。
def insert_into_mex(exist_num, l_list, x):
  m = mex_using_section(exist_num, l_list, x)
  if m != x:
    print(f"既に {x} は {exist_num} の中に存在しています")
    return 
  
  next = l_list.bisect_left(x) # x より大きい最小の l を求める
  prev = next - 1
  if x == exist_num[prev][1] + 1 and x == exist_num[next][0] - 1: # prev + x + next
    exist_num[prev][1] = exist_num[next][1]
    exist_num.pop(next)
    l_list.pop(next)
  elif x == exist_num[prev][1] + 1: # prev + x, next
    exist_num[prev][1] = x
  elif x == exist_num[next][0] - 1: # prev, x + next
    exist_num[next][0] = x
    del l_list[next]
    l_list.add(x)
  else: # prev, x, next
    exist_num.add([x, x])
    l_list.add(x)

  

# 既に存在している数を配列 A に入れる。
A = SortedList([[0, 0], [2, 5], [10, 20], [INF+1, INF+1]]) # 番兵を入れておく
L = SortedList()
for a in A:
  L.add(a[0])
for i in [0, 1, 3, 4, 5, 6, 9, 10, 11, 20, 22]:
  print(i, mex_using_section(A, L, i))

insert_into_mex(A, L, 100)
insert_into_mex(A, L, 101)
insert_into_mex(A, L, 99)
print(A, L)
"""