"""
# ローリングハッシュ

## 説明
文字列比較に有用なアルゴリズムである。
大まかな使いどころとしては、長い文字列の中から特定のキーワードを検索する場面。

長さ N の文字列 S の中に
長さ M の文字列 T があるかどうか検索する問題を考える。

それぞれをハッシュ化しておくことで比較が O(1) で済む。
が、ハッシュ化自体に文字列の長さ分の時間がかかる。

だから、T を 1 字ずつずらしながら S の長さ M の部分文字列と照合する場合
S の部分文字列をハッシュ化 O(M) -> ハッシュ化された T と比較 O(1) する。
これを N-M+1 回、まあ N 回行うので O(NM) の時間がかかってしまう。

しかし、スライディングウィンドウのように差分更新していくことで
S の部分文字列のハッシュ化 N 回を O(M) + O(N) で済ませることができる。

要は 1 回目だけ普通に O(M) でハッシュ化し、あとは差分更新で済ませる。


## 計算量
O(N+M)

## 使われる問題
ABC141-E https://atcoder.jp/contests/abc141/tasks/abc141_e
ABC398-F https://atcoder.jp/contests/abc398/tasks/abc398_f

## 仕組み
ハッシュ化の規則。
BASE （基数）と MOD を用意する。
桁番号を右から順に振る。
各桁 (k = 0, ..., M-1) に対し、その桁の数値に BASE の k 乗を掛ける。
これらを全て足し合わせたものがその文字列のハッシュ。
大きな数字になるので MOD で割った余りをハッシュとする。
故に衝突することもある。

この仕組みを利用すれば差分更新の際、
全体に BASE を掛け 1 桁ずらし、
あとは左端を out, 右端を in すれば O(1) で次が求められる。


#####################################################################
## ライブラリ本体
"""

# ハッシュ化 O(M)
def hash_of(str, base, mod):
  ret = 0
  for s in str: # 差分更新で効率的にハッシュ化
    ret *= base
    ret += ord(s)
    ret %= mod
  return ret

# M 字ごとに切り出して連続でハッシュ化 O(M+N) (Nは str の長さ〉
# 返り値はハッシュ値の配列
def rolling_hash_of(str, m, base, mod):
  if len(str) < m: # 長さが足りない場合
    return []
  hash_S = hash_of(str[:m], base, mod) # 初期値 S[:M] のハッシュ
  rollha = [hash_S] # 部分文字列 S[i:i+M] のハッシュ値 (0-index)
  # 連続で次々にハッシュ値を求めていく（ローリングする）
  base_m = pow(base, m, mod)
  for i in range(len(str) - m):
    next_i = ord(str[i])
    next_im = ord(str[i+m])
    # 全体を1桁ずらし、元の左端の寄与を引き、右端に新しい文字を加える
    hash_S = (hash_S * base - next_i * base_m + next_im) % mod
    rollha.append(hash_S)
  return rollha

## 応用した関数
MOD1 = 998244353
MOD2 = 949999993
BASE1 = 100019
BASE2 = 100013
# 2つのハッシュ値を tuple にし、衝突の可能性を大幅に下げる
def tuple_hash_of(str):
  ret1, ret2 = 0, 0
  for s in str: # 差分更新で効率的にハッシュ化
    ret1 = (ret1 * BASE1 + ord(s)) % MOD1
    ret2 = (ret2 * BASE2 + ord(s)) % MOD2
  return (ret1, ret2)

def rolling_tuple_hash_of(str, m):
  rollha1 = rolling_hash_of(str, m, BASE1, MOD1)
  rollha2 = rolling_hash_of(str, m, BASE2, MOD2)
  rollha_t = []
  for i in range(len(rollha1)):
    rollha_t.append((rollha1[i], rollha2[i]))
  return rollha_t

## 使用例
# 文字列検索
S = "ababcabc"
T = "abc"
M = len(T)
rollha = rolling_tuple_hash_of(S, M) # S の長さ M の部分文字列をすべて tuple を用いてハッシュ化
target = tuple_hash_of(T) # T も同様に tuple ハッシュ化
ans = []
for i in range(len(rollha)):
  if rollha[i] == target:
    ans.append(i)
print(ans)  # [2, 5]

# ABC398-F
# 元の文字列の先頭から始まる部分文字列を順番に列挙し、
# そのハッシュ値を配列 hash に入れて返す関数。
# 元の文字列自体をハッシュ化したものが欲しければ hash[-1] を見ればよい。
def hash_from_head(str, base, mod):
  # 文字列 str は 1-index で考える。1文字目が1。
  # 配列 hash は 0 には 0 を入れ、1 以降は str の添字と一致する。
  n = len(str)
  hash = [0 for _ in range(n+1)]
  for i in range(1, n+1):
    hash[i] = hash[i-1] * base + ord(str[i-1])
    hash[i] %= mod
  return hash[1:]

print(hash_from_head("", BASE1, MOD1))
print(hash_from_head("a", BASE1, MOD1))
print(hash_from_head("ab", BASE1, MOD1))
print(hash_from_head("abc", BASE1, MOD1))


















"""
文字列 S の中に文字列 T が現れるかどうかを高速に検索する。
S の長さを N
T の長さを M 
とする。

T を
S[0:M]
S[1:M+1]
S[2:M+2]
........
と順番に比較していく。
前計算で T のハッシュ値を求めておく。O(M) かかる。
それを利用して連続して S との比較を行っていく。(N) かかる。
"""

MOD = 998244353
BASE1 = 100019
BASE2 = 15

def hash_of(str, base, mod):
  m = len(str)
  ret = 0
  for i in range(m):
    num = ord(str[i])
    ret += num * pow(base, m-1-i, mod)
    ret %= mod
  return ret % mod

def rolling_hash(str_S, str_T, base, mod):
  # T と S[:M] のハッシュ値をまず求める
  hash_T = hash_of(str_T, base, mod)
  hash_S = hash_of(str_S[:M], base, mod)
  # 照合してから順番に次のハッシュ値を求めていく（ローリング）
  match_index = []
  for i in range(N):
    if i + M >= N:
      break
    if hash_T == hash_S:
      match_index.append(i)
    # S の次のハッシュ値を求める。
    next_i = ord(str_S[i])
    next_iM = ord(str_S[i+M])
    hash_S = (hash_S * base - next_i * pow(base, M, mod) + next_iM) % mod
  if hash_T == hash_S:
    match_index.append(i)
  return match_index
  
#########################################################
S = "ossansansaosasnsa"
T = "nsa"
N, M = len(S), len(T)

# ハッシュ値を試しに求める
"""
print("T : ", hash_of(T, BASE1, MOD))
for i in range(len(S)):
  if i+3 <= len(S):
    print(hash_of(S[i:i+M], BASE1, MOD))
print("----")
"""
# ローリングハッシュを実行する。念のため2種類実行して共通するものだけをとる。
matched_1 = rolling_hash(S, T, BASE1, MOD)
matched_2 = rolling_hash(S, T, BASE2, MOD)
set_matched_2 = set(matched_2)
ans = []
for m1 in matched_1:
  if m1 in set_matched_2:
    ans.append(m1)
print(ans)

