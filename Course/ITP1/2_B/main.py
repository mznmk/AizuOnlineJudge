#
# AOJ ITP1 / 2_B - Range
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_B

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    a, b, c = map(int, input().split())

    # [ output ]
    if (a < b < c):
        print("Yes")
    else:
        print("No")

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
