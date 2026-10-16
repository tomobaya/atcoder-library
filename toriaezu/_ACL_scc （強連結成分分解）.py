### SCC (strongly connected component)
# https://atcoder.jp/contests/practice2/tasks/practice2_g 
# 練習問題
# 入力例
"""
6 7
1 4
5 2
3 0
5 5
4 1
0 3
4 2
"""
from atcoder.scc import SCCGraph

edges = [[1, 4], [5, 2], [3, 6], [5, 5], [4, 1], [6, 3], [4, 2]]
N, M = 6, 7
SG = SCCGraph(N+1) # N+1 個の頂点を用意する
for i in range(M):
  [u, v] = edges[i]
  SG.add_edge(u, v) # 辺を追加する
print(SG)
print(SG.scc()) # それぞれの強連結成分の中身リストと、それがトポロジカルソートされたもの
  

"""
N, M = map(int, input().split())
graph = SCCGraph(N) # 1-index の場合は N+1 にすること
for _ in range(M):
    a, b = map(int, input().split())
    graph.add_edge(a, b)
print(graph) # これは SCCGraph object として出力され、中身は見られない

groups = graph.scc()
print(len(groups)) # いくつのグループに分解されるか
for group in groups: 
    print(len(group), *group) # それぞれのグループに所属する頂点の数と、そこに所属する頂点の一覧
"""