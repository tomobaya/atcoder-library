# bisect を使う方法
import bisect
N = 18 # 0-index で考える。配列は長さ N, 添字は 0 - N-1
A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 34, 55, 55, 89, 144, 233, 377, 610, 987]
# bisect_left  : x の挿入位置を返す（x が既にある場合、一番左に入れる）
# bisect_right : x の挿入位置を返す（x が既にある場合、一番右に入れる）
print(bisect.bisect_left(A, 34)) # A[9] == 34 の前に入れるので 8
print(bisect.bisect_right(A, 34)) # A[11] == 55 の前に入れるので 10
print(bisect.bisect_left(A, -1)) # A[0] == 0 の前に入れるので 0

X = 34
# X を越える最小の A[i] を求める
idx = bisect.bisect_right(A, X) # A[10] == 55 の前に入れるので 10
print(f"A[{idx}] = {A[idx]}")
# ※ idx == N （存在しない添字の前に入れる）になる場合、X を越える A[i] は存在しない
# X を越える A[i] の個数
print(N - idx, "個") # 18 - 10 = 8

# X 以上の最小の A[i] を求める
idx = bisect.bisect_left(A, X) # A[8] == 34 の前に入れるので 9。範囲に X を含む分、左にずれる。
print(f"A[{idx}] = {A[idx]}")
# ※ idx == N （存在しない添字の前に入れる）になる場合、X を越える A[i] は存在しない
# X 以上の A[i] の個数
print(N  - idx, "個") # 10

# X を越えない最大の A[i] を求める（X の左端の左の一つ左）
idx = bisect.bisect_left(A, X) - 1 
print(f"A[{idx}] = {A[idx]}")
# idx == -1 になる場合、X を越えない A[i] は存在しない。
# A[-1] の参照が発生しないよう、if 文で別途処理すること。
# その個数
print(idx + 1, "個")
# 例： A[7] == 21, 8個

# X 以下の最大の A[i] を求める（X の右端の右の一つ左）
idx = bisect.bisect_right(A, X) - 1
print(f"A[{idx}] = {A[idx]}")
# idx == -1 になる場合、X 以下の A[i] は存在しない。
# A[-1] の参照が発生しないよう、if 文で別途処理すること。
# その個数
print(idx + 1, "個")
# 例： A[9] == 34, 10個


# めぐる式二分探索
# * ok が答えになる
# * 条件に合う側を ok, その逆を ng に設定すること
# * ok の方にすれば余裕で条件を満たすんだけど、その中でもなるべく ng に近いものを求めたい。

# 例：30を超える最小の A[i] を求める。
def solve(arg, B):
  return (B[arg] >= 100)

B = [0, 5, 8, 13, 22, 25, 58, 88, 90, 100]
ok = len(B)
ng = -1    
while (abs(ok - ng) > 1):
  mid = (ok + ng) // 2
  if solve(mid, B):
    ok = mid
  else:
    ng = mid
print(f"B[{ok}] = {B[ok]}")

"""
# 二分探索について気づいたことを補足
2025/10/08にABC269-Eを解き直してわかった。
二分探索は「条件Xを満たす最小or最大のmidを見つける」仕組みである。
しかしこの問題を見るとどうしても「条件Xを満たす1点を見つける」という目的が先行してしまい、
「最小or最大を見つける」という二分探索の仕組みと結びつかなくなってしまっていた。

この問題の仕様を見て、どうやって「最小or最大を見つける」という二分探索の仕組みに落とし込むか。
それがこの問題、ひいては二分探索の肝である。

"""
"""

# bisect を使えば簡単
import bisect 
C = [0, 5, 8, 13, 22, 25, 58, 88, 90, 100]
# ※ 数字が既存のものと被らない場合は left も right も同じ。被る場合は 1 ずれる。

# 25を超える最小の C[i] を求めるとき
idx = bisect.bisect_right(C, 25)
print(f"C[{idx}] = {C[idx]}")
# idx が C の範囲外になる場合に注意
idx = bisect.bisect_right(C, 1000)
if idx == len(C):
  print(f"そのようなインデックス {idx} は存在しません")


# 25以上で最小の C[i] を求めるとき
idx = bisect.bisect_left(C, 25) 
print(f"C[{idx}] = {C[idx]}")
# idx が C の範囲外になる場合に注意
idx = bisect.bisect_right(C, 1000)
if idx == len(C):
  print(f"そのようなインデックス {idx} は存在しません")


# 25を超えない最大の C[i] を求めるとき
idx = bisect.bisect_left(C, 25) - 1
print(f"C[{idx}] = {C[idx]}")
# idx が C の範囲外になる場合に注意 （-1になるので値自体は出てしまう）
idx = bisect.bisect_left(C, -10) - 1
if idx == -1:
  print(f"そのようなインデックス {idx} は存在しません")


# 25以下で最大の C[i] を求めるとき
idx = bisect.bisect_right(C, 25) - 1
print(f"C[{idx}] = {C[idx]}")
idx = bisect.bisect_left(C, -10) - 1
if idx == -1:
  print(f"そのようなインデックス {idx} は存在しません")


# 以上  以下  超過  未満
# left right right left
#      -1          -1


##################################################################
# めぐる式二分探索テンプレ
# * ok が答えになる
# * 求めたい答えの側（条件に合う側）を ok, その逆を ng に設定すること
# * ok の方にすれば余裕で条件を満たすんだけど、その中でもなるべく ng に近いものを求めたいと考える。

# 30を超える最小の A[i] を求める。
def is_ok(arg):
    return (A[arg] >= 30)

A = [0, 5, 8, 13, 22, 25, 58, 88, 90, 100]
ok = len(A) + 1
ng = -1    
while (abs(ok - ng) > 1):
  mid = (ok + ng) // 2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid
print(ok)
print(A[ok])

# 25を超えない最大の B[i] を求める。
def is_ok(arg):
    return (B[arg] < 25)

B = [0, 5, 8, 13, 22, 25, 58, 88, 90, 100]
ok = -1
ng = len(B) + 1
while (abs(ok - ng) > 1):
  mid = (ok + ng) // 2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid
print(ok)
print(B[ok])

"""