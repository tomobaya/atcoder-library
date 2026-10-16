"""
2025/03/14
https://algo-logic.info/lca/
の内容を参考に、ChatGPT に作ってもらった。
まだ中身の理解が不十分。

"""

class LCA:
  def __init__(self, G, root=1):
    self.init(G, root)
  
  def init(self, G, root=1):
    # G は 1-indexed で、G[0] はダミー
    V_total = len(G) - 1  # 実際の頂点数
    K = 1
    while (1 << K) < V_total:
      K += 1
    # parent[k][v]:= v の 2^k 先の親。v は 1～V_total の値をとる
    self.parent = [[-1] * (V_total + 1) for _ in range(K)]
    # 根からの距離（1-index: 0 番目は使わない）
    self.dist = [-1] * (V_total + 1)
    self.dfs(G, root, -1, 0)
    for k in range(K - 1):
      for v in range(1, V_total + 1):
        if self.parent[k][v] < 0:
          self.parent[k+1][v] = -1
        else:
          self.parent[k+1][v] = self.parent[k][self.parent[k][v]]
  
  def dfs(self, G, v, p, d):
    self.parent[0][v] = p
    self.dist[v] = d
    for u in G[v]:
      if u != p:
        self.dfs(G, u, v, d + 1)
  
  def query(self, u, v):
    # u の方が深い（または同じ）になるようにする
    if self.dist[u] < self.dist[v]:
      u, v = v, u
    K = len(self.parent)
    diff = self.dist[u] - self.dist[v]
    for k in range(K):
      if (diff >> k) & 1:
        u = self.parent[k][u]
    if u == v:
      return u
    for k in range(K - 1, -1, -1):
      if self.parent[k][u] != self.parent[k][v]:
        u = self.parent[k][u]
        v = self.parent[k][v]
    return self.parent[0][u]

if __name__ == '__main__':
  # 例: 頂点数 7 の木（1-indexed）を構築
  V = 7
  # G[0] はダミー、頂点 1 ～ 7 を使う
  G = [[] for _ in range(V + 1)]
  # 例として、1 を根とし、
  # 辺: (1,2), (1,3), (2,4), (2,5), (3,6), (3,7)
  edges = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6), (3, 7)
  ]
  for u, v in edges:
    G[u].append(v)
    G[v].append(u)
  
  lca = LCA(G, root=1)
  # 例: 頂点 4 と 5 の LCA は 2 になるはず
  print("LCA(4,5):", lca.query(4, 5))
  # 例: 頂点 4 と 6 の LCA は 1 になるはず
  print("LCA(4,6):", lca.query(4, 6))
