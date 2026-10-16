"""
https://atcoder.jp/contests/awc0053/tasks/awc0053_d

* クエリ逆読みで埋めていく
* 一度確定したマスは二度と触らない、そこを上手にスキップするのがこの問題の肝。
"""

# 再帰用の記述を忘れず、また CPython を使うこと
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
nxt = [i for i in range(N+2)] # i 以上で最も小さい未確定マスの番号
# ※ N+1 という範囲外の値を用意することで、 while x <= R[i]: の停止条件を満たせるようにする。
color = [0 for _ in range(M+1)] # 何番目に塗られる色が何色かを格納する
L = [0 for _ in range(M+1)]
R = [0 for _ in range(M+1)]
for i in range(1, M+1):
  l, r, c = map(int, input().split())
  L[i] = l
  R[i] = r
  color[i] = c

# ここが処理の肝
def find(x): # x 以降（xも含む）で最小の未確定マスを見つける関数
  if nxt[x] == x: return x # x 自身が該当するなら未確定マスなので return
  nxt[x] = find(nxt[x]) # 再帰
  return nxt[x]

ans = [0 for _ in range(N+1)]
for i in range(M, 0, -1):
  # L[i] から R[i] を color[i] で塗る。スキップすべきマスはスキップする。
  x = find(L[i])
  while (x <= R[i] and x <= N):
    ans[x] = color[i]
    nxt[x] = find(x+1) # x が確定したから次からは x+1 (の先)を見てもらうようにする。
    # この +1 で N の外に出るから処理が終了できる。nxt を 0-N+1 まで用意したおかげ。
    x = find(x) # 次の未確定位置へ飛ぶ
  #print(i, ans)

print(*ans[1:])

  

"""
map(int, input().split())
list(map(int, input().split()))
##################################
MOD = 998244353
##################################
# 再帰の回数を変更する ※再帰関数を使う場合は必ず確認すること
# また、PyPy は再帰が遅いので CPython を使うように！
import sys
sys.setrecursionlimit(10**7)

##################################
# よくある入力1
N = int(input())
A = [0] + list(map(int, input().split()))

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

# 表の出力（i, j が 0 のときを除去して見やすくした）
for i in range(1, H+1):
  for j in range(1, W+1):
    print(board[i][j], end=" ")
  print("")

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

##################################
AND &
OR  |
XOR ^
##################################
# BFS テンプレ
from collections import deque
N = int(input())
G = [[] for _ in range(N+1)]
for i in range(1, N+1):
  a, b = map(int, input().split())
  G[a].append(i)
  G[b].append(i)

que = deque([])
seen = [False for _ in range(N+1)]
seen[1] = True

while(que):
  v = que.popleft()
  for v2 in G[v]:
    if seen[v2]: continue
    seen[v2] = True
    que.append(v2)
print(seen)
"""
