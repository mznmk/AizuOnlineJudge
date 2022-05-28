#
# AOJ ITP1 / 2_D - Circle in a Rectangle
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_D

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    w, h, x, y, r = map(int, input().split())

    # [ output ]
    if r <= x <= w-r and r <= y <= h-r:
        print("Yes")
    else:
        print("No")

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
