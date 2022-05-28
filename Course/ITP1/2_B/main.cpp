//
// AOJ ITP1 /2_B - Range
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_B


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

    // [ output ]
    if (a < b && b < c)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    // [ return ]
    return (0);
}
