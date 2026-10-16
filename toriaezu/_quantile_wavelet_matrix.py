# https://qiita.com/izu_nori/items/410831398fda74e35f5f#wavelet-matrix
# ウェーブレット行列なるものを使って
# 整数列に対して quantile(l,r,i)
# ([l,r)の中でi番目に小さい値を取得する)
# を行う。iは0-index.
# ただし数字の重複があったら別カウントみたい。不便。



import array as ar
from itertools import accumulate

class BitVector:
    def __init__(self, data):
        self.n = len(data)
        self.data = ar.array('b',data)
        self.cumsum = ar.array('i',[0] + list(accumulate(data)))
    def access(self, i):
        return self.data[i]
    def rank(self, i, x):
        return self.cumsum[i] if x else i - self.cumsum[i]
    def select(self, i, x):
        l,r = 0, self.n
        while r-l > 1:
            m = (r+l)//2
            n = self.cumsum[m] if x else m - self.cumsum[m]
            if n < i+1:
                l = m
            else:
                r = m
        return l
class WaveletMatrix:
    def __init__(self, data):
        self.T = data[:]
        self.N = len(data)
        max_value = max(data)
        self.l = max_value.bit_length()-1
        th = 1 << self.l
        self.B = []
        self.cnt0 = []
        while th:
            self.B.append(BitVector(ar.array('b',((t&th)==th for t in self.T))))
            L,R = [],[]
            for t,b in zip(self.T, self.B[-1].data):
                if b:
                    R.append(t)
                else:
                    L.append(t)
            self.cnt0.append(len(L))
            self.T = L + R
            th >>= 1
    # find i-th value in [l,r)
    def quantile(self, l, r, i):
        th = 1 << self.l
        for c0, row in zip(self.cnt0,self.B):
            n0 = row.rank(r,0) - row.rank(l,0)
            n1 = row.rank(r,1) - row.rank(l,1)
            if n0 <= i:
                i -= n0
                l = c0 + row.rank(l,1)
                r = c0 + row.rank(r,1)
            else:
                l = row.rank(l,0)
                r = row.rank(r,0)
            th >>= 1
        return self.T[r-1]


A = [1, 4, 1, 2, 5, 2, 3, 2, 1]
W = WaveletMatrix([1, 4, 1, 2, 5, 2, 3, 2, 1])
W = WaveletMatrix([0,1,2,3,4,5,6])
print(W.quantile(0, 7, 0))
print(W.quantile(2, 5, 1))
print(W.quantile(2, 5, 2))

