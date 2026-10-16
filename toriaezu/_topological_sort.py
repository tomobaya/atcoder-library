# トポロジカルソート
# ・入次数 0 の頂点から順に消していく
# https://atcoder.jp/contests/abc291/tasks/abc291_e
# 1,…,N の並び替えである長さ N の数列 A=(A1​,…,AN​) があります。
# あなたはA を知りませんが、M 個の整数の組 (Xi​,Yi​) について、
# AXi​​<AYi​​ が成り立つことを知っています。
# A を一意に特定できるかどうか判定し、できるなら A を求めてください。

from collections import deque

file = open(__file__ + "\\..\\_topological_input.txt")
N, M = map(int, file.readline().split())
G = [[] for _ in range(N+1)]
# 入次数を管理する配列
# 後述するが、入次数を引いていくだけでよく、グラフ自体をいじる必要はない。
in_degree_of = [0 for _ in range(N+1)] 
for i in range(1, M+1):
  x, y = map(int, file.readline().split())
  if x not in G[y]: # 重複排除のため
    # y -> x と考える。
    G[y].append(x)
    in_degree_of[x] += 1 # というわけで入次数が +1 されるのは x の方
print(G)
print(in_degree_of)

que = deque()
for i in range(1, N+1):
  # シンクになっている頂点（入次数が 0 の点）を探す
  if in_degree_of[i] == 0:
    que.append(i)

flag = True
route = []
while(que):
  if len(que) > 1: # que のサイズが 2 以上になったら一意に定まらなくなる。
    flag = False
    break

  v = que.popleft() # v は入次数 0 の頂点
  route.append(v)
  for neibor in G[v]:
    print(v, " -> ", neibor) # v から neibor に向かってグラフが伸びている。
    in_degree_of[neibor] -= 1 # 入次数を減らしていく。グラフ自体はいじらなくていい。
    # この操作により neibor の入次数が 0 になったら neibor も探索候補になる
    if in_degree_of[neibor] == 0:
      que.append(neibor)  

if flag:
  print("Yes")
  route.reverse()
  route = [-1] + route
  ans = [-1 for _ in range(N+1)]
  for i in range(1, N+1):
    ans[route[i]] = i
  print(*ans[1:])
else:
  print("No")


"""
##################################
MOD = 998244353
##################################
# 再帰の回数を変更する ※再帰関数を使う場合は必ず確認すること
# また、PyPy は再帰が遅いので CPython を使うように！
import sys
sys.setrecursionlimit(10**6)

##################################
# よくある入力1 (整数1つを受け取る)
N = int(input()) 

# よくある入力2
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

# 整数文字列混合のときはいったん文字列で受け取る
string, integer = input().split()

##################################
# 縦横の表
H, W = map(int, input().split())
board = [["" for _ in range(W+1)] for _ in range(H+1)]
for i in range(1, H+1):
  line = input()
  for j in range(1, W+1):
    board[i][j] = line[j-1]
print(board)
##################################
# グラフ
G = [[] for _ in range(N+1)]
for _ in range(1, M+1):
  u, v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)
print(G)
##################################
# ファイルからの入力
file = open(__file__ + "\\..\\input.txt")
N, K = map(int, file.readline().split())
A = [0] + list(map(int, file.readline().split()))
file.close()
# 
file = open(__file__ + "\\..\\input.txt")
N = file.readline().split()
A = [0] * (N+1)
B = [0] * (N+1)
for i in range(1, N+1):
  A[i], B[i] = map(int, file.readline().split())
"""