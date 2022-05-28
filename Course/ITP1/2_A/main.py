#
# AOJ ITP1 / 2_A - Small.Large, or Equal
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_A

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    a, b = map(int, input().split())

    # [ output ]
    if a < b:
        print("a < b")
    elif a > b:
        print("a > b")
    elif a == b:
        print("a == b")

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
