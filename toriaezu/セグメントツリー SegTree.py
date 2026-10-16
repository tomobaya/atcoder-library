"""
# セグメント木
* 長さ N の配列に対し区間の要素の総積を O(logN) で計算できる。積の計算と配列の操作を行う場合に有用。
## 速度比較
          配列    累積和  フェニック木   セグメント木 遅延評価セグメント木
------------------------------------------------------------------------
挿入      O(1)    O(N)    O(logN)       O(logN)     O(logN)  
区間和    O(N)    O(1)    O(logN)       O(logN)     O(logN)  

ただし定数倍の差があり BIT（フェニック木） に比べてセグメント木は 2-3倍、遅延評価セグメント木はさらに 1.5-2倍重い。

## Fenwick 木で済む場合
Fenwick 木は挿入（add）と区間和ができる。応用により
* X 以上／以下／より大／未満 が何個あるかを求める
* l 以上 r 以下の値の合計値を求める
* 転倒数の計算
* 順位 ... 与えられた数値 x が何位であるかがわかる
* k 番目 ... k 番目に大きな値はいくつであるかがわかる
* 「範囲加算」+「一点取得」ができる ⇔ 「一点加算」+「区間和」はセグメント木、「区間加算」+「区間和」は遅延評価セグメント木

などができる。min, max, gcd, xor などは扱えない。

## セグメント木を使う場合
特徴として「一点更新(set)」「区間クエリ(prod)」が使える。
min, max, gcd, xor などを見たらこちらを使う。

## 遅延評価セグメント木を使う場合
セグメント木は「一点更新」だが遅延評価セグメント木は「区間更新」ができる。


## 参考資料
【データ構造編】ac-Library-pythonを軽くまとめる
https://qiita.com/Nekoq0o0p/items/6c5970ebb371b8a4979f 
## 使い方

* __init(op, e, v)__  opは演算、eは単位元、v は 0-index の配列
* set(p, x)           p の値を x に更新する。
* get(p)              p の値を取得する。
* prod(left, right)   [left, right) に対する op の結果を返す。product (積) の略か。
* all_prod()          全区間への prod
* max_right(left, f)  f を満たす区間[left, right) となる right を返す。
                      f は bool を返す。単位元を入れたら True にならないといけない。
* min_left(right, f)  f を満たす区間[left, right) となる left を返す。
すべて 0-index であることに注意。


# 例
## max
どんな x に対しても op(e, x) = x となるような e を選ぶ。
非負整数が格納された配列なら e = -1 としたらよい。

## min 
同様に e = INF とする。

"""

import math
from atcoder.segtree import SegTree
INF = 10**20
A = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# i=[0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11, 12]
print(A)

# 区間内の最大値を求める
# op : max(x, y)
# e  : -INF
st = SegTree(lambda x, y : max(x, y), -INF, A)
print("seg_max")
print(st.prod(0, 1), st.prod(1, 2), st.prod(2, 6), st.prod(5, 10))

# 区間内の最小値を求める
# op : min(x, y)
# e  : INF
st = SegTree(lambda x, y : min(x, y), INF, A)
print("seg_min")
print(st.prod(0, 1), st.prod(1, 2), st.prod(2, 6), st.prod(5, 10))

# 区間内の和を求める
# op : x+y
# e  : 0
st = SegTree(lambda x, y : x+y, 0, A) # 単位元 e = 0
print("seg_plus")
print(st.prod(0, 1), st.prod(1, 2), st.prod(2, 6), st.prod(5, 10))
st.set(5, 1000)
print(st.prod(0, 1), st.prod(1, 2), st.prod(2, 6), st.prod(5, 10))

# 区間内の最大公約数を求める
# op : math.gcd(x, y)
# e  : 0
st = SegTree(lambda x, y : math.gcd(x, y), 0, A)
print("seg_gcd")
print(st.prod(9, 12))
st.set(10, 51)
st.set(11, 68)
print(st.prod(9, 12))

# 区間内の最小公倍数を求める
# op : math.lcm(x, y)
# e  : 1
st = SegTree(lambda x, y : math.lcm(x, y), 1, A)
print("seg_lcm")
print(st.prod(9, 12))
st.set(10, 51)
st.set(11, 68)
print(st.prod(9, 12))

# OR (ビット演算、bitwise)
# op : |
# e  : 0
st = SegTree(lambda x, y : x | y, 0, A)
print("seg_or")
print(st.prod(9, 12))

# AND (ビット演算、bitwise)
# op : &
# e  : 全桁 1
ALL_ONE = (1 << 60) - 1 # 1 が 60個
st = SegTree(lambda x, y : x & y, ALL_ONE, A)
print("seg_and")
print(st.prod(9, 12))

# XOR
# op : ^
# e  : 0
st = SegTree(lambda x, y : x ^ y, 0, A)
print("seg_xor")
print(st.prod(9, 12))


# セグ木上の二分探索（≒尺取法）
# op, e とともに f を定義する必要あり
#A= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# i=[0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11, 12]
st = SegTree(lambda x, y : x+y, 0, A) # 再度加算で st を定義
print("max_right, min_left")
# A[1] からスタートして区間和が13未満になる最大区間の右端のindexを求める
print(st.max_right(1, lambda x : x < 13)) # [1, 6) なので 6 が出力される
# A[11] からスタートして区間和が130以下になる最大区間の左端のindexを求める
print(st.min_left(11, lambda x : x <= 130)) # [7, 11) なので 7 が出力される

