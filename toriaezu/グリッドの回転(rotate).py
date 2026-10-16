# rotate : 回転させる
# 縦 H x 横 W のマス目を 90 度ずつ回転させる。

# 0-index の場合
def rotate_grid0(S, h, w):
  S90 = [["" for _ in range(h)] for _ in range(w)] # 右90° S(i, j) -> S90(j, H-i-1)
  S180 = [["" for _ in range(w)] for _ in range(h)] # 右180° S(i, j) -> S180(H-i-1, W-j-1)
  S270 = [["" for _ in range(h)] for _ in range(w)] # 右270° (i, j) -> S270(W-j-1, i)
  for i in range(h):
    for j in range(w):
      S90[j][h-i-1] = S[i][j]
      S180[h-i-1][w-j-1] = S[i][j]
      S270[w-j-1][i] = S[i][j]
  return S90, S180, S270


# 1-index の場合
def rotate_grid(S, h, w):
  S90 = [["" for _ in range(h+1)] for _ in range(w+1)] # 右90° S(i, j) -> S90(j, H-i+1)
  S180 = [["" for _ in range(w+1)] for _ in range(h+1)] # 右180° S(i, j) -> S180(H-i+1, W-j+1)
  S270 = [["" for _ in range(h+1)] for _ in range(w+1)] # 右270° (i, j) -> S270(W-j+1, i)
  for i in range(1, h+1):
    for j in range(1, w+1):
      S90[j][h-i+1] = S[i][j]
      S180[h-i+1][w-j+1] = S[i][j]
      S270[w-j+1][i] = S[i][j]
  return S90, S180, S270

# 使用例
H = 5
W = 8
S = [
  ["", "", "", "", "", "", "", "", ""], 
  ["", ".", "#", ".", ".", ".", ".", ".", "#"], 
  ["", ".", ".", "#", ".", "#", ".", "#", "#"],
  ["", ".", ".", ".", "#", ".", ".", "#", "#"],
  ["", ".", ".", "#", ".", "#", ".", ".", "."],
  ["", ".", "#", ".", ".", ".", ".", "#", "."]
]
S90, S180, S270 = rotate_grid(S, H, W)

# 出力
for i in range(1, H+1):
  for j in range(1, W+1):
    print(S[i][j], end="")
  print("")
print("")

for i in range(1, W+1):
  for j in range(1, H+1):
    print(S90[i][j], end="")
  print("")
print("")

for i in range(1, H+1):
  for j in range(1, W+1):
    print(S180[i][j], end="")
  print("")
print("")

for i in range(1, W+1):
  for j in range(1, H+1):
    print(S270[i][j], end="")
  print("")

"""
# 90°ずつ回転させた配列を用意する。
S90 = [["" for _ in range(H+1)] for _ in range(W+1)] # 左90° (i, j) -> (N-j+1, i)
S180 = [["" for _ in range(W+1)] for _ in range(H+1)] # 左180° (i, j) -> (N-i+1, N-j+1)
S270 = [["" for _ in range(H+1)] for _ in range(W+1)] # 左270° (i, j) -> (j, N-i+1)
# 中身を入れていく。
for i in range(1, W+1):
  for j in range(1, H+1):
    S90[i][j] = S[H-j+1][i]
    S270[i][j] = S[j][W-i+1]

for i in range(1, H+1):
  for j in range(1, W+1):
    S180[i][j] = S[H-i+1][W-j+1]

# 出力する。
for i in range(1, H+1):
  for j in range(1, W+1):
    print(S[i][j], end="")
  print("")
print("")

for i in range(1, W+1):
  for j in range(1, H+1):
    print(S90[i][j], end="")
  print("")
print("")

for i in range(1, H+1):
  for j in range(1, W+1):
    print(S180[i][j], end="")
  print("")
print("")

for i in range(1, W+1):
  for j in range(1, H+1):
    print(S270[i][j], end="")
  print("")
"""