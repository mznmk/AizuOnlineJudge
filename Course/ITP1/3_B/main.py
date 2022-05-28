#
# AOJ ITP1 / 3_B - Print Test Cases
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_3_B

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    i = 1
    while 42:
        # input
        x = int(input())
        if x == 0:
            break
        # [ output ]
        print("Case %d: %d" % (i, x))
        # increment index
        i += 1

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
