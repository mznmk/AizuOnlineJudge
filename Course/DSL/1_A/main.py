#
# AOJ DSL / 1_A Disjoint set: Union Find Tree
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A

# tag: union find

# ---------------------------------------------------------------------------- #

class union_find:
    # [ constractor ]
    def __init__(self, n:int) -> None:
        self.n = n
        self.parents = [-1] * n
        self.ranks = [1] * n
    # [ find ]
    def find(self, x:int) -> int:
        if self.parents[x] == -1:
            # parent -> self
            return x
        else:
            # find parent (recursive)
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    # [ union ]
    def unite(self, x:int, y:int) -> None:
        x = self.find(x)
        y = self.find(y)
        # same tree ?
        if x == y:
            return
        # union tree
        # avoid depth deeper
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        elif self.ranks[x] == self.ranks[y]:
            self.ranks[y] +=1
        # x: new child / y: new parent
        self.parents[x] = y

def main():
    # input
    n, q = map(int, input().split())
    pab = [list(map(int, input().split())) for _ in range(q)]

    # execute query
    uf = union_find(n)
    for i in range(q):
        p = pab[i][0]
        a = pab[i][1]
        b = pab[i][2]
        # query1: union
        if p == 0:
            uf.unite(a, b)
        # query2: judge
        if p == 1:
            if uf.find(a) == uf.find(b):
                print(1)
            else:
                print(0)

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
