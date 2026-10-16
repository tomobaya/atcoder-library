"""
・0, 1 を並べた配列を作る関数

0 と 1 が合わせて n 個あり、そのうち 0 が r 個ある。
この関数はそのような長さ n の配列のパターンを全て列挙する。
以下、0 を a 個、 1 を b 個とする。
"""
def line_a_and_b(a, b, total, now):
  if a == b == 0:
    total.append(now)
  else:
    ret = []
    if a > 0:
      line_a_and_b(a - 1, b, total, now + [0])
    if b > 0:
      line_a_and_b(a, b - 1, total, now + [1])
    return total

a, b = 4, 2
patterns = line_a_and_b(a, b, [], [])
for pat in patterns:
  print(pat)

################################################################
"""
a 個のアメを b 人に配る全パターンを列挙する。
1 人に複数個配ることもあり、貰わない人が居ても構わない。
"""
import sys
sys.setrecursionlimit(10**7)

def give_a_to_b(remain_candy, remain_person, patterns, now):
  if remain_candy == 0 or remain_person == 0:
    for i in range(remain_person):
      now += [0]
    patterns.append(now)
  else:
    for i in range(remain_candy + 1):
      give_a_to_b(remain_candy - i, remain_person - 1, patterns, now + [i])
    return patterns

a, b = 2, 3
patterns = give_a_to_b(a, b, [], [])
for pat in patterns:
  print(pat)
