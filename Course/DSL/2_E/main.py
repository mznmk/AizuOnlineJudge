#
# AOL DSL / 2_E - Range Add Query (RAQ)
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_E

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
    def add(self, left:int, right:int, value:int) -> None:
        # [ preprocessing ]
        # convert index -> proper index i segment tree
        left += self.size
        right += self.size
        # [ add ]
        while (left < right):
            # move left index to right-side segment
            if left % 2 == 1:
                self.segments[left] += value
                left += 1
            left //= 2
            # move right index to left-side segment 
            if right % 2 == 1:
                self.segments[right-1] += value
                right -= 1
            right //= 2
        # [ return ]
        return

    # [ get ]
    def get(self, index:int) -> int:
        # [ preprocessing ]
        # convert index -> proper index in segment tree
        index += self.size
        # [ get one ]
        total_sum = self.segments[index]    # leaf segment
        while 42:
            # move to up-side segment
            index //= 2
            if index < 1:   # 1-index
                break
            total_sum += self.segments[index]
        # [ return ]
        return total_sum

def main():
    # [ input ]
    n, q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(q)]

    # [ execute query ]
    st = segment_tree(n)
    for i in range(q):
        command = query[i][0]
        # query1: add(left, right+1, value)
        if command == 0:
            left = query[i][1]
            right = query[i][2]
            value = query[i][3]
            st.add(left, right+1, value)
        # query2: get(index)
        if command == 1:
            index = query[i][1]
            # [ output ]
            print( st.get(index) )

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
