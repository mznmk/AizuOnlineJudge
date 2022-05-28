#
# AOL DSL / 2_A - Range Minimum Query (RMQ)
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A

# tag: segment tree

# ---------------------------------------------------------------------------- #

import sys
sys.setrecursionlimit(10**9)

class segment_tree:
    # [ const variable ]
    INF = (1<<31)-1

    # [ constractor ]
    def __init__(self, n:int) -> None:
        # [ set parameter ]
        # set segment size
        size = 1
        while size < n+1:                       # 1-index
            size *= 2
        self.size = size
        # set segments
        self.segments = [self.INF] * (size*2)   # 1-index
        # [ return ]
        return

    # [ update ]
    def update(self, index:int, value:int) -> None:
        # [ preprocessing ]
        # convert index -> proper index in segment tree
        index += self.size
        # [ update ]
        # update value to (leaf) segment
        self.segments[index] = value
        # update all segments
        while 42:
            # move to up-side segment
            index //= 2
            if index < 1:   # 1-index
                break
            # update segment (minimum value)
            self.segments[index] \
                = min(self.segments[index*2], self.segments[index*2+1])
        # [ return ]
        return

    # [ find ]
    def find(self, q_left:int, q_right:int,
                    seg_left:int = 0, seg_right:int = None, index:int = 1):
        if seg_right == None:
            seg_right = self.size
        """
        [ case 1 ]
        segment:       ===== | =====
        query  : =====       |       =====
        --> return INF
        """
        if q_right <= seg_left or seg_right <= q_left:
            return self.INF
        """
        [ case 2 ]
        segment:   =====
        query  : =========
        --> return this segment
        """
        if q_left <= seg_left and seg_right <= q_right:
            return self.segments[index]
        """
        [ case 3 ]
        segment:   ===== | =====
        query  : =====   |   =====
        --> recursive ( left-side / right-side )
        """
        seg_mid = (seg_left + seg_right) // 2
        min_left = self.find(q_left, q_right, seg_left, seg_mid, index*2)
        min_right = self.find(q_left, q_right, seg_mid, seg_right, index*2+1)
        return min(min_left, min_right)

def main():
    # [ input ]
    n, q = map(int, input().split())
    cxy = [list(map(int, input().split())) for _ in range(q)]

    # [ execute query ]
    st = segment_tree(n)
    for command, x, y in cxy:
        # query1: update(index, value)
        if command == 0:
            st.update(x, y)
        # query2: find(left, right+1)
        if command == 1:
            print( st.find(x, y+1))

    # [ output ]

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
