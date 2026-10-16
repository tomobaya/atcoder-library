# 2 * N 人（偶数）の中から 2 人ずつを選んで列挙する全パターンを出力する
def enumerate_pairs(n):
  def dfs(selected, current_pairs):
    # 全てのペアが作られたら結果に追加
    if len(current_pairs) == n: 
      result.append(current_pairs[:]) # [:] で浅いコピー
      return
    # まだペアが完成していないなら完成をめざす。
    # ペアを作り、同じ関数を呼び出した後はバックトラックを用いる。つまり、元の状態に戻す。    
    for i in range(2 * n): # 最初の未使用の人を探し、選択する
      if not selected[i]:
        first_unselected = i
        selected[i] = True
        break
    for another in range(first_unselected + 1, 2 * n): # 残りの人とペアを作る
      if not selected[another]:
        selected[another] = True
        current_pairs.append((first_unselected, another))
        dfs(selected, current_pairs)
        current_pairs.pop() # ここからはバックトラック処理
        selected[another] = False 
    selected[first_unselected] = False # 「最初の未使用の人」も選択前に戻す

  result = []
  selected = [False for _ in range(2 * n)]
  dfs(selected, [])
  return result

N = 4
patterns = enumerate_pairs(N)
for pat in patterns:
  print(pat)

