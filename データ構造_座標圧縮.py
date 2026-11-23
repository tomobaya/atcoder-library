def zaatsu(X):
  Y, Z = dict(), dict() 
  for i, x in enumerate(sorted(set(X))):
    Y[i] = x # 座標復元（圧縮の逆）
    Z[x] = i # 座標圧縮
  return Y, Z # Y: 圧縮後→元の値、Z: 元の値→圧縮後