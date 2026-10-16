"""
2N 人の人を N 組のペアに分ける。
パターンを全列挙する。

16人でも計算量は 15*13*11*9*7*5*3*1 = 2,027,025

・2人のときは 1 通り
・4人のとき、1-2 3-4, 1-3 2-4, 1-4 2-3 の 3 通り。
ここで、1 の相方を決めれば残りの組は自動的に決まるというのが公式解説の考え方。
・6人のとき、1 の相方をまず決め、残り 4 人で 2 ペアを作る。
前者は 5 通り、後者は前述の通り 3 通り。計 15 通り。
・8人のとき、1 の相方をまず決め、残り 6 人で 3 ペアを作る。
7 x 15 = 7 x 5 x 3 = 105
・10人のとき 9 x 7 x 5 x 3 = ...
......

関連： ABC236-D
"""

def make_pairings(remain):
  if not remain:
    return [[]]
  res = []
  first = remain[0]
  for i in range(1, len(remain)):
    rem = remain[i]
    other = remain[1:i] + remain[i+1:]
    head = [(first, rem)]
    for tail in make_pairings(other):
      res.append(head + tail)
  return res

all = [i for i in range(1, 13)]
pairs = make_pairings(all)
for pai in pairs:
  print(pai)
