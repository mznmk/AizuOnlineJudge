//
// AOJ ITP1 / 3_C - Swapping Two Numbers
//
// https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_3_C

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); i++)
using ll = long long;

int main()
{
    // [ input ]
    vector<pair<int,int>> xy;
    int n = 0;
    while (42) {
        // input
        int x, y;
        cin >> x >> y;
        if (!x && !y)
            break;
        xy.push_back({x, y});
        // update data count
        n++;
    }

    // [ output ]
    rep(i, 0, n) {
        // swap
        if (xy[i].first > xy[i].second)
            swap(xy[i].first, xy[i].second);
        // output
        printf("%d %d\n", xy[i].first, xy[i].second);
    }

    // [ return ]
    return (0);
}
