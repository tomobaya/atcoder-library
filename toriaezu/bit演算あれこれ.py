n = 54 # 110110
x = 3

#### 変更したいとき
# n の x ビット目だけを 1 にする（Set） = x ビット目だけが 1 のものと OR をとる
n = n | (1 << x)
print(n)
# または
n |= (1 << x)
print(n)

x = 2
# n の x ビット目だけを 0 にする（Clear） = x ビット目だけが 0 のものと AND をとる
n = n & ~(1 << x)
print(n)
# または
n &= ~(1 << x)
print(n)

x = 0
# n の x ビット目を反転する（Toggle） = XOR は 1 をぶつけると反転させられ、0 をぶつけるとそのままにできる
n = n ^ (1 << x)
print(n)
# または
n ^= (1 << x)
print(n)

#### 中身を調べたいとき
x = 5
# n の x ビット目が 1 かどうかを調べる
# 方法①：ビットをシフトして下位ビットを取り出す
is_one = ((n >> x) & 1) == 1
print(is_one)
# 方法②：マスクして bool 判定 = x ビット目だけが 1 のものと AND をとる
is_one = bool(n & (1 << x))
print(is_one)

# n の x ビット目が 0 かどうかを調べる
# 方法①
is_zero = ((n >> x) & 1) == 0
print(is_zero)
# 方法② = x ビット目だけが 1 のものと AND をとって not する
is_zero = not (n & (1 << x))
print(is_zero)


# 補足：よく使うビット演算テクニック
# 最下位の 1 ビットを取り出す
lowbit = n & -n

# 最下位の 1 ビットを消す
n_without_lowbit = n & (n - 1)

# マスク mask の部分集合を列挙するとき
"""
sub = mask
while True:
    # sub が mask の部分集合
    ...
    if sub == 0:
        break
    sub = (sub - 1) & mask
"""