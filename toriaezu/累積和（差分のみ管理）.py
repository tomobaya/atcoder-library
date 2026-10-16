"""
長さ N の配列 A の累積和をとる。
通常の累積和だと累積和配列が長さ N となり、
これをたくさん使う場合は配列作成の時間で TLE になる。

例えば
Σ N <= 10**6 
K <= 10**6
になる問題の場合、長さ N の配列を K 個用意すると TLE だけど
和の値が変わるところだけを記録するようにしておけば
トータルでメモリ量 N だけで済むようになる。

そんな累積和のとりかたを示す。
"""

N = 10
A = [0] + [1, 0, 3, 0, 20, 0, 0, 2, 9, 4] # 1-index にする。

# 累積和用の配列を用意する
cum_idx = [0]
cum_value = [0]

for i in range(1, N+1):
  if A[i] == 0: continue
  cum_idx.append(i)
  cum_value.append(cum_value[-1] + A[i])

print(cum_idx)
print(cum_value)

# この累積和を利用するとき、cum_idx に存在しない添字のところを調べたかったら
# 調べたい添字 k に対してそれ以下で最大のところを二分探索で調べて参照すれば良い。
import bisect
k = 7
idx = bisect.bisect_right(cum_idx, k) - 1
print(k, "番目までの累積和は", cum_value[idx], "です。")

k = 6
idx = bisect.bisect_right(cum_idx, k) - 1
print(k, "番目までの累積和は", cum_value[idx], "です。")


k = 2
idx = bisect.bisect_right(cum_idx, k) - 1
print(k, "番目までの累積和は", cum_value[idx], "です。")

k = 10
idx = bisect.bisect_right(cum_idx, k) - 1
print(k, "番目までの累積和は", cum_value[idx], "です。")



