# LIS(Longest Increase Subsequence, 最長増加部分列)
# これをO(N logN) で求める。なお転倒数との関係は一切ない。
# 中身の理解はなんとなく。

import bisect
def lis_reconstruct_strict(A):
  n = len(A)
  tails = []          # 長さ i+1 の増加部分列の末尾に置くことができる最小の値を tails[i] に格納
  tails_idx = []      # tails[k] を作った A の添字
  prev_idx = [-1 for _ in range(n)]  # 復元用。A[i] を採用したときにその直前の文字 A[i]（の添字）を格納

  for i, x in enumerate(A):
    k = bisect.bisect_left(tails, x)  # x 以上の最小
    if k == len(tails): # どれよりも大きいやつが来たらそのまま追加
      tails.append(x)
      tails_idx.append(i)
    else: # そうでない場合は k 番目の数をより小さなものに更新する（当然元あった数より x の方が小さいまたは等しい）
      tails[k] = x
      tails_idx[k] = i
    # 直前ポインタを張る。今 A[i] を末尾にする長さ k+1 の増加部分列ができたので、
    # その直前の要素（長さ k の末尾）の添字である tails_idx[k-1] を入れておく。
    if k > 0: # k == 0 のときは先頭なので無視
      prev_idx[i] = tails_idx[k-1]

  # 復元
  ret = []
  i = tails_idx[-1]
  while i != -1:
    ret.append(A[i])
    i = prev_idx[i]
  ret.reverse()
  return ret


print(lis_reconstruct_strict([1,3,4,5,6]))
print(lis_reconstruct_strict([1,3,4,5,6,2]))
print(lis_reconstruct_strict([10,9,8]))
print(lis_reconstruct_strict([10,9,8, 1, 2, 3, 7, 6, 4, 5]))