"""
AWC0030-D
https://atcoder.jp/contests/awc0030/tasks/awc0030_d

T はそのまま Funcional Graph を表している。
頂点を 1 つずつ選び、not seen ならそこから辿っていく。
履歴を持っておいてループを検出し、ループサイズを計算する。

この問題では各成分ごとに、自分の所属するグループにおいて
1つ存在している閉路のサイズを答えなくてはいけない。
というわけで、ループサイズが確定した点（ループ内の点）から
逆向きに BFS で辿ることで全ての点について答えとなる値を埋めていっている。

"""

N = int(input())
T = [0] + list(map(int, input().split()))
rT = [[] for _ in range(N+1)]
for i in range(1, N+1):
  rT[T[i]].append(i)
# 1 から順に頂点を選んでいって次々と辿る。
seen = [False for _ in range(N+1)]
loop_sizes = [0 for _ in range(N+1)]
for v in range(1, N+1):
  if seen[v]:
    continue
  # 履歴を用意してそこと被ったら終了。ループがあるので記録する。
  # 履歴にないけど next が seen だったらそれも終了。
  # これは記録しないで破棄してよい。
  #print(f"{v=}")
  seen[v] = True
  count = 1
  results = {v: count}
  exit_flag = False
  while (T[v] not in results):
    count += 1
    results[T[v]] = count

    if seen[T[v]]:
      exit_flag = True
      break
    else:
      v = T[v]
      seen[v] = True
  if exit_flag:
    continue
  else: # 最後に訪れたところがループの終端になる
    loop_size = results[v] - results[T[v]] + 1
    #print(loop_size)
    """
    # ループサイズのみなら ↑ だけでよいが、ループの所属する点を挙げると次のようになる
    loops = set()
    for key, value in results.items():
      loop_sizes[key] = loop_size
      if results[T[v]] <= value <= results[v]:
        loops.add(key)
    #print(loops)
    """

# 逆向きに辿って全ての点の loop_sizes[v] を埋める
from collections import deque
for v in range(1, N+1):
  if loop_sizes[v] == 0:
    continue

  que = deque([v])
  while (que):
    q = que.popleft()
    for q2 in rT[q]:
      if loop_sizes[q2] == 0:
        loop_sizes[q2] = loop_sizes[q]
        que.append(q2)

print(*loop_sizes[1:])

"""
for start in starts:
  seen = [False for _ in range(N+1)]
  seen[start] = True
  count = 0
  v = start
  results = {v: count}
  while (not seen[T[v]]):
    seen[v] = True
    v = T[v]
    count += 1
    results[v] = count
  #print(results)
  loop_start = T[v]
  loop_start_count = results[T[v]]
  #print(loop_start, loop_start_count)

  loop_size = count - loop_start_count + 1
  #print(loop_size)

  for k, v in results.items():
    #if v < loop_start_count: # ループ外は count - 自分の番号
    #  ans[k] = count - v
    #else:
    ans[k] = loop_size
      
# ここまで見たところで、ループ外の点が存在しないやつについては検出できていないことに気づく。
# あとは UF でよい。
uf = UnionFind(N+1)
for i in range(1, N+1):
  uf.union(i, T[i])

for i in range(1, N+1):
  if ans[i] == -1:
    ans[i] = uf.size_of_group(i)

print(*ans[1:])
"""


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
