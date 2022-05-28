#
# AOL DSL / 5_B The Maximum Number of Overlaps
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/5/DSL_5_B

# tag: prefix sum
# tag: imos method

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    n = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(n)]
    
    # [ const variables ]
    H, W = 1000+1, 1000+1       # 0 -> 1000

    # [ simulate ! ]
    # create imos table
    dp = [[0] * W for _ in range(H)]
    # simulate
    for x1, y1, x2, y2 in rectangles:
        dp[y1][x1] += 1
        dp[y2][x2] += 1
        dp[y1][x2] -= 1
        dp[y2][x1] -= 1
    # prefix sum (left->right)
    for i in range(0, H):
        for j in range(1, W):
            dp[i][j] += dp[i][j-1]
    # prefix sum (top->bottom)
    for j in range(0, W):
        for i in range(1, H):
            dp[i][j] += dp[i-1][j]
    # find "max_overlaps"
    max_overlaps = 0
    for i in range(0, H):
        for j in range(0, W):
            max_overlaps = max(dp[i][j], max_overlaps)

    # # [ for debug ]
    # for row in dp:
    #     print(row)

    # [ output ]
    print(max_overlaps)

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
