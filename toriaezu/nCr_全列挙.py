# 0 と 1 が合わせて n 個
# そのうち 0 が r 個ある
# そのような長さ n の配列のパターンを全て列挙する。

# 以下、0 を a 個、 1 を b 個として関数を作った。


def rec(a, b, pat):
  if a > 0:
    rec(a - 1, b, pat + [0])
  
  if b > 0:
    rec(a, b - 1, pat + [1])
  
  if a == b == 0:
    global patterns 
    patterns.append(pat)
    return []

patterns = []
a = 4
b = 2
rec(a, b, [])
print(patterns)