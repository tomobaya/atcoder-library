# ABC349-D や ABC355-E で登場

# divide(1, 5) -> [(1, 1), (2, 3), (4, 5)]
# divide(3, 13) -> [(3, 3), (4, 7), (8, 11), (12, 13)]

# ただし l, r が大きすぎると無理。配列をくっつけるので。
# l, r が大きい場合にも対応するには ABC349-D の解答を参照のこと。

import sys
sys.setrecursionlimit(10**7)

def divide(l, r):
  #print(f"divide({l}, {r})")
  if l > r:
    return []
  if l == r:
    return [(l, r)]

  # r - l 以下の最大の 2**i を求めたい
  m1 = 0
  while (2 ** (m1 + 1) <= r - l + 1):
    m1 += 1

  # r 以上の最小の 2**i を求めたい
  m2 = 0
  while (2 ** m2 < r):
    m2 += 1
  
  for i in range(m1, -1, -1):
    for j in range(2**m2 // (2**i)):
      il, ir = 2**i * j, 2**i * (j+1) - 1
      if l <= il and ir <= r:
        #print(min_il, max_ir)
        return divide(l, il-1) + [(il, ir)] + divide(ir + 1, r)

print(divide(1, 5))
print(divide(3, 13))







