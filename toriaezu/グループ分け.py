"""
N 人の人を T 個のチームに分ける。
パターンを全列挙する。

関連 : ABC310-D, ABC390-D

"""
import sys
import copy
sys.setrecursionlimit(10**7)

# N <= 12 までじゃないと時間がかかりすぎる
N, T = 12, 8

def func(n, t):
  patterns = []

  # 今あるチームの中身はリスト teams に格納。今からどこかに入れたい人の番号が player_num.
  def dfs(player_num, teams):
    if player_num > n:
      if len(teams) == t:
        #print(teams)
        # teams の中身を見たいなら、
        # teams は再帰呼び出しのたびに中身が変わるので
        # 参照ではなく中身をコピーして渡す必要がある。
        patterns.append(copy.deepcopy(teams))
      return
      
    # 既存のチームに選手 player_num を追加する
    for team_num in range(len(teams)):
      teams[team_num].add(player_num) # 追加
      dfs(player_num + 1, teams)
      teams[team_num].remove(player_num) # 削除（バックトラック）

    # 新たなチームを作ってそこに選手 player_num を入れる
    if len(teams) < T:
      teams.append({player_num}) # 追加
      dfs(player_num + 1, teams)
      teams.pop() # 削除（バックトラック）

  dfs(1, [])
  print(patterns)

func(N, T)
