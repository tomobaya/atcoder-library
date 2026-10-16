# dict の足し算引き算を行う関数
# {数値: 数値} の場合のみに対応
def dict_plus(d1, d2):
  d3 = dict()
  for key, value in d1.items():
    if key in d3:
      d3[key] += value
    else:
      d3[key] = value

  for key, value in d2.items():
    if key in d3:
      d3[key] += value
    else:
      d3[key] = value
  return d3

def dict_minus(d1, d2):
  d3 = dict()
  for key, value in d1.items():
    if key in d3:
      d3[key] += value
    else:
      d3[key] = value

  for key, value in d2.items():
    if key in d3:
      d3[key] -= value
    else:
      d3[key] = - value
  return d3
  
d1 = {1: 10, 2:30}
d2 = {1: 1000, 2:15, 3:5}
print(dict_plus(d1, d2))

d1 = {1: 10, 2:30}
d2 = {1: 1000, 2:15, 3:5}
print(dict_minus(d1, d2))