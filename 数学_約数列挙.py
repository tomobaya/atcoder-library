"""
# 約数列挙

## 説明
関数 yakusuu : 引数として与えられた整数の約数を全て列挙する。
関数 yakusuu_all : 1 から引数として与えられた整数までの約数を全て列挙する。


## 計算量
yakusuu O(√N)
yakusuu_all O(N logN)
10**6 までの数について、その約数の数の総数を求めたら 13,970,034 となった。
1.4*10**7 と考えると全列挙は一応間に合う。
参考までに 1433ms, 452,228KB. 

## 仕組み
約数の候補となる数の方からアプローチする。
エラトステネスのふるいのように、
  * 2 は 2, 4, 6, 8, ... の約数になる
  * 3 は 3, 6, 9, 12, ... の約数になる
  ......
としていくだけ。

#################################################################
## ライブラリ + 使用例
"""

def yakusuu(num):
  if num == 0:
    return []
  small = []
  large = []
  for p in range(1, num+1):
    if p * p > num:
      break
    if num % p == 0:
      sm = p
      la = num // p
      small.append(sm)
      if sm != la:
        large.append(la)
  return small + large[::-1]

y = yakusuu(100)
print(y)
y = yakusuu(180)
print(y)


def yakusuu_all(max_num):
  divisors = [[1] for _ in range(max_num + 1)]
  for p in range(2, max_num + 1):
    q = p
    while (q <= max_num):
      divisors[q].append(p)
      q += p
  divisors[0] = []
  return divisors

div = yakusuu_all(10)
for i, d in enumerate(div):
  print(i, d)

"""
div = yakusuu_all(10**6)
for i, d in enumerate(div):
  print(i, d)
"""

"""
# 約数の個数を数える
count = 0
for d in div:
  count += len(d)
print(count)
print(div)
"""
