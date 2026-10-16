import itertools

# 重複なし・並び替えなし (4C2 = 6)
for pair in itertools.combinations("ABCD", 2):
  print(pair)

# 重複あり・並び替えなし (4C2 + 4 = 10) (4 は同じもの同士の組み合わせの数)
for pair in itertools.combinations_with_replacement([10, 22, 99, 60], 2):
  print(pair, end=" ")
print("")

# 重複なし・並び替えあり (4P3)
for pattern in itertools.permutations([i for i in range(4)], 3):
  print(pattern, end=" ")
print("")

# 重複あり・並び替えあり（3 ** 4）
for pattern in itertools.product("357", repeat = 4):
  str = "".join(pattern)
  num = int(str)
  print(num, end=" ")
print("")

# 番外編 0 を a 個と 1 を b 個 …… 別ファイル "_nCr_全列挙.py" を参照のこと

###
# 使用例 1 : bit 全探索
for pattern in itertools.product([0, 1], repeat = 4):
  print(pattern)