import math
a = math.radians(30) # 度からラジアンへ
print(math.radians(30))
print(math.sin(a)) # sin 関数はラジアンを使用する

print(math.cos(math.radians(30))) # √3 / 2 = 0.8660...
print(math.cos(math.radians(390))) # √3 / 2 = 0.8660...

rad_b = math.degrees(math.pi * 0.5) # ラジアンから度へ
print(rad_b)
print(math.degrees(math.pi * 1.0))
print(math.degrees(math.pi * 1.75))
print(math.degrees(math.pi * 2.0))
print("=========================")

"""
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
"""
Ax, Ay = 1, 3
Bx, By = -1, 10
Cx, Cy = 7, 1

AB_2 = (Ax - Bx) ** 2 + (Ay - By) ** 2 # 辺 AB の長さの 2 乗
BC_2 = (Bx - Cx) ** 2 + (By - Cy) ** 2
CA_2 = (Cx - Ax) ** 2 + (Cy - Ay) ** 2
AB = math.sqrt(AB_2) # 辺 AB の長さ
BC = math.sqrt(BC_2)
CA = math.sqrt(CA_2)

# 余弦定理より
cosA = (CA_2 + AB_2 - BC_2) / (2 * CA * AB)
cosB = (AB_2 + BC_2 - CA_2) / (2 * AB * BC)
cosC = (BC_2 + CA_2 - AB_2) / (2 * BC * CA)

print(math.degrees(math.acos(cosA))) # それぞれの角度
print(math.degrees(math.acos(cosB)))
print(math.degrees(math.acos(cosC)))

# ヘロンの公式
s = (AB + BC + CA) / 2
S = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))

print(cosA, cosB, cosC, S)



# 外積について
# ABC266-C
# 2 点 A=(Ax​,Ay​),B=(Bx​,By​) に対し、
# ∠AOB は、Ax​By​−Ay​Bx​>0 のとき 180 度未満であり、
# ≤0 のとき 180 度以上である。ただし、角度は反時計回りに測るものとする。
#
# 外積の性質：
# a=(a1​,a2​,a3​),b=(b1​,b2​,b3​) としたとき、
# a×b=(a2 * ​b3 ​− a3 * ​b2​, a3 * ​b1 ​− a1 * ​b3​, a1 * ​b2 ​− a2 * ​b1​) 
#
# 今 a3, b3 が 0 なので axb = (0, 0, a1 * b2 - a2 * b1)

# ABC266-C 別解から、2点(x1, y1) (x2, y2) が直線 f(x, y) = 0 の異なる側にあるかどうかの判定方法
# f(x1, y1) と f(x2, y2) の符号が異なるかどうかでわかる。
# 
# 2点 (x3, y3) と (x4, y4) を通る直線の方程式は
# (x4 - x3)(y - y3) = (y4 - y3)(x - x3) 
# で求まる。

