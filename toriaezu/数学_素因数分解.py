"""
# 数学_素因数分解

## 説明
与えられた整数を素因数分解して返す。
例えば 200 = (2**3) * (5**2) なら [(2, 3), (5, 2)] 

### 使いどころ
* 多数の整数を何度も素因数分解するとき
* 登場する整数の最大値が十分小さいとき(10**6など。 10**7などになるとメモリ制限に注意)
などに使う。

逆に少ない回数しか素因数分解しないのなら O(√N) になる試し割り方式でも十分。
また、最大値が 10**9 など巨大になる場合は使えない。


## 計算量
A を現れる数字の最大値として、
(1) 前処理 O(A log log A)
(2) 分解 O(log A)

## メモリ
spf 配列がサイズ A+1 なので O(A) だが、Python では定数倍が重い。
10**7 ぐらいなら警戒すること。


## 使われる問題
いろいろ

## 処理の概要
1. エラトステネスのふるいを利用し、
   SPF (Smallest Prime Factor) を 1 から N について求めていく。
2. SPF を利用して素因数分解を高速に行う。

* 関数 make_spf(max_num): 最初に指定した max_num までの SPF を求める。
* 関数 prime_factorize(num, spf): max_num 以下の整数 num について素因数分解を行う。

「前計算で 1 から max_num までの全ての整数について素因数分解を行う」とすると、計算がやや重い。
なので、前計算で使うのではなく、問題文中で N 個の整数が登場する（N = 5 * 10**5）とかなら
その都度 prime_factorize 関数を使えばよい。
また、一度使った結果は MEMO 化しておくと効率的。
加えて、make_spf 関数は1度だけ実行するようにしておき、以後使い回すのが大事。

#########################################################
## ライブラリ本体 + 使用例
"""

# 与えられた配列 A に対して max(A) とする方がより効率的ではある
# 10**6 程度なら大丈夫, 10**7 はメモリ制限に注意
#max_num = 10**7 
A = [1, 10, 100, 5, 2, 929292, 999, 1000000]
max_num = max(A)

# SPF (Smallest Prime Factor) を求める関数
def make_spf(max_num):
  spf = [i for i in range(max_num + 1)]
  # エラストテネスのふるいを用いて合成数を落としていく
  for p in range(2, max_num+1):
    if p * p > max_num: break # √max_num までチェックすれば十分
    if spf[p] == p: # p が素数なら、自分より大きな数字について p で割れるかどうかチェックするのに使用する。
      for q in range(p*p, max_num + 1, p): # q = p*p, p*(p+1), ......
        if spf[q] == q: # 素数と判定されているなら p に書き換える。
          spf[q] = p # 初めて割れるようになったものを入れているので、これが最小である。
  return spf

# 整数 num を素因数分解する
def prime_factorize(num, spf):
  pf = []
  while (num > 1): # num == 1 になったら終わる (※ num == 1 なら [] を返す)
    p = spf[num] # 最初に割れるやつで割っていく
    multi = 0
    while (num % p == 0):
      num //= p
      multi += 1
    pf.append((p, multi))
  return pf

## 使用例
spf = make_spf(max_num)
print(prime_factorize(100, spf))
print(prime_factorize(252, spf))
print(prime_factorize(1099, spf))
print(prime_factorize(73, spf))
print(prime_factorize(1, spf)) # [] が返るのは適切な処理、仕様

