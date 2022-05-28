#
#  AOJ ITP1 / 2_C - Sorting Three Numbers
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_C

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    n = 3
    a = list(map(int, input().split()))

    # [ output ]
    a.sort()
    print(*a)

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
