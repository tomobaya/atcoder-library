# 二次元累積和

N = 3
B = [[0, 0, 0, 0], [0, 1,2,3], [0, 3,5,7], [0, 10, 8, 4]]
cum_B = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 先に横に足していく
for i in range(1, N+1):
  for j in range(1, N+1):
    cum_B[i][j] = cum_B[i][j-1] + B[i][j]
# 次に縦に足していく
for i in range(1, N+1):
  for j in range(1, N+1):
    cum_B[i][j] = cum_B[i][j] + cum_B[i-1][j]


## 出力
for i in range(1, N+1):
  for j in range(1, N+1):
    print(B[i][j], end=" ")
  print("")
print("")

for i in range(1, N+1):
  for j in range(1, N+1):
    print(cum_B[i][j], end=" ")
  print("")
print("")

## 区間和を求める
## (x1, y1) から (x2, y2)
# a = cum_B[x2][y2] - cum_B[x1-1][y2] - cum_B[x2][y1-1] + cum_B[x1-1][y1-1]


## (1, 1) から (2, 2)
a = cum_B[2][2] - cum_B[0][2] - cum_B[2][0] + cum_B[0][0]
print(a)
## (2, 2) から (3, 3)
a = cum_B[3][3] - cum_B[1][3] - cum_B[3][1] + cum_B[1][1]
print(a)

## (2, 1) から (3, 2)
a = cum_B[3][2] - cum_B[1][2] - cum_B[3][0] + cum_B[1][0]
print(a)





# よくある入力1 (整数1つを受け取る)
# N = int(input())
# 
# よくある入力2
# N, K = map(int, input().split())
# A = [0] + list(map(int, input().split()))
# 
# 整数文字列混合のときはいったん文字列で受け取る
# string, integer = input().split()
#
# ファイルからの場合
# file = open(__file__ + "\\..\\input.txt")
# N, K = map(int, file.readline().split())
# A = [0] + list(map(int, file.readline().split()))
# file.close()
#  
# 複数行の入力
# A = [0] * (N+1)
# B = [0] * (N+1)
# for i in range(1, N+1):
#   A[i], B[i] = map(int, input().split())
# 
# ファイルからの場合
# file = open(__file__ + "\\..\\input.txt")
# N = file.readline().split()
# A = [0] * (N+1)
# B = [0] * (N+1)
# for i in range(1, N+1):
#   A[i], B[i] = map(int, file.readline().split())

# こちらが高速らしい
# import sys
# readline = sys.stdin.readline
# uv = [list(map(int, readline().split())) for _ in range(N)]
#  for u, v in uv:
