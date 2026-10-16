"""
単調deque

範囲内の最大値を常に確認できるようにする方法。
SortedListでもいけるが、こちらの方が簡単。

deque を用意し、この中身に index を入れていく。
必然的に index は昇順に入る。
そして、その中身（A[i]）については常に降順が保たれるようにする。
そうなるように、入れるたびに判定を行って余計な小さい奴があれば pop していく。

範囲を左から縮めるときは、縮める index が deque の左端に入っていれば
そのときだけ popleft() する。
"""


from collections import deque
N = 5
A = [0, 1, 4, 2, 5, 3] # 1-index

Dmax = deque()
# 拡げる
print("範囲を拡げていく")
for i in range(1, N+1):
  while (Dmax and A[Dmax[-1]] < A[i]):
    Dmax.pop() # 同じなら入れるが、大きければ排除していく
  Dmax.append(i)
  print(Dmax, "\n最大値 : ", A[Dmax[0]])

# 縮める
print("今度は縮める")
for i in range(1, N+1):
  if len(Dmax) == 0:
    continue
  
  if Dmax[0] == i:
    Dmax.popleft()

  if len(Dmax) == 0:
    continue
  print(Dmax, "\n最大値 : ", A[Dmax[0]])



