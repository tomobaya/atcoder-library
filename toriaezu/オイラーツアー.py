"""
ABC213-D を参考に。
"""

import sys
sys.setrecursionlimit(10**6)

def euler_tour(v, G):
  seen = [False for _ in range(N+1)]
  result = list()

  def dfs(v):
    # 先に v を見たことを記録する（行きがけ順）。
    seen[v] = True
    result.append(v)
    for neibor in G[v]:
      if not seen[neibor]:
        dfs(neibor)
        result.append(v) # オイラーツアーでは戻るときにも記録する。

  seen[1] = True
  dfs(1)
  return result

from sortedcontainers import SortedSet
"""
N = int(input())
G = [SortedSet() for _ in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().split())
  G[a].add(b)
  G[b].add(a)
"""
N = 4
G = [SortedSet([]), SortedSet([2, 3]), SortedSet([1, 4]), SortedSet([1]), SortedSet([2])]
result = euler_tour(1, G)
print(*result)
