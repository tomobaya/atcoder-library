"""
ローリングハッシュ
"""
MOD1 = 998244353
MOD2 = 1000000007
BASE1 = 100019
BASE2 = 15

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

# 実際に使用する際はこのようにして2つのハッシュ値をタプルにし、衝突の可能性を大幅に下げるとよい。
H = dict()
A = ["abc", "arc", "agc", "abd"]
for str in A:  
  hashs1 = hash_from_head(str, BASE1, MOD1)
  hashs2 = hash_from_head(str, BASE2, MOD2)
  for i in range(len(str)):
    if (hashs1[i], hashs2[i]) not in H:
      H[(hashs1[i], hashs2[i])] = 0
    H[(hashs1[i], hashs2[i])] += 1
print(H)













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

