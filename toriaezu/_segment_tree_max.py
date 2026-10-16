####### セグメント木
# SEG_INIT の値は求めたいものに応じて変える。
# 例えば最大値を求める場合は 0 など。
SEG_INIT = 0

# num 番目の値に score 点を入れる
#### max の部分には任意のやりたい演算を入れる
def update_segtree(seg_list, num, score):
  p = len(seg_list) // 2 + num - 1
  while (p != 1):
    seg_list[p] = max(seg_list[p], score)
    p //= 2
  seg_list[1] = max(seg_list[1], seg_list[2], seg_list[3])
  return seg_list
 
# index 1 から p までのそれぞれのカバー範囲を算出する
def get_cover_range(seg_list):
  cover = [0, 0] * (len(seg_list) // 2)
  for i in range(1, len(seg_list)):
    q = i
    dividable = 0
    while (q >= 2):
      q //= 2
      dividable += 1
    cover_length = (len(seg_list) // 2) // (2 ** dividable)
    num = i % (2 ** dividable)
    cover_from = cover_length * num + 1
    cover_to = cover_length * (num + 1) - 1 + 1
    # print(i, dividable, cover_length, num, f"{cover_from}-{cover_to}")
    #print(i, f"{cover_from}-{cover_to}")
    cover[i] = [cover_from, cover_to]
  return cover

# 配列を元にセグメントツリーを作る
def create_segtree(orig_list):
  # orig_list は 1-index でなくてはいけない
  seg_size = 4
  p = len(orig_list) - 2 # 1-index なので余分に 1 引く
  while(p >= 2):
    p //= 2
    seg_size *= 2
  # 初期化
  seg_list = [SEG_INIT] * seg_size
  for i in range(1, len(orig_list)):
    update_segtree(seg_list, i, orig_list[i])
 
  # それぞれの index のカバー範囲を算出する
  cover = get_cover_range(seg_list)
  return seg_list, cover
 
# 部分配列から答えを取得する
def rec_segtree(seg_list, now, cover, left, right):
  #print(now)
  #print(cover[now], left, right)
  
  # left, right と cover[now] を比較する
  if cover[now][1] < left or right < cover[now][0]:
    # 全く範囲が被らないなら初期値を返す
    #print("aaa")
    return SEG_INIT
  elif cover[now][0] == left and right == cover[now][1]:
    # ぴったり入っているならそこの値を返す
    #print("bbb")
    return seg_list[now]
  else:
    #print("ccc")
    # そうでないならはみ出す。このとき子を見る。
    partition = (cover[now][0] + cover[now][1] - 1) // 2 # 子の仕切り。左の子の右端のインデックス。
    if left <= partition and partition < right:
      # 2人の子をまたぐ場合
      value_left  = rec_segtree(seg_list, now * 2    , cover, left, partition)
      value_right = rec_segtree(seg_list, now * 2 + 1, cover, partition + 1, right)
      #### max の部分には任意のやりたい演算を入れる
      return max(value_left, value_right)
    elif right <= partition:
      # 左の子だけを見る場合
      return rec_segtree(seg_list, now * 2    , cover, left, right)
    else:
      # 右の子だけを見る場合
      return rec_segtree(seg_list, now * 2 + 1, cover, left, right)
    

# main    
orig_list = [0, 2, 6, 9, 10, 7, 3, 5, 4, 8, 1]
seg_list, cover = create_segtree(orig_list)

print(rec_segtree(seg_list, 1, cover, 1, 10))
print(rec_segtree(seg_list, 1, cover, 1, 3))
print(rec_segtree(seg_list, 1, cover, 8, 10))
print(rec_segtree(seg_list, 1, cover, 6, 8))
