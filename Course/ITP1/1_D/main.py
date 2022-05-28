#
# AOJ ITP1 / 1_D - Watch
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_1_D

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    s = int(input())

    # [ calc time ]
    h = s // 3600
    s -= 3600 * h
    m = s // 60
    s -= 60 * m

    # [ output ]
    print( f'{h}:{m}:{s}' )

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
