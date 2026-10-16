"""
・関数 enumrate_divisors()
まず素因数分解したものを持っておく。
それを利用して約数の列挙を高速に行う。
それぞれの素因数を掛け合わせて作れる数を全て列挙する。
DFS とバックトラックを活用する。

……コードテストで測ってみたが PyPy 9264 ms, 1,985,280 KB.  遅い。CPython は論外。
SortedSetをやめたら PyPy 4171 ms,メモリ 	979528 KB.
改造したエラトステネスのふるいを利用し、素因数分解の高速化を行ったら 
PyPy 3609ms, 721192KB となった。少しだけマシ程度。
配列の部分切り出しをやめて、配列の何番目を見るという風にしたら
PyPy 3030ms となった。割と速くはなってきた。
が、まだ遅い。
ちなみに 10**6 までの数について、その約数の数の総数を求めたら 13,970,035 となった。
1.4*10**7 なので一応全列挙は間に合うのか。

・関数 enumrate_divisors2()
約数の候補となる数の方からアプローチする手法。
エラトステネスのふるいのように、
  * 2 は 2, 4, 6, 8, ... の約数になる
  * 3 は 3, 6, 9, 12, ... の約数になる
  ......
としていくだけ。これで速くなった。なんと 1433ms, 452,228KB. これでええやん。
"""

# 1 から max_num までの整数について、その約数を列挙する
def enumerate_divisors(max_num): 
  # max_num 以下の素数を得る + ある整数に対しそれを割り切れる最小の素数を記録する
  def eratosthenes(max_num):
    is_prime = [1 for _ in range(max_num + 1)] # 1 なら素数、それ以外なら素数でない
    is_prime[0], is_prime[1] = 0, 0
    for p in range(2, max_num+1): # 合成数を落としていく
      if is_prime[p] != 1: continue # p が既に合成数と判定されていればスキップ
      q = p * 2 # p 以外の p の倍数を落としていく
      while(q <= max_num):
        if is_prime[q] == 1:
          is_prime[q] = p
        else:
          is_prime[q] = min(p, is_prime[q])
        q += p
    return is_prime

  # 整数 num ( <= max_num )を素因数分解する
  is_prime = eratosthenes(max_num)
  #print(is_prime)
  def prime_factorize(num):
    if is_prime[num] == 1:
      return [(num, 1)]
    else:
      prime_factors = []
      for i in range(is_prime[num], num + 1):  
        if i * i > num: # √max_num までを調べる。これを2乗で表現する。
          break
        if num % i == 0: # num を i で何回割ることができるか
          j = 0
          while(num % i == 0):
            num //= i
            j += 1
          prime_factors.append((i, j))

      if num != 1: # 素数が最後に残ることがありうる
        prime_factors.append((num, 1))
      return prime_factors

  prime_factors = [[(0, 0)], [(1, 1)]]
  for i in range(2, max_num + 1):
    prime_factors.append(prime_factorize(i))
  #print(prime_factors)
  
  # 整数 num の約数を列挙する関数 
  divisors = [set() for _ in range(max_num + 1)]
  def enumerate_factors(num):
    def dfs(x, index, prime_factors): # DFSバックトラック 
      if index >= len(prime_factors):
        divisors[num].add(x)
      else:
        [n, multi] = prime_factors[index]
        for m in range(multi + 1):
          x *= n ** m
          dfs(x, index + 1, prime_factors)
          x //= n ** m # バックトラック  
    dfs(1, 0, prime_factors[num])

  for i in range(1, max_num + 1):
    enumerate_factors(i)
  return divisors

#print(enumerate_divisors(10**6))
"""
count = 0
for div in enumerate_divisors(10**6):
  #print(len(div))
  count += len(div)
print(count)
"""


def enumerate_divisors2(max_num):
  divisors = [[1] for _ in range(max_num + 1)]
  for p in range(2, max_num + 1):
    q = p
    while (q <= max_num):
      divisors[q].append(p)
      q += p
  return divisors

div = enumerate_divisors2(10**6)
print(div)
"""
count = 0
for d in div:
  count += len(d)
print(count)

for d in div:
  d.sort()
#print(div)
"""
