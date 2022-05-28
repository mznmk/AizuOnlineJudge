#
# AOJ GRL / 2_A Minimum Spanning Tree
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

# tag; graph theory
# tag: minimum spanning tree
# tag: kruskal's algorithm
# tag: union find
# tag: disjoint set union

# ---------------------------------------------------------------------------- #

import sys
sys.setrecursionlimit(10**9)

class UnionFind:
    # [[ constractor ]]
    def __init__(self, n:int) -> None:
        self.n = n
        self.root = [-1] * n
        self.rank = [1] * n
        self.weight = [0] * n

    # [[ union (merge) ]] -> "merge" at atcoder library
    def unite(self, x:int, y:int, w:int = 1) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        # same tree ?
        if rx == ry:
            # [ return ]
            return False        # fail to unite
        # [ unite tree ]
        # calc weight
        w -= self.weight[x]
        w += self.weight[y]
        # avoid depth deeper (marge technique)
        if self.rank[rx] > self.rank[ry]:
            rx, ry = ry, rx
            w *= -1
        elif self.rank[rx] == self.rank[ry]:
            self.rank[ry] += 1
        # update size
        self.root[ry] += self.root[rx]
        # unite tree
        self.root[rx] = ry      # x: new child / y: new parent
        # update weight
        self.weight[rx] = w
        # [ return ]
        return True             # success to unite

    # [[ find (leader) ]] -> "leader" at atcoder library
    def find(self, x:int) -> int:
        if self.root[x] < 0:
            # need not to find parent (parent->self)
            # [ return ]
            return x
        else:
            # need to find parent (recursive)
            r = self.find(self.root[x])
            self.weight[x] += self.weight[self.root[x]]     # update weight
            self.root[x] = r
            # [ return ]
            return self.root[x]

    # [[ size ]]
    def size(self, x:int) -> int:
        # [ return ]
        return -self.root[self.find(x)]

    # [[ depth ]]
    def depth(self, x:int) -> int:
        # [ return ]
        return self.rank[self.find(x)]

    # [[ same ]]
    def same(self, x:int, y:int) -> bool:
        # [ return ]
        return self.find(x) == self.find(y)

    # [[ diff weight ]]
    def diff(self, x:int, y:int) -> int:
        # [ return ]
        return self.weight[x] - self.weight[y]

    # [[ groups ]]
    def groups(self) -> list:
        groups = [[] for _ in range(self.n)]
        for i in range(self.n):
            groups[self.find(i)].append(i)
        # [ return ]
        return groups

def main():
    # [ input ]
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]

    # [ find minimum cost ]
    uf = UnionFind(v)
    edges.sort(key=lambda x:x[2])
    min_cost = 0
    for s, t, w in edges:
        # already linded ?
        if not uf.same(s, t):
            # link "s" with "t"
            uf.unite(s, t)
            # update "min_cost"
            min_cost += w

    # [ output ]
    print(min_cost)

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
