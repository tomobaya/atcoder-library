"""
# Trie （Trie 木）

## 説明
共通の接頭辞 (prefix) を見る問題に極めて有用なデータ構造。
テンプレは4行だけ。クラス3行、オブジェクト生成1行。

class Trie: 
  def __init__(self):   
    self.child = dict()

root = Trie() 

要するに木。
.child には dict() 型を入れる。
key が辺を表し、value が子の Trie オブジェクトである。

Trie では各頂点に文字などの情報を持たせるわけだが、
同じ情報を持った子を dict() を使って束ねている。
この仕組みにより、
同じ接頭辞を持った配列（特に文字列）は
木の上で（共通している間は）同じ経路をたどる。

その他欲しい情報があれば
self.value = 
みたいにして持たせる。

## 計算量
木に入れた文字（または数列の項数）の総数。

もう少し厳密には、全入力文字列の長さの合計を L とすれば、
- 構築: O(L)
- 空間: O(L)
- 長さ M の文字列の挿入・検索 : O(M)

## 使われる問題
ABC353-E
ABC437-E
ABC287-E

###########################################
## ライブラリ本体
"""

# Trie テンプレ
# 最小限はこの4行だけ。
class Trie: 
  # __init__(self, value = None) などとして情報を渡すようにもできる
  def __init__(self):   
    self.child = dict() # {辺のラベル（「次の文字」など） : 子のTrieオブジェクト}
    # child の key = 子のラベル = Trie 木における辺にあたる
    # その他、value など欲しい情報を持たせる
root = Trie() # root を作る。あとはその下に繋げていく

# 基本的な動き
# あるノードについてその子の一覧を見る。次の要素 c に進むとする。
# 次に進む子ノードがもうあるならそこに進んで、そうでないなら新たに Trie() として生成する。
# これは c というラベルの辺があれば進むということ。その後は実装としては
# 「子ノードを作り、中身を入れる」もしくは「既にある子ノードを選び、中身を追加する」

"""
# 使用例
# ABC353-E
class Trie: 
  def __init__(self, value = None):
    self.child = {}
    self.value = value
    self.count = 0
root = Trie()

N = int(input()) 
S = list(input().split()) 
ans = 0
for s in S: 
  now = root 
  for c in s: 
    if c not in now.child: # now.child は dict. これは dict にデータを入れるときのいつもの流れ.
      now.child[c] = Trie(c)  
    now = now.child[c] 

    ans += now.count
    now.count += 1
print(ans)
"""
