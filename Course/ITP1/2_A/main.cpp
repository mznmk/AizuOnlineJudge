//
// AOJ ITP1 / 2_A - Small.Large, or Equal
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_A

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); i++)
using ll = long long;

int main()
{
    // [ input ]
    int a, b;
    cin >> a >> b;

    // [ output ]
    if (a < b)
        cout << "a < b" << endl;
    else if (a > b)
        cout << "a > b" << endl;
    else if (a == b)
        cout << "a == b" << endl;

    // [ return ]
    return (0);
}
