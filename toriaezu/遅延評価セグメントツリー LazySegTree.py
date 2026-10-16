
# https://atcoder.jp/contests/awc0014/tasks/awc0014_e
# 区間加算（更新）、区間和の 2 つの操作ができる形。

from atcoder.lazysegtree import LazySegTree
import sys

def op(x, y):
    # x, y = (sum, size)
    return (x[0] + y[0], x[1] + y[1])

e = (0, 0)

def mapping(f, x):
    # f = 加算量
    # 区間長が x[1] なので、区間和は f * x[1] だけ増える
    return (x[0] + f * x[1], x[1])

def composition(f, g):
    # 先に g をやって、その後に f をやる
    # 加算どうしなので足せばよい
    return f + g

id_ = 0

def main():
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    # 各要素を (値, 区間長=1) にして持つ
    A = [(c, 1) for c in C]

    seg = LazySegTree(op, e, mapping, composition, id_, A)

    ans = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, l, r, v = query
            seg.apply(l - 1, r, v)
        else:
            _, l, r = query
            ans.append(str(seg.prod(l - 1, r)[0]))

    print("\n".join(ans))

if __name__ == "__main__":
    main()