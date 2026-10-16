# 素因数分解
def prime_factorize(N):
  # 1 から √N までの数を調べていく。
  prime_factors = []
  for i in range(2, N):
    # √N までを調べる。これを2乗で表現する。
    if i * i > N:
      break
    if N % i == 0:
      # N を i で何回割ることができるか
      j = 0
      while(N % i == 0):
        N //= i
        j += 1
      prime_factors.append((i, j))

  # 素数が最後に残ることがありうる
  if N != 1:
    prime_factors.append((N, 1))
  return prime_factors

N = int(input())
prime_factors = prime_factorize(N)
print(prime_factors)






