# 引数が回文なら True, そうでなければ False を返す
def is_palindrome(string):
  length = len(string)
  max_length = (length - 1) // 2
  res = True
  for i in range(max_length + 1):
    if string[i] != string[length - 1 - i]:
      res = False
      break
  return res


print(is_palindrome("ossan"))
print(is_palindrome("ossanasso"))
print(is_palindrome("a"))
print(is_palindrome("assa"))
print(is_palindrome("yzy"))


# 文字列 S の中に回文が含まれているかどうかを調べる。