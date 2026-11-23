# RLE (Run Length Encoding), 連長圧縮
# 配列を見て「何が何個続いている」を調べる。
# 結果を [文字、個数] の配列に格納して出力する。

def run_length_encoding(string): # 引数は文字列のほか、配列も可
  result = []
  for i in range(len(string)):
    if result == [] or result[-1][0] != string[i]:
      result.append([string[i], 1])
    else:
      result[-1][1] += 1
  return result

A = "aaaaabbbbbcdeffffffggggggghhiikjjmlnoooooppppqqqqqrrrrrrs"
print(run_length_encoding(A))



