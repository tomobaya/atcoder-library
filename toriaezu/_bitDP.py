"""
https://qiita.com/karutetto332/items/90fc8186c915afd1e9e8
巡回セールスマン問題のサンプル問題として提示されていたのでこれをやる。
bitDPを使う。

全ての都市を訪れるにあたり、訪れ方の全パターンを探索すると N! 通りになる。
これはいくら N <= 17 という小さな制約でも TLE になる。
ここで、訪れた順番ではなく
これまでにどの都市を訪れたのかがわかっていれば十分なことに気づく。
そこで、訪れた順番に関係なく都市ごとに True/False で管理すれば
2 ** 17 ≒ 1.3 * 10**5 におさまる。

次に訪れる都市との距離を知る必要があるため、
直前に訪れた都市の情報は持っておく必要がある。
だから DP テーブルには
「これまでに訪れた都市の集合」
「直前に訪れた都市」
の 2 つを持たせる。
(2 ** 17) * 17 の配列サイズでいける。

入力例 2 で途中で都市 1 に戻っているのであれ？と思ったが
移動中にたまたまあるだけだった。惑わされてはいけない。

"""

N = int(input())
XYZ = [[0, 0, 0] for _ in range(N+1)]
for i in range(1, N+1):
  x, y, z = map(int, input().split())
  XYZ[i] = [x, y, z]
INF = 10**18
move_cost = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
  a, b, c = XYZ[i]
  for j in range(1, N+1):
    p, q, r = XYZ[j]
    move_cost[i][j] = abs(p - a) + abs(q - b) + max(0, r - c)
#print(move_cost)

# これまでに訪れた都市の集合を bit で管理し、i とする。
# 直前に訪れた都市を j とする。
# そのときの最小コストを DP[i][j] に格納する。
DP = [[INF for _ in range(N+1)] for _ in range(2 ** N)]
DP[1][1] = 0 # 都市 1 には訪問済みなので

# bit パターンと都市の関係（N = 3 として）
# 000(2) = 0(10) = {}
# 001(2) = 1(10) = {1}
# 010(2) = 2(10) = {2}
# 011(2) = 3(10) = {1, 2}
# 100(2) = 4(10) = {3}
# 101(2) = 5(10) = {1, 3}
# 110(2) = 6(10) = {2, 3}
# 111(2) = 7(10) = {1, 2, 3}
# 2進数として見て、右シフトして i 桁目を 1 桁目に移動させてから
# 論理積 & により 1 と比較することで
# 桁ごとに有無が判定できる。
# if (s >> (i-1) & 1) == 1

# ここからよくわからないので解説を見ながら。
# 全ての bit パターンについて、全ての都市間の移動を試す。
# 計算量は (2 ** N) * N * N
for s in range(2 ** N):
  for u in range(1, N+1):
    for v in range(1, N+1):
      # 集合 s を見て、u が訪問済みかつ v が未訪問の場合のみの遷移をチェックする。
      if (s >> (u-1) & 1) == 1 and (s >> (v-1) & 1) == 0:
        # あるなら v に遷移する。集合もいじる。
        ns = s | 1 << (v-1) # 下から v-1 桁目を 1 にする。
        DP[ns][v] = min(DP[ns][v], DP[s][u] + move_cost[u][v])

ans = INF
# 最後に都市 1 に戻らなくてはいけない
for u in range(2, N+1): # 都市 u から都市 1 へ
  ans = min(ans, DP[2**N - 1][u] + move_cost[u][1])
print(ans)



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
N = int(input())
A = [0] + list(map(int, input().split()))

# よくある入力3
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

#################################################
MYP = 1
def myprint(x, end="\n"):
  if MYP == 1:
    print(x, end=end)
##################################################
"""

