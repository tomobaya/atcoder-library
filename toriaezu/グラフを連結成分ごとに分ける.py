
class UnionFind():
  def __init__(self, n):
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  # これは計算量が重いのでループで毎回使うのには向かない
  def groups(self, n): 
    groups = dict()
    for i in range(1, n):
      root = self.find(i)
      if root not in groups:
        groups[root] = {i}
      else:
        groups[root].add(i)
    return groups


N, M = map(int, input().split())
# まずグラフの頂点と辺を完全に連結成分ごとに分けてしまう。
uf = UnionFind(N+1)
edges = [[0, 0]]
for _ in range(M):
  [u, v] = map(int, input().split())
  uf.union(u, v)
  edges.append([u, v])

group_of_vertexs = [0 for _ in range(N+1)]
group_of_edges = [0 for _ in range(M+1)]
vertexs_per_group = dict()
edges_per_group = dict()
for i in range(1, N+1):
  group_number = uf.find(i)
  group_of_vertexs[i] = group_number
  if group_number not in vertexs_per_group:
    vertexs_per_group[group_number] = [i]
  else:
    vertexs_per_group[group_number].append(i)
for i in range(1, M+1):
  [u, v] = edges[i]
  group_number = group_of_vertexs[u]
  group_of_edges[i] = group_number
  if group_number not in edges_per_group:
    edges_per_group[group_number] = [i]
  else:
    edges_per_group[group_number].append(i)
print(group_of_vertexs)
print(group_of_edges)
print(vertexs_per_group)
print(edges_per_group)

