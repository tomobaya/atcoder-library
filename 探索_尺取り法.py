"""
# 尺取り法 (Two Pointer Approach)

## 説明
区間に関する条件が単調性を持つ場合に使うことができる。
Lを右に進めたとき、Rが左に戻らないというのも重要。

仕組みとしては以下の通り。
1 <= L <= N, 1 <= R <= N の範囲で全探索すると L <= R を仮定しても
計算量は N*(N+1)//2, つまり O(N^2)
L = 1 に対し R = 1, 2, 3, .....
L = 2 に対し R = 2, 3, 4, .....

これを
L = 1 に対し R = 1, 2, ..., X
L = 2 に対し R = X, X+1, ....
とすることで計算量を概ね 2*N, つまり O(N) に減らす。

計算量削減のポイントは一度右に進んだ R が左には戻らないということ。
それを成立させるために必要な条件は
「L を固定して R を自由に動かすとき、
ある範囲までは条件がずっと成立し、その範囲を出たら条件が成立しない」
こと。成立／不成立は逆でもよい。

### 2 種類の尺取り法
ここが重要。名前を「最大 R」「最小 R」とする。R は配列の要素ではなく区切りを表す。すなわち [L, R)。
* 最大 R ... 条件を満たす最大の R を求める。すなわち、R 以下が True。R より右は False なので見なくてよい。
* 最小 R ... 条件を満たす最小の R を求める。すなわち、R 未満が False。R 以上は True なので見なくてよい。
ただし、ここで処理の際に 1 のズレが生じる。

最大 R : True  True  True  False False
                      ↑ ここを求めたい

最小 R : False False False True  True
                            ↑ ここを求めたい

あくまで欲しいのは「True となる値の端」なので、ずれが生じる。
具体的には「R を +1 したときに条件を満たすかどうか」「今の R で条件を満たすかどうか」
という風に条件のチェックのタイミングが変わってくる。
このテンプレでは両方を扱う。

## 計算量
上記の通り O(N)

## 使われる問題
いっぱい。
二分探索できる問題では尺取り法も使えることが多い。

#####################################################################
# ライブラリ本体 & 使用例
※ ライブラリといっても独立した関数として動くわけではなく、組み方の例になるので
使用例ありきになる。

"""

# 最大 R の例
# ABC032-C を題材にする。 0 が含まれる例外的な場合はこのテンプレでは無視する。
"""
N, K = map(int, input().split())
S = [0 for _ in range(N+1)]
for i in range(1, N+1):
  S[i] = int(input())
"""
N, K = 7, 6 # 1-index
A = [0, 4, 3, 1, 1, 2, 10, 2]
#print(A)

# R 以下が True, R より大が False.
def solve_maxR(value, r, A, K): 
  # 現在の区間 [L, R) に 次の要素 A[R] を追加しても条件を満たすかどうか
  return value * A[r] <= K

# 以下のコードは 1-index. 範囲は [L, R) なので L==R は空である。
# L は 1 - N、R は 1 - N+1 の値をとる（L == N+1 は無意味なので考慮しない）
ans = 0
R = 1
# [条件判定用変数の初期化]
value = 1 
for L in range(1, N+1): 
  #print(f"-- {L=} --")
  # while (R <= N and [Rを用いた条件判定式]):
  while (R <= N and solve_maxR(value, R, A, K)):
    # [R を用いて条件判定用変数の値を変える]
    #print(R)
    value *= A[R]
    R += 1

  # [この問題の答えを数える部分]
  ans = max(ans, R - L)

  if L == R:
    R += 1
  else:
    # [L を用いて条件判定用変数の値を変える]
    value //= A[L]
    
print(ans)

#############################################################################
# 最小 R の例
# ABC485-D
# 最小構成の ABC からなる列を見つけ、そこから拡げていくイメージ。
# すなわち R 未満が False, R 以上が True となる「最小 R」しゃくとり。

# R 未満が False, R 以上が True
def solve_minR(D):
  # 現在の区間 [L, R) が条件を満たすかどうか
  return D["A"] > 0 and D["B"] > 0 and D["C"] > 0


def trim(S): # この問題固有のトリミング処理
  ST = set()
  trim_L = -1
  for i in range(len(S)):
    ST.add(S[i])
    if len(ST) == 3:
      trim_L = i
      break
  ST = set()
  trim_R = -1
  for i in range(len(S)-1, -1, -1):
    ST.add(S[i])
    if len(ST) == 3:
      trim_R = i
      break
  return trim_L, trim_R


N = 20
S = "BCACABCACACABCAACBCA"
N = int(input())
S = input()
trim_L, trim_R = trim(S)
if trim_L == -1 or trim_R == -1:
  print(0)
elif trim_R - trim_L - 1 < 3:
  print(0)
else:
  T = S[trim_L+1 : trim_R]
  M = len(T)
  ans = 0
  R = 0 # 0-index
  D = {"A":0, "B":0, "C":0} # dict の D
  for L in range(M):
    #print(f"-- {L=} --")
    while (R <= M-1 and not solve_minR(D)): # 最小 R の場合はここに not を入れること！
      D[T[R]] += 1
      R += 1
      
    # 上記ループは条件が不成立であっても、R == M となってたら終わる。
    # つまり、最後まで R を進めても答えを求めるための条件を満たせていない場合がある
    # （絶対ではない）
    if solve_minR(D): 
      ans += M - R + 1 # R から M までが True なので

    if L == R:
      R += 1
    else:
      # [L を用いて条件判定用変数の値を変える]
      D[T[L]] -= 1          

  print(ans)

