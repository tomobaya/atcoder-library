"""
# フェニック木（Fenwick tree）または BIT (Binary Indexed Tree)

## 説明
仕組みはここを参照
https://qiita.com/AkariLuminous/items/f2f7930e7f67963f0493

大まかなイメージとしては「途中で値を加算できる累積和」。
特に add (x, 1) とすれば「何の値が何個ある」を管理できる。用途はこれが多い。
値域が大きいときには使えないものの、座標圧縮すればOKな問題もある。

この配列に対し
* 挿入（add）
* 区間和（sum）
の2つの操作ができる。
これを応用すると、
add(i, 1) で一つ挿入なら add(i, -1) で一つ削除もできる。

そのほか応用例として
* X 以上／以下／より大／未満 が何個あるかを求める
* l 以上 r 以下の値の合計値を求める
* 転倒数の計算
* 順位 ... 与えられた数値 x が何位であるかがわかる
* k 番目 ... k 番目に小さな値はいくつであるかがわかる（全体数から引けば大きい方もわかる）

「一点加算」+「区間和」ができる。
    * 差分配列を利用すれば「範囲加算」+「一点取得」もできる。
    * min, max, gcd など別の演算を使うならセグメント木（XOR はフェニック木でも扱える）
    * 「区間加算」+「区間和」は遅延評価セグメント木

## 計算量
値域の最大値を N として、add, sum ともに O(log N)
k_th は O((log N)^2)

## 使われる問題
ABC484-E など

## 補足
「範囲加算」+「一点取得」ができるというのはこういうこと。
差分配列（第一項と第二項の差、第二項と第三項の差、......）を用意することにより、
* 1点取得 => 区間和
* 範囲加算 => 2点更新
になる。
そして区間和、2点更新を FenwickTree を用いて行う。これでできるということ。
参考 : AWC0047-C

## 補足2
FenwickTree は途中で中身が変更できる累積和のようなものとみなすことができる。

############################################################
## ライブラリ本体
"""

from atcoder import fenwicktree
# 木の中身を全て出力する
def see(fw, f_max): # f_max は値域の最大値（座標圧縮した場合は圧縮後の最大値）
  for i in range(f_max+1):
    print(fw.sum(i, i+1), end="")
    if i != f_max:
      print(", ", end="")
  print("")

# 木の中身の総合計を求める
def total(fw, f_max):
  return fw.sum(0, f_max+1)

# x 以上／以下／より大／未満 の数が（重複込みで、のべ）何個あるかを求める
def leq(fw, x): # x 以下
  return fw.sum(0, x+1)
def lthan(fw, x): # x 未満
  return fw.sum(0, x)
def geq(fw, x, f_max): # x 以上
  return total(fw, f_max) - fw.sum(0, x)
def gthan(fw, x, f_max): # x より大
  return total(fw, f_max) - fw.sum(0, x+1)

# l 以上 r 以下の値の合計値を求める
def sum_between(fw, l, r):
  return fw.sum(l, r+1)

# 順位にまつわる関数
# (1) 順位（与えられた数値 x が何位であるか）を求める
# （※ 1, 3, 5, 5, 5, 9 のような場合 1位 2位 3位 3位 3位 6位とみなす）
# より正確には x を挿入したときに何位になるのかを返す。存在しない数値が与えられた場合でも答えを返す。
def rank_of(fw, x):
  # x 未満の数を数えてそれに +1 する
  return fw.sum(0, x) + 1

# (2) 小さい方から数えて k 番目の値を求める
# （※ 1, 3, 5, 5, 5, 9 のような場合 1位 2位 3位 4位 5位 6位とみなす）
# これは「自分以下の値が k 個以上あるような数」の中で最小のものと同じ。
# つまり、自身を含めた同じ値の集団が初めて k をまたぐイメージ。
# 先の例なら3は「自分以下が2個」、5は「自分以下が5個」、9は「自分以下が6個」とみなせる。
def k_th_solve(m, fw, k):
  return leq(fw, m) >= k

def k_th(fw, k, f_max): # f_max は値域の最大値（座標圧縮した場合は圧縮後の最大値）
  if k <= 0:
    return -1
  if leq(fw, f_max) < k: # 要素数が足りない場合
    return -1
  ok = f_max
  ng = -1    
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if k_th_solve(mid, fw, k):
      ok = mid
    else:
      ng = mid
  return ok


"""
############################################################
## 使用例
"""
# 0-index 長さ N の Fenwick Tree を構築する
N = 7
ft = fenwicktree.FenwickTree(N) 
# 中身を入れる
A = [4, 2, 7, 1, 5, 6, 3]
for i, a in enumerate(A):
  ft.add(i, a) # ft[i] += a
  # a を 1 にすれば個数のカウントに使えるし、
  # a に具体的な値を入れれば総和を求めるのに使える。
  # 
  # ちなみに、転倒数なら i に値, a に 1 を入れるらしい。

print(ft.sum(1, 4)) # 区間和 [l, r)
ft.add(3, 100) # 加算
# ※ 加算しかできず、「この値に書き換える」操作はできない。
# 別途元々の値を保持した配列 A を持っておき A[i] を引いてから差分だけ足すなどの工夫をする。
print(ft.sum(1, 4)) # 区間和 [l, r)
see(ft, N-1)

######## 応用
# # (1) X 以上／以下／より大／未満 が何個あるかを求める
# (2) l 以上 r 以下の値の合計値を求める
B = [42, 1, 42, 5, 88, 17, 73, 42, 5, 88, 17, 73, 42, 50, 88, 17, 73, 42, 5, 100]
N, M = len(B), max(B)
ft2 = fenwicktree.FenwickTree(M+1) # (1) 用
ft3 = fenwicktree.FenwickTree(M+1) # (2) 用

for b in B:
  ft2.add(b, 1) # 個数を調べたいので1を足すだけ
  ft3.add(b, b) # その値の合計値を求めたいので自分自身を足す

print(leq(ft2, 42))
print(lthan(ft2, 42))
print(geq(ft2, 42, M))
print(gthan(ft2, 42, M))
print(sum_between(ft3, 10, 88))
see(ft2, M)
for k in range(1, N+1):
  print(k, k_th(ft2, k, M), sorted(B)[k-1])



"""
# 実装
# https://github.com/not522/ac-library-python/blob/master/atcoder/fenwicktree.py
# 二分探索はないので注意

class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s
"""