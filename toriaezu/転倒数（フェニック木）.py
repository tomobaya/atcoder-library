"""
転倒数を求める。

フェニック木（Fenwick tree）または BIT (Binary Indexed Tree) を利用する。
https://tjkendev.github.io/procon-library/python/range_query/bit.html
より
"""

from atcoder import fenwicktree
def inversion_number_of(X): # 必要なら X は座標圧縮しておくこと
  MAX = max(X)
  ft = fenwicktree.FenwickTree(MAX+1)
  inv = 0
  for x in X: # 「x より左にある x より大きな数」の個数を足す
    inv += ft.sum(0,MAX+1) - ft.sum(0,x)
    ft.add(x, 1)
  return inv

#   [1, 2, 3, 4, 5, 6, 7]  
A = [4, 2, 7, 1, 5, 6, 3]
print(inversion_number_of(A))


print(inversion_number_of([0,1,1,3]))
print(inversion_number_of([0,3,2,1]))