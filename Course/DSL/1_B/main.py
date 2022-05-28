#
# AOL DSL / 1_B Weighted Union Find Trees
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B

# ---------------------------------------------------------------------------- #

class UnionFind:
    # [[ constractor ]]
    def __init__(self, n:int) -> None:
        self.n = n
        self.root = [-1] * n
        self.rank = [1] * n
        self.weight = [0] * n

    # [[ union ]]
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
        """
        w :           :from "X" to "Y"
        x :  weight[x]: from "X" to "X's root"
        r :           :from "X's root" to "Y's root"
        y : -weight[y]:from "Y'x root" to "Y"
        --------------------------------------------
        w = x + r + y
        r = w - x - y
        """
        # [ return ]
        return True             # success to unite

    # [[ find ]]
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

def main():
    # [ input ]
    n, q = map(int, input().split())
    queries = [input() for _ in range(q)]

    # [ execute query ]
    uf = UnionFind(n)
    for query in queries:
        cmd = query[0]
        # query1: relate(x,y,z)
        if cmd == "0":
            _, x, y, z = map(int, query.split())
            uf.unite(x, y, z)
        # query2: diff(x,y)
        if cmd == "1":
            _, x, y = map(int, query.split())
            # [ output ]
            if uf.same(x, y):
                print(uf.diff(x, y))
            else:
                print("?")

    # # [ for debug ]
    # print( uf.root )
    # print( uf.rank )
    # print( uf.weight )

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
