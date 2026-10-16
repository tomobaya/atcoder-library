"""
累積和を利用して 2 次元配列の範囲和を求める関数
"""

# 配列 A の (a, b) から (c, d) までの矩形範囲の和を求める
def square_sum(A, a, b, c, d):
  if (a > c) or (b > d):
    return 0

  # 累積和を求める
  h, w = len(A), len(A[0])
  cumA = [[0 for _ in range(w)] for _ in range(h)]
  cumA[0][0] = A[0][0]
  for i in range(h):
    for j in range(w):
      if i == 0:
        cumA[i][j] = cumA[i][j-1] + A[i][j]
      elif j == 0:
        cumA[i][j] = cumA[i-1][j] + A[i][j]
      else:
        cumA[i][j] = cumA[i-1][j] + cumA[i][j-1] + A[i][j] - cumA[i-1][j-1]
  """
  for i in range(h):
    for j in range(w):
      print(cumA[i][j], end=" ")
    print("")
  """

  if a == b == 0:
    sum_ab_cd = cumA[c][d]
  elif a == 0:
    sum_ab_cd = cumA[c][d] - cumA[c][b-1]
  elif b == 0:
    sum_ab_cd = cumA[c][d] - cumA[a-1][d]
  else:
    sum_ab_cd = cumA[c][d] - cumA[a-1][d] - cumA[c][b-1] + cumA[a-1][b-1]

  # 試しに範囲内を出力
  print("")
  for i in range(a, c+1):
    for j in range(b, d+1):
      print(A[i][j], end=" ")
    print("")
  
  return sum_ab_cd

H, W = 4, 5
A = [[0 for _ in range(W)] for _ in range(H)]
A[0] = [1,2,3,4,5]
A[1] = [4,6,3,2,8]
A[2] = [9,0,1,1,7]
A[3] = [8,7,5,3,2]

print(square_sum(A, 0, 0, 0, 0))
print(square_sum(A, 0, 0, 2, 2))
print(square_sum(A, 1, 3, 2, 4))
print(square_sum(A, 2, 1, 2, 3))
print(square_sum(A, 1, 1, 2, 3))
print(square_sum(A, 0, 0, 3, 4))


