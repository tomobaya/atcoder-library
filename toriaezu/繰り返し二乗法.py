# ものすごい回数の N 乗をして MOD で割るやつは繰り返し二乗法を使う。
# なお pow() 関数はこれを内部で使っている。

# x の 1乗、2乗、4乗、8乗、……を計算しておく。
# x の N 乗はこれらの積で表せる。(N を 2 進数に変換してやればいい)

#N, K = map(int, input().split())
N, K = 2021, 617
MOD = 10 ** 9 + 7

if N == 1:
  print(K)
elif N == 2:
  print(K * (K-1))
else:
  ans = K * (K-1)
  N -= 2
  X = K-2
  while (N > 0):
    if N % 2 == 1: # 2 進数で表したときに 1 となる桁のときだけ X をかけてやる
      ans = ans * X % MOD
    X = X * X % MOD # X は 1, 2, 4, 8乗, ... と増大していく
    N //= 2
  print(ans)