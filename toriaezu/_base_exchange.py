# n 進数を 10 進数に変換する
def base_n_to_10(n, string):
  string = string[::-1]
  n10 = 0
  for digit in range(len(string)):
    if int(string[digit]) >= n:
      print(f"{n} 以上の数字が混ざっています", end=" ")
      return "error."
    n10 += n ** digit * int(string[digit])
  return n10
  
# 10進数を n 進数に変換する
def base_10_to_n(n, num):
  n_str = ""
  while (num >= n):
    n_str += str(num % n)
    num //= n
  n_str += str(num)
  n_str = n_str[::-1]
  return n_str

# 10進数を n 進数に変換する（0埋めver.）
def base_10_to_n_fill_0(n, num, length):
  n_str = ""
  while (num >= n):
    n_str += str(num % n)
    num //= n
  n_str += str(num)
  for i in range(length - len(n_str)):
    n_str += "0"
  n_str = n_str[::-1]
  return n_str

print(base_n_to_10(2, "100"))
print(base_n_to_10(2, "100001"))
print(base_10_to_n(2, 4))
print(base_10_to_n(2, 33))
print(base_10_to_n_fill_0(2, 4, 10))
print(base_10_to_n_fill_0(2, 33, 10))
print(base_n_to_10(2, "230"))