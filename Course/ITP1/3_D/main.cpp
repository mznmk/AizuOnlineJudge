//
// AOJ ITP1 / 3_D - How Many Divisors ?
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_3_D

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); i++)
using ll = long long;

int main()
{
    // [ input ]
    int a, b, c;
    cin >> a >> b >> c;

    // [ find number of divisors ]
    int divs = 0;
    rep(v, a, b+1) {
        if (c % v == 0)
            divs++;
    }

    // [ output ]
    cout << divs << endl;

    // [ return ]
    return (0);
}
