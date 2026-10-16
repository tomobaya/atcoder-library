# 常にソート状態が保たれた set や list や dict を作れるデータ構造
# 平衡二分探索木を利用しているらしい。
# https://qiita.com/Shirotsume/items/706742162db68c481c3c
# など参照のこと。
# ソースコードはここ
# https://github.com/grantjenks/python-sortedcontainers/blob/master/src/sortedcontainers/sorteddict.py

from sortedcontainers import SortedSet, SortedList, SortedDict

# 以下、使用例。
print("====== SortedSet() ======")
S = SortedSet([3, 1, 2])
#SortedSet([1, 2, 3]), 初期化の計算量は O(N * logN)
S.add(4)
#SortedSet([1, 2, 3, 4]), add の計算量は O(logN)

print(S)

S.add(3)
#SortedSet([1, 2, 3, 4]), 要素は重複しない
S.discard(4)
#SortedSet([1, 2, 3]), 値4を削除 計算量は O(logN) 存在しない要素をdiscardすると、何も起こらない
#S.remove(100) とやると、KeyErrorが出る
S.pop(2)
#S[2]を削除 S.pop()で最大要素の削除 S.pop(0) で最小要素の削除　全部 O(logN)
S[1]
#2 getは O(logN)
S[0:2]
#0 1 スライスなどもできる　これの計算量は長さを k として O(klogN)
len(S)
#2 現在の要素数 O(1)
S.bisect_left(1)
#1
S.bisect_right(1)
#2
#これらは二分探索。 S.bisect_left(x) で、Sにxを挿入する位置(index)を返す。
#S.bisect_right(x) との違いは、すでにxがSにあるときに左に入れるか右に入れるか
#Pythonのbisectと同じ使用感

# 以上  以下  超過  未満
# left right right left
#      -1          -1

S.index(2)
#1 Sに2が現れる最初の位置を返す。ないとValueError
S.irange(0,2)
#[1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙

print("====== SortedList() ======")
S = SortedList([3, 1, 2, 1])
#SortedList([1, 1, 2, 3]), 初期化の計算量は O(N * logN)
S.add(4)
#SortedList([1, 1, 2, 3, 4]), add の計算量は O(logN)
S.add(3)
#SortedList([1, 1, 2, 3, 3, 4]), 要素は重複する
S.discard(3)
#SortedList([1, 1, 2, 3, 4]), 値3を削除 計算量は O(logN) 要素は1個だけ消される
#S.remove(100) とやると、KeyErrorが出る
S.pop(2)
#S[2]を削除 S.pop()で最大要素の削除 S.pop(0) で最小要素の削除　全部 O(logN)
S[1]
#2 getは O(logN)
S[0:2]
#スライスなどもできる　これの計算量はO(klogN)
len(S)
#現在の要素数 O(1)
S.bisect_left(1)
S.bisect_right(1)
#これらは二分探索。 S.bisect_left(x) で、Sにxを挿入する位置(index)を返す。
#S.bisect_right(x) との違いは、すでにxがSにあるときに左に入れるか右に入れるか
#Pythonのbisectと同じ使用感
#S.index(2) ※これは使えないみたい
#1 Sに2が現れる最初の位置を返す。ないとValueError
S.count(1)
#2 Sに含まれる要素の個数を返す SortedSetにもあるがそっちは使う意味ないので…
S.irange(0,2)
#[1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙

print("====== SortedDict() ======")
S = SortedDict()
S['c'] = 2
S['b'] = 3
S['a'] = 1
#SortedDict({'a': 1, 'b': 3, 'c': 2}) keyの昇順に格納される O(logN)
print(S.index("a"), S.index("b"), S.index("c"))

S.items()
S.keys()
S.values()
del S["a"]
print(S)
S['a'] = 100
#dictと同じものが使える
# S.peekitem() を使うと index を元に key, value を返す。
print("-- peekitem() --")
print(S.peekitem(1))
print(S.peekitem(-1))

# S.pop() で指定された key に対応する value を返し、削除する。
print(S)
print(S.pop("a"))
print(S)
# S.popitem() を使うと index を元に key, value を返し、それらを削除する。
S['a'] = 100
print(S.pop("b"))
print(S)
# Sのうち、keyが最大のものを返す S.pop(i)でi番目 S.pop(0)で最小 全部 O(logN)
# ではなく、pop は key を指定することしかできないみたい。大きさの順番は指定できない。
if 'c' in S:
  print("Yes")
else:
  print("No")
#True

############################################################
# 使用例その2

from sortedcontainers import SortedSet

s = SortedSet([2, 3, 1, 44, 5, 4])
print(s)
#SortedSet([1, 2, 3, 4, 5, 44])　初期化
s.add(10)
print(s)
#SortedSet([1, 2, 3, 4, 5, 44])　addで追加
s.add(2)
print(s)
#SortedSet([1, 2, 3, 4, 5, 10, 44])　重複した要素は１つになる
print(s[0])
#1 s[0]で最も小さいものを選択
print(s[-1]) 
#44 s[-1]で最も小さいものを選択
s.pop()
print(s)
#SortedSet([1, 2, 3, 4, 5, 10]) 一番大きな要素が削除される
print(s.index(2))
#1
print(s.bisect_left(5)) # 二分探索. C++のlower_bound()相当
#4
print(s.bisect_right(5)) # 二分探索. C++のupper_bound()相当
#5
print(list(s.irange(3, 8)))
#[3,4,5] 範囲の値を取り出す
s.remove(4)
print(s)
#SortedSet([1, 2, 3, 5, 10]). 要素を削除する

from sortedcontainers import SortedList

s = SortedList([3, 2, 1, 44, 5, 4])
print(s)
#SortedList([1, 2, 3, 4, 5, 44]) 　初期化
s.add(10)
print(s)
#SortedList([1, 2, 3, 4, 5, 10, 44]) addで追加
s.add(2)
print(s)
#SortedList([1, 2, 2, 3, 4, 5, 10, 44]) 重複した要素もOK
print(s[0])
#1 s[0]で最も小さいものを選択
print(s[-1])
#44 s[-1]で最も小さいものを選択
s.pop()
print(s)
#SortedList([1, 2, 2, 3, 4, 5, 10])  一番大きな要素が削除される
print(s.index(2))
#1
print(s.bisect_left(2)) # 二分探索. C++のlower_bound()相当
#1
print(s.bisect_right(2)) # 二分探索. C++のupper_bound()相当
#3
print(list(s.irange(3, 8)))
#[3,4,5] 範囲の値を取り出す
s.remove(2)
print(s)
#SortedSet([1, 2, 3, 5, 10]) 要素を削除する

from sortedcontainers import SortedDict

s = SortedDict({'d': 10})
print(s)
# SortedDict({'d': 10})
s['b'] = 2
s['e'] = 2
s['a'] = 2
print(s)
# SortedDict({'a': 2, 'b': 2, 'd': 10, 'e': 2})
for e in s.items() : print(e)
#('a', 2)
#('b', 2)
#('d', 10)
#('e', 2)
for e in s.keys() : print(e)
#a
#b
#d
#e
for e in s.values() : print(e)
#2
#2
#10
#2