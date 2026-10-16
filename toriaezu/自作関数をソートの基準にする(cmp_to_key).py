from functools import cmp_to_key
# cmp_to_key は正の値を受け取ったとき、入れ替えるべきだと判定する。

# 昇順ソート
def mysort1(x, y):
  # 2 つの要素が x, y の順に与えられる。
  # x > y ならば正の値を返して入れ替える。
  # x <= y ならば 0 以下の値を返してそのままの順序にする。
  return x - y


N = 3
A = [0, 1, 3, 2]
B = [0, 3, 1, 2]

# 昇順ソート
A.sort(key=cmp_to_key(mysort1))
print(A)
# 降順ソート
B.sort(key=cmp_to_key(mysort1), reverse=True)
print(B)


"""
ABC307-C より。
A[i] / (A[i]+B[i]) をソートの基準にする。
"""

from functools import cmp_to_key

N = 3
A = [0, 1, 3, 2]
B = [0, 3, 1, 2]

AB = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(1, N+1):
  AB[i] = [i, A[i], B[i]]
print(AB)

# A[i] / (A[i]+B[i]) を基準にして X, Y を並び替える。
def mysort(X, Y):
  Ai, Bi = X[1], X[2]
  Aj, Bj = Y[1], Y[2]
  # A[i] / (A[i]+B[i]) と A[j] / (A[j]+B[j]) の比較
  # 左辺が大きければ正、右辺が大きければ負、等しければ 0 を返す。
  # ※ この問題では大きい順に結果が欲しいので、この正負も逆に考えて
  # 右辺 - 左辺を判定に使用する。
  return Aj * (Ai+Bi) - Ai * (Aj+Bj) # 式変形して

# cmp_to_key はどうやら正の値を受け取ったら入れ替えるべきと判断するようだ。
AB.sort(key=cmp_to_key(mysort)) 
#print(AB)
for i in range(1, N+1):
  print(AB[i][0], end=" ")
print("")
