def func(n, G, seen):
  result = []
  def dfs(v): # 帰りがけで探索
    for v2 in G[v]:
      if not seen[v2]:
        dfs(v2)
    seen[v] = True
    result.append(v)
    
  dfs(1)
  return result

