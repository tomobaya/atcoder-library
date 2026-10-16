### 遅延セグメント木
# ・セグメント木 ...... 一点更新・区間取得ができる。
# 
# ・遅延セグメント木 ...... 区間更新・区間取得ができる。
#   通常のセグメントツリーでは区間更新の計算量が大きいため
#   二分木を2つ使って値の更新を遅延させる。

from atcoder.lazysegtree import LazySegTree
A = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# 範囲内の最大値を得る
# opの定義
def op(n1,n2):
    return max(n1,n2)

#単位元の定義
e=-1

#mappingの定義
def mapping(f:int,data:int):
  #操作が単位元であれば、dataのままで良い
  if f == e:
    return data
  else:
    #dataの値に関係なく上書きする
    return f
    
#compositionの定義
def composition(f,g):
  if f == e:
    return g
  else:
    #子の更新に関係なく親の値を受け取る
    return f
    
#id_を定義
id_ = -1

#初期値を定義
v = [0]*10
#[0,0,0,0,0,0,0,0,0,0]

#インスタンス化
lazy_seg_tree = LazySegTree(op,e,mapping,composition,id_,v)

#値の更新
lazy_seg_tree.set(3,1)
#[0,0,0,1,0,0,0,0,0,0]

#値の取得
print(lazy_seg_tree.get(3))
#>>1

#区間のopを取得
max_height = lazy_seg_tree.prod(0,4)
print(max_height)
#>>1

#区間にその区間の最大値＋1の値を入れる
lazy_seg_tree.apply(0,4,max_height+1)
#[2,2,2,2,0,0,0,0,0,0]

#全区間のopを取得
print(lazy_seg_tree.all_prod())
#>>2

#条件を満たし続けるrightのインデックスを取得
print(lazy_seg_tree.max_right(1 ,lambda x: x<1))
#>>1

#条件を満たし続けるleftのインデックスを取得
print(lazy_seg_tree.min_left(8,lambda x: x<1))
#>>4

