# nCr % MOD を高速で求めるプログラム
import math
MOD = 998244353
MAX = 10 ** 5

# 累乗を求めておく (MOD)
power_list = [1, 1] # 0! = 1 と考える
for i in range(2, MAX+1):
  power_list.append((power_list[-1] * i) % MOD)

# 累乗の逆元を求めておく (MOD)
r_power_list = [1]
for i in range(1, MAX+1):
  r_power_list.append(pow(power_list[i], -1, MOD))


# nCr = n! / (r! * (n-r)!)
# つまり
# nCr = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
# 
# MOD を考えるので、 r! で割るのは r! の逆元を掛けるのに等しくなる。よって
# nCr = n!(MOD) * 逆r!(MOD) * 逆(n-r)!(MOD) となる。
def nCr(n, r):
  if n < 0 or r < 0 or n < r:
    return 0 # 不正な場合
  if r == 0 or r == n:
    return 1
  return (power_list[n] * r_power_list[r] * r_power_list[n - r]) % MOD
  
print(nCr(4, 2))
print(nCr(10, 3))
print(nCr(5, 3))

print(nCr(0, 0))
print(nCr(-1, -1))

"""
# これは旧版。判定順序がまずくて、不正な範囲を弾く方を先にすべきであった。
def nCr(n, r):
  if r == 0 or r == n:
    return 1
  if r < 0 or n < r:
    return 0
  
  return (power_list[n] * r_power_list[r] * r_power_list[n - r]) % MOD
"""