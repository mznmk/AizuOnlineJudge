//
// AOJ ITP1 / 2_C - Sorting Three Numbers
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_2_C

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); i++)
using ll = long long;

int main()
{
    // [ input ]
    int n = 3;
    vector<int> a(n);
    rep(i, 0, n) cin >> a[i]; 

    // [ output ]
    sort(a.begin(), a.end());
    rep(i, 0, n) {
        cout << a[i]; 
        if (i != n-1)
            cout << " ";
        else
            cout << endl;
    }

    // [ return ]
    return (0);
}
