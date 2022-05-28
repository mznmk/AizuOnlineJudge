#
# AOJ ITP1 / 3_D - How Many Divisors ?
#
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_3_D

# ---------------------------------------------------------------------------- #

def main():
    # [ input ]
    a, b, c = map(int, input().split())

    # [ find number of divisors ]
    divs = 0
    for v in range(a, b+1):
        if c % v == 0:
            divs += 1

    # [ output ]
    print(divs)

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()
