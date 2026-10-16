"""
ABC281-E.
sortedList で連続部分列を持ち、1個1個出し入れしていくだけ。
だが結構ややこしい。
"""
from sortedcontainers import SortedList
#N, M, K = map(int, input().split())
#A = [0] + list(map(int, input().split()))
N, M, K = 6, 4, 3
A = [0, 3, 1, 4, 1, 5, 9]

SA = SortedList([])
# 最初の配列を用意する
for i in range(M+1):
  SA.add(A[i])
ans = [0, 0]
for i in range(1, K+1):
  ans[1] += SA[i] # ans[1] には A[1] - A[M] の総和を入れる
print(SA, ans[1]) 

# 1つずつ入れ替えながら進める
for i in range(2, N-M+2):
  #print(f"--- {i=} ---")
  sumK = ans[i-1]
  outA = A[i-1]  # A[1],  A[2],  ... , A[N-M] 
  inA = A[i+M-1] # A[M+1],A[M+2],... , A[N]
  if K == M:
    sumK = sumK - outA + inA
  else:
    # outA が先頭 K 個に入っているなら sumK から引く
    #print(outA, SA[K])
    if outA <= SA[K]:
      sumK -= outA
      sumK += SA[K+1] # 次のやつが代わりに入る
    SA.remove(outA)

    # inA が先頭 K 個に入っているなら sumK に加える
    #print(inA, SA[K])
    if inA <= SA[K]:
      sumK += inA
      sumK -= SA[K] # 今の K 個目が押し出されて出る
    SA.add(inA)
    print(SA, sumK)
  ans.append(sumK)

print(*ans[1:])


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

