### フェニック木、またの名は Binary Indexed Tree (BIT)
# * セグメント木の機能制限版。
#   * オーダーは同じだが定数倍だけ高速に動作し、メモリも省略できる
#   * あちらは任意の区間和（和以外の演算も）を求められる。こちらは「1 から i 番目までの和」を求められる。
# * 累積和でも同じことができるが、あちらは挿入が遅い。
# * ナイーブな方法（ただの配列でやる）では挿入は速いが累積和は遅い。
### 速度比較
#           配列    累積和  フェニック木   セグメント木
# 挿入      O(1)    O(N)    O(logN)       O(logN)  
# 区間和    O(N)    O(1)    O(logN)       O(logN)
#
### 参考資料
# 【データ構造編】ac-Library-pythonを軽くまとめる
# https://qiita.com/Nekoq0o0p/items/6c5970ebb371b8a4979f 
# 素の配列、累積和、フェニック木（BIT）、いもす法、セグメント木、遅延評価セグメント木、それぞれが得意／不得意な操作について図示
# https://algo-logic.info/binary-indexed-tree/ 
# Binary Indexed Tree (BIT) 総まとめ！区間加算や二次元BITまで
# https://qiita.com/hibit/items/dee03a16c2d82003f6be
#
### 使い方
# * __init__(n)         数列の大きさを定義する。
# * add(p, x)           p の値を x で上書きする。
# * sum(left, right)    [left, right) の合計値を返す
# * _sum(r)             sum(0, r) に同じ。というか sum が _sum を使って実装されている。
# すべて 0-index であることに注意


from atcoder.fenwicktree import FenwickTree

A = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
N = len(A)
ftree = FenwickTree(N)

for i in range(N):
  ftree.add(i, A[i])


print(ftree.sum(1, 3))
print(ftree.sum(5, 10))
print(ftree._sum(12))


### Github よりソースコード
# https://github.com/not522/ac-library-python/blob/master/atcoder/fenwicktree.py
# import typing
# class FenwickTree:
#     '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''
#     def __init__(self, n: int = 0) -> None:
#         self._n = n
#         self.data = [0] * n
# 
#     def add(self, p: int, x: typing.Any) -> None:
#         assert 0 <= p < self._n
# 
#         p += 1
#         while p <= self._n:
#             self.data[p - 1] += x
#             p += p & -p # これは bit演算。一番右にある 1 の桁を抽出する。そして p にそれを足している。
# 
#     def sum(self, left: int, right: int) -> typing.Any:
#         assert 0 <= left <= right <= self._n
# 
#         return self._sum(right) - self._sum(left)
# 
#     def _sum(self, r: int) -> typing.Any:
#         s = 0
#         while r > 0:
#             s += self.data[r - 1]
#             r -= r & -r # これは bit演算。一番右にある 1 の桁を抽出する。そして r からそれを引いて 0 にしている。
# 
#         return s