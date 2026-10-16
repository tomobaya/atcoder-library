# UnionFind 構造。
# 使える関数はシンプルに union, find のみとする。※ groups を追加。これで中身を見られる。
# find はいわゆる root 関数と同じ。
# issame も用意していないがこれは要するに x y の find (root) が同じなら True を返すだけ。

# 段階的に効率化していく様子がコードとともに記された便利なサイト。
# https://note.nkmk.me/python-union-find/

# また、根 parents の中身には -(そのグループの要素数) を格納する。
# これを利用すれば要素数がすぐにわかる。

class UnionFind():
  def __init__(self, n):
    self.parents = [-1 for _ in range(n)]

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
  def groups(self): 
    groups = dict()
    for i in range(len(self.parents)):
      root = self.find(i)
      if root not in groups:
        groups[root] = {i}
      else:
        groups[root].add(i)
    return groups
  
  # 頂点 x が所属するグループのサイズを返す
  def size_of_group(self, x):
    return -self.parents[self.find(x)]


# 使用例。
# 以下は典型 090 の 012 - Red Painting（★4）の解答。
# 入力例
"""
3 3
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3
"""
# 出力例
"""
No
No
Yes
Yes
No
"""


def henkan(i, j):
  # 0 <= i < H, 0 <= j < W を想定
  # これを 0 <= x < H*W に変換する。
  return i * W + j 
  
# H * W のマス目を Union-Find に落とし込む。
H, W = map(int, input().split())
Q = int(input())
uf = UnionFind(H*W) #### まず宣言
color = [["white" for _ in range(W)] for _ in range(H)]
for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    # print("union")
    r, c = query[1] - 1 , query[2] - 1
    color[r][c] = "red"
    for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
      nx, ny = r + dx, c + dy
      if 0 <= nx < H and 0 <= ny < W and color[nx][ny] == "red":
        x = henkan(r, c)
        y = henkan(nx, ny)
        uf.union(x, y) ### Union
  else: # query[0] == 2:
    # print("find")
    ra, ca, rb, cb = query[1] - 1 , query[2] - 1, query[3] - 1 , query[4] - 1
    x = henkan(ra, ca)
    y = henkan(rb, cb)
    root_x = uf.find(x)  ### Find (root)
    root_y = uf.find(y)
    if color[ra][ca] == "red" and color[rb][cb] == "red" and root_x == root_y:
      print("Yes")
    else:
      print("No")