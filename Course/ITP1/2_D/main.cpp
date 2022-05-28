//
// AOJ ITP1 / 2_D - Circle in a Rectangle
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_D

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); i++)
using ll = long long;

int main()
{
    // [ input ]
    int w, h, x, y, r;
    cin >> w >> h >> x >> y >> r;

    // [ output ]
    if ((r <= x && x <= w-r) && (r <= y && y <= h-r))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    // [ return ]
    return (0);
}
