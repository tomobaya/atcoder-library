"""
1次元配列
"""
import random

N = 10 # 個数
M, m = 9, 1 # 最大値, 最小値
A = []
for i in range(N):
  A.append(random.randint(m, M))
print(N)
print(*A)

"""
重複なしの1次元配列
"""
N = 9 # 個数
A = [i for i in range(1, N+1)]
random.shuffle(A)
print(N)
print(*A)




