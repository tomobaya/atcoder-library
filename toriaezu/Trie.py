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
# 使用例@ABC353-E
class Trie: 
  def __init__(self, value = None):
    self.child = {}
    self.value = value
    self.count = 0
root = Trie()

N = int(input()) 
S = list(input().split()) 
root = Trie() 
for s in S: 
  now = root 
  for c in s: 
    if c not in now.child: 
      now.child[c] = Trie(c)  
    now = now.child[c] 
    now.count += 1
"""



#####################  
# 以下旧テンプレ
"""
# Trie 木
prefix(接頭辞)を見る問題に極めて有効。
全てのprefixを総当たりで調べようとしたら全列挙に O(N^2) かかってしまう。
（"prefix" なら "p", "pr", ..., "prefix" となりそれぞれに文字数分の時間がかかるので 1+2+3+4+5+6=21回）
Trieは共通のprefixを括り出すことにより文字数の総和の時間で済ませることができる。O(N).
アルファベットが26種類しかないため、必然的に大量の共通prefixが生まれる。そのおかげで高速化される。

テンプレはそのまま使うのではなく各関数の改良が必要になる。応用範囲は広い。
__init__ 関数に格納したい値を設定し、
insert 関数の中で挿入しながら数えるなど。

作り上げた Trie の中を DFS により探索する手もある。
"""

"""
class Trie: 
  def __init__(self): 
    self.children = {} # 子ノードを入れる dict() 
    self.is_end = False # この文字が単語の終端かどうか 
    self.passcount = 0

  # 新たな語を挿入する。
  def insert(self, word):
    ret = 0
    pointer = self # Trie の root から始める
    for char in word: # 単語を1字ずつ見る
      if char not in pointer.children: # 子がこの文字を持っていなければ新たな子を増やす
        pointer.children[char] = Trie()
      pointer = pointer.children[char] # ポインタを子につけかえる
      ret += pointer.passcount # カウント+1の前に数える
      pointer.passcount += 1 # 子のカウントを +1
    pointer.is_end = True
    return ret

  # 与えられた接頭辞が Trie 木の中にいくつあるかを返す
  def count_prefix(self, prefix):
    pointer = self
    for char in prefix:
      next = pointer.children.get(char) # 子 char があるかどうか調べる
      if next is None:
        return 0
      pointer = next
    return pointer.passcount
  

# これらの共通の接頭辞の長さの合計を求める。
# "a" が3つ -> 3通り
# "ap" "app" "appl" が2つずつ ->1通りずつ
# 計 6 通りが答え。
S = ["apple", "apply", "ace"]

trie = Trie()
# insert しながら数えていく
ans = 0
for s in S:
  ans += trie.insert(s)

print(ans)
"""


"""
## 汎用トライの設計ポイント
1) ノードに何を持たせるか（最小セット＋拡張）
### 最小セット
* children: dict<char, node>（アルファベットが固定なら配列化も可）
* endcount: int（このノードで“単語が終わる”回数＝重複カウント）
* passcount: int（このノードを通過した文字列本数＝そのprefix本数）
### よく使う拡張（必要なときだけ追加）
* subtree_size: このノード配下の終端総数（重複反映）
* depth: ルートからの深さ（共通prefix長・辞書順走査で便利）
* ids/list: その単語のID一覧（上限次第で保持）
* best_k候補: オートコンプリートTop-Kなどのための小ヒープ/配列
ルール：足し算で済む量は insert/erase で1文字ごとに更新できる＝オンラインで使える

2) 典型クエリと“何を持てば”O(|S|)で解けるか
* 「文字列Sが登録されている個数」→ 末端の endcount
* 「prefix P を持つ文字列本数」→ passcount（Pノードの値）
* 「prefix P の辞書順列挙」→ Pノードから DFS/BFS（children順に走査）
* 「共通prefix長の総和」→ 全ノードで C(passcount,2) を合計（今やったやつ）
* 「共通prefix長がL以上のペア数」→ 深さ ≥ L のノードだけ C(passcount,2) を合計
* 「各クエリ文字列Qと既挿入集合の共通prefix長」→ Qで降りながら“降りられた深さ”が答え
* 「prefix P の中で完全一致K個だけ欲しい」→ Pから辞書順で endcount を拾いながらK個
* 「削除対応」→ insert の逆を実装（passcount--/endcount--、0になれば子を掃除）

3) 「オンライン加算」汎用パターン
* “二つの文字列の間で、ノードを共有しているかどうか”が貢献の源泉。
* insertの各文字で到達したノードに対して：
  * 事前に「現在の passcount が貢献する値」を答えへ加える
  * その後 passcount += 1

例：
* 共通prefix総和 → ans += passcount
* 「共通prefix長がL以上のペア数」→ 深さがL以上のノードだけ ans += passcount
* 「prefix P 固定で、Pを持つ既存本数」→ Pに到達した時点で ans += passcount(P)
コツ：どの深さのノードが貢献するかを先に決めておく（深さフィルタ）。

4) “列挙せずに集計する”発想
* 文字列を生成（join）したり、prefixを列挙して辞書キーにしたりしない。
* ノードに蓄える（passcount / endcount / subtree_size …）→ ノード全走査で集計 or オンラインで都度加算。
* これで基本は O(総文字数) に落ちる。

5) よくある派生タスクとノード拡張の対応表
* 重複ありの正確な登録数 → endcount
* prefix本数 → passcount
* 辞書順K番目 → subtree_size を持って「左の合計 < K」を満たす子へ降りる
* Top-K候補 → ノードに小ヒープ（スコア付き）を持ち、挿入時に更新（Kが小さいときのみ）
* 削除 → insert の逆・0で掃除（ロジックが増えるだけで型は同じ）

この「ノードに“必要な集計値”を持たせて、insert/eraseで局所更新」という設計が、Trieを“汎用武器”に変えます。
今のあなたのクラスに、endcount と必要に応じて subtree_size を足すだけで、多くの問題に即応できますよ。

"""