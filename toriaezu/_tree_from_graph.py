from collections import deque
# グラフ G が与えられたとき、それを v を根とする木にする関数
def make_tree_from_graph(N, G, v):
  parents = [-1 for _ in range(N+1)]
  parents[v] = 0
  # BFS を用いて 根 v から順に木を作っていく。BFS をする。
  que = deque([v])
  while(que):
    parent = que.popleft()
    for child in G[parent]:
      if parents[child] == -1:
        parents[child] = parent
        que.append(child)
  children = [[] for _ in range(N+1)]
  for i in range(1, N+1):
    children[parents[i]].append(i)
  
  return parents, children

N = 5
G = [[], [2, 4], [1], [4], [3, 5, 1], [4]]
p, c = make_tree_from_graph(N, G, 1)
print(p)
print(c)
