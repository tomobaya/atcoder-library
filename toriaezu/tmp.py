# Binary Indexed Tree (Fenwick Tree) の使用例

# BIT クラスの定義（タブ幅2）
class BIT:
  def __init__(self, n):
    self.n = n
    self.n0 = 2**(n-1).bit_length()
    self.data = [0]*(n+1)
    self.el = [0]*(n+1)
  def init(self, A):
    self.data[1:] = A
    for i in range(1, self.n):
      if i + (i & -i) <= self.n:
        self.data[i + (i & -i)] += self.data[i]
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # i 番目の要素に x を加算
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j=None):
    # j が指定されなければ i 番目の元の要素を返す
    if j is None:
      return self.el[i]
    # j が指定されている場合は区間和を返す（self.sum(j) - self.sum(i)）
    return self.sum(j) - self.sum(i)
  def lower_bound(self, x):
    # 累積和が x を超える最小のインデックスを返す
    w = i = 0
    k = self.n0
    while k:
      if i+k <= self.n and w + self.data[i+k] <= x:
        w += self.data[i+k]
        i += k
      k >>= 1
    return i+1

# 使用例
def main():
  # 初期の配列（BIT は 1-indexed で管理）
  A = [1, 2, 3, 4, 5]
  n = len(A)
  
  # BIT インスタンスを生成し、配列 A で初期化
  bit = BIT(n)
  bit.init(A)
  
  # 例1: 先頭から3つの要素の累積和を求める
  # 期待値: 1 + 2 + 3 = 6
  print("Prefix sum up to index 3:", bit.sum(3))
  
  # 例2: 3 番目の要素に 2 を加算する
  # 元の A[2] は 3 なので、更新後は 5 になる
  bit.add(3, 2)
  # 先頭から3つの要素の累積和は 1 + 2 + 5 = 8 となる
  print("After adding 2 to index 3, prefix sum up to index 3:", bit.sum(3))
  
  # 例3: 3 番目の要素の値を直接取得
  print("Value at index 3:", bit.get(3))
  
  # 例4: インデックス 2 から 4 までの区間和を取得
  # BIT.get(i, j) は self.sum(j) - self.sum(i) を返すので、
  # ここでは get(1, 4) により、2番目から4番目の要素の和が得られる
  # 期待値: 2 + 5 + 4 = 11
  print("Range sum from index 2 to index 4:", bit.get(1, 4))
  
  # 例5: 累積和が 7 を超える最小のインデックスを lower_bound で取得
  # 更新後の配列は [1, 2, 5, 4, 5] となっているので、
  # 累積和: 1, 3, 8, 12, 17 ... となり、7 を超えるのは 3 番目
  print("Lower bound index for cumulative sum > 7:", bit.lower_bound(7))
  
if __name__ == '__main__':
  main()
