#
# AOL DSL / 5_A The Maximum Number of Customers
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/5/DSL_5_A

# tag: prefix sum
# tag: imos method

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    n, t = map(int, input().split())
    customer = [list(map(int, input().split())) for _ in range(n)]

    # [ simulate ! ]
    # create imos table
    dp = [0] * (t+1)
    # simulate
    for l, r in customer:
        dp[l] += 1
        dp[r] -= 1
    max_customer = dp[0]
    for i in range(1, t+1):
        dp[i] += dp[i-1]
        max_customer = max(dp[i], max_customer)

    # # [ for debug ]
    # print(dp)

    # [ output ]
    print(max_customer)

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
