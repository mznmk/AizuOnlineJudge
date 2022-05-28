#
# AOJ ITP1 / 3_C - Swapping Two Numbers
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_3_C

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    xy = []
    n = 0
    while 42:
        # input
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        xy.append([x, y])
        # update data count
        n += 1

    # [ output ]
    for i in range(n):
        # swap
        if xy[i][0] > xy[i][1]:
            xy[i][0], xy[i][1] = xy[i][1], xy[i][0]
        # output
        print("%d %d" % (xy[i][0], xy[i][1]))

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
