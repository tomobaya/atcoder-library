def Eratosthenes(X):
  # 0からNまでを調べ上げる。素数なら True。
  is_prime = [True] * (X+1)
  # 0, 1 を落とす
  is_prime[0], is_prime[1] = False, False
  # 合成数を落とす
  for p in range(2, X+1):
    # p が既に合成数と判定されていればスキップ
    if not is_prime[p]:
      continue
    # p 以外の p の倍数を落としていく
    q = p * 2
    while(q <= X):
      is_prime[q] = False
      q += p

  return is_prime # 0 から N までが True か False になっている配列を返す
    
N = int(input())
is_prime = Eratosthenes(N)
# print(is_prime) # N=5 なら [False, False, True, True, False, True]

prime_list = []
for i in range(N+1):
  if is_prime[i]:
    prime_list.append(i)
print(prime_list)
