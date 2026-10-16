import itertools

def rec(a, b, pat):
  if a > 0:
    rec(a - 1, b, pat + [0])
  
  if b > 0:
    rec(a, b - 1, pat + [1])
  
  if a == b == 0:
    global patterns 
    patterns.append(pat)
    return []

# n 個のお菓子を r 人に配る。配られない子が居てもよい。
n = 13
r = 3
patterns = []
rec(n, r-1, [])
print(patterns)

okashi = []
for pat in patterns:
  tmp_okashi = []
  tmp = 0
  for i in range(n+r-1):
    if pat[i] == 0:
      tmp += 1
    else:
      tmp_okashi.append(tmp)
      tmp = 0
  tmp_okashi.append(tmp)
  okashi.append(tmp_okashi)
print(okashi)