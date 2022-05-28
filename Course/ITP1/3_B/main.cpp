//
// AOJ ITP1 / 3_B - Print Test Cases
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_3_B

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); i++)
using ll = long long;

int main()
{
    // [ input ]
    int i = 1;
    while (42) {
        // input
        int x;
        cin >> x;
        if (x == 0)
            break;
        // [ output ]
        printf("Case %d: %d\n", i, x);
        // increment index
        i++;
    }

    // [ return ]
    return (0);
}
