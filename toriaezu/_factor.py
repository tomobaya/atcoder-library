# N の約数を列挙する関数
def factor(N):
  # 1 から √N までの数を調べていく。
  factors = []
  for i in range(1, N+1):
    # √N までを調べる。これを2乗で表現する。
    if i * i > N:
      break
    if N % i == 0:
      factors.append(i)
      # i と対になる数字も約数。同じなら除く。
      if N // i != i:
        factors.append(N // i)
  factors.sort()
  return factors           

N = int(input())
factors = factor(N)
print(factors)

