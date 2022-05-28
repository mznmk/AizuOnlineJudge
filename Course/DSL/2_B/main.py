#
# AOL DSL / 2_B Range Sum Query(RSQ)
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B

# tag: segment tree

# ---------------------------------------------------------------------------- #

class segment_tree:
    # [ constractor ]
    def __init__(self, n:int) -> None:
        # [ set parameter ]
        # set segment size
        size = 1
        while size < n+1:                   # 1-index
            size *= 2
        self.size = size
        # set segments
        self.segments = [0] * (size*2)      # 1-index
        # [ return ]
        return
    
    # [ add ]
    def add(self, index:int, value:int) -> None:
        # [ preprocessing ]
        # convert index -> proper index in segment tree
        index += self.size
        # [ add ]
        # add value to (leaf) segment
        self.segments[index] += value
        # update all segments
        while 42:
            # move to up-side segment
            index //= 2
            if index < 1:   # 1-index
                break
            # update segment
            self.segments[index] = self.segments[index*2] + self.segments[index*2+1]
        # [ return ]
        return

    # [ get sum ]
    def getsum(self, left:int, right:int) -> int:
        # [ preprocessing ]
        # convert index -> proper index i segment tree
        left += self.size
        right += self.size
        # [ get sum ]
        total_sum = 0
        while (left < right):
            # move left index to right-side segment
            if left % 2 == 1:
                total_sum += self.segments[left]
                left += 1
            left //= 2
            # move right index to left-side segment 
            if right % 2 == 1:
                total_sum += self.segments[right-1]
                right -= 1
            right //= 2
        # [ return ]
        return total_sum

def main():
    # [ input ]
    n, q = map(int, input().split())
    cxy = [list(map(int, input().split())) for _ in range(q)]

    # [ execute query ]
    st = segment_tree(n)
    for command, x, y in cxy:
        # query1: add(index, value)
        if command == 0:
            st.add(x, y)
        # query2: getsum(left, right+1)
        if command == 1:
            # [ output ]
            print( st.getsum(x, y+1) )

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
