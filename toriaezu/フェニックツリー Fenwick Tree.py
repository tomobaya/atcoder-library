"""
フェニック木（Fenwick tree）または BIT (Binary Indexed Tree)
解説
https://qiita.com/AkariLuminous/items/f2f7930e7f67963f0493

## Fenwick 木で済む場合
Fenwick 木は挿入（add）と区間和ができる。応用により
* X 以上／以下／より大／未満 が何個あるかを求める
* l 以上 r 以下の値の合計値を求める
* 転倒数の計算
* 順位 ... 与えられた数値 x が何位であるかがわかる
* k 番目 ... k 番目に大きな値はいくつであるかがわかる
* 「範囲加算」+「一点取得」ができる ⇔ 「一点加算」+「区間和」はセグメント木、「区間加算」+「区間和」は遅延評価セグメント木

などができる。min, max, gcd, xor などは扱えない。

補足 : 「範囲加算」+「一点取得」ができるというのはこういうこと。
差分配列を用意することにより、
* 1点取得 => 区間和
* 範囲加算 => 2点更新
になる。
そして区間和、2点更新を FenwickTree を用いて行う。これでできるということ。
参考 : AWC0047-C

補足2 :
FenwickTree は途中で中身が変更できる累積和のようなもの。

"""

from atcoder import fenwicktree
# 添字 x 以下の値の総和 # 使用例: X 以下の値が何個あるか（add(x, 1) とした場合）
def leq(fw, x): 
  return fw.sum(0, x+1)

def lthan(fw, x): # 同じく x 未満
  return fw.sum(0, x)

def geq(total, fw, x): # 同じく x 以上（total にはその時点で fw に入っている値の合計を入れる）
  return total - fw.sum(0, x)

def gthan(total, fw, x): # 同じく x より大（total にはその時点で fw に入っている値の合計を入れる）
  return total - fw.sum(0, x+1)

def sum_between(fw, l, r): # 同じく l 以上 r 以下の総和
  return fw.sum(l, r+1)


# 0-index 長さ N の Fenwick Tree を構築する
N = 7
ft = fenwicktree.FenwickTree(N) 

A = [4, 2, 7, 1, 5, 6, 3]
for i, a in enumerate(A):
  ft.add(i, a) # ft[i] += a
  # a を 1 にすれば個数のカウントに使えるし、
  # a に具体的な値を入れれば総和を求めるのに使える。

  # 転倒数なら i に値, a に 1 を入れるらしい

# 加算と累積和（を利用した区間和）が O(logN) で可能
print(ft.sum(1, 4)) # 区間和 [l, r)
ft.add(3, 100) # 加算
# ※ 加算しかできず、「この値に書き換える」操作はできない。
# 別途元々の値を保持した配列 A を持っておき A[i] を引いてから差分だけ足すなどの工夫をする。
print(ft.sum(1, 4)) # 区間和

# 一応こうすれば木の中身が全部見られる
for i in range(N):
  print(ft.sum(i, i+1), end=", ")
print("")

######## 応用
# (1) X 以上／以下／より大／未満 が何個あるかを求める
# (2) l 以上 r 以下の値の合計値を求める
# 
# 「何の数字が何個あるか」を Fenwick Tree の要素にする。
# 値域分の配列を作る必要があるので 10**9 とかになる場合には使えない。

B = [42, 1, 42, 5, 88, 17, 73, 42, 5, 88, 17, 73, 42, 50, 88, 17, 73, 42, 5, 100]
N, M = len(B), max(B)
ft2 = fenwicktree.FenwickTree(M+1) # (1) 用
ft3 = fenwicktree.FenwickTree(M+1) # (2) 用

for b in B:
  ft2.add(b, 1) # 個数を調べたいので1を足すだけ
  ft3.add(b, b) # その値の合計値を求めたいので自分自身を足す

print(leq(ft2, 42))
print(lthan(ft2, 42))
print(geq(N, ft2, 42))
print(gthan(N, ft2, 42))
print(sum_between(ft3, 10, 88))



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