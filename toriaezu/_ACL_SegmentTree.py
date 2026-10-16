### セグメント木
# * 長さ N の配列に対し区間の要素の総積を O(logN) で計算できる。積の計算と配列の操作を行う場合に有用。
### 速度比較
#           配列    累積和  フェニック木   セグメント木
# 挿入      O(1)    O(N)    O(logN)       O(logN)  
# 区間和    O(N)    O(1)    O(logN)       O(logN)
#
### 参考資料
# 【データ構造編】ac-Library-pythonを軽くまとめる
# https://qiita.com/Nekoq0o0p/items/6c5970ebb371b8a4979f 
#
### 使い方
# * __init(op, e, v)__  opは演算、eは単位元、v はリスト
# * set(p, x)           p の値を x に更新する。
# * get(p)              p の値を取得する。
# * prod(left, right)   [left, right) に対する op の結果を返す。product (積) の略か。
# * all_prod()          全区間への prod
# * max_right(left, f)  f を満たす区間[left, right) となる right を返す。
#                       f は bool を返す。単位元を入れたら True にならないといけない。
# * max_left(right, f)  f を満たす区間[left, right) となる left を返す。
# すべて 0-index であることに注意。
from atcoder.segtree import SegTree

A = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
#op = max
def op(x, y):
  return max(x ,y)

# 任意の演算を自分で指定して使う場合
e = -1
stree = SegTree(op, e, A)

print(stree.prod(0, 1))
print(stree.prod(1, 2))
print(stree.prod(2, 3))
print(stree.prod(5, 10))


def op2(x, y):
  return x+y
e2 = 0
stree = SegTree(op2, e2, A)
print("op2")
print(stree.prod(0, 1))
print(stree.prod(1, 4))
print(stree.prod(6, 9))
print(stree.prod(3, 10))





# 最大値や最小値を求めるときの使用例
# A の中で13を越えない 1 以上の最大の index + 1 (right) を取得する。
print(stree.max_right(1, lambda x : x < 13))
# lambda x : x > 10 だと単位元 -1 が満たさないのでタメ
# [1, 7) なので 7 が出力される

# A の中で10を越えない 6 未満の最小の index (left) を取得する。
print(stree.min_left(6, lambda x : x < 10))
# [0, 7) なので 0 が出力される
print(stree.min_left(7, lambda x : x < 10))
# [0, 7) なのでこの場合も 0 が出力される
print(stree.min_left(8, lambda x : x < 10))
# [0, 7) だが 8 はこの範囲を超えるので 8 が出力される

