#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<queue>
#include<numeric>
#include<map>
#include<string>

using namespace std;

string max_string(string a, string b) {
    if (a.length() > b.length()) {
        return a;
    } else if (a.length() < b.length()) {
        return b;
    } else {
        for (int i = 0; i < a.length(); i++) {
            if (a[i] > b[i]) return a;
            else if (a[i] < b[i]) return b;
        }
        // 一致
        return a;
    }
}

int mm[10] = {0, 2, 5 ,5, 4, 5, 6, 3, 7, 6};
int a[15];
string dp[11000];
int main() {
    int n, m;

    scanf("%d%d", &n, &m);

    for (int i = 0; i < m; i++) {
        scanf("%d", &a[i]);
    }

    for (int i = 0; i < m; i++) {
        if (dp[mm[a[i]]] == "") dp[mm[a[i]]] = to_string(a[i]);
        else dp[mm[a[i]]] = max_string(dp[mm[a[i]]], to_string(a[i]));
    }

    for (int i = 1; i <= n; i++) {
        if (dp[i] == "") continue;

        for(int j = 0; j < m; j++) {
            if (dp[i + mm[a[j]]] == "") dp[i + mm[a[j]]] = to_string(a[j]) + dp[i];
            else dp[i + mm[a[j]]] = max_string(dp[i + mm[a[j]]], to_string(a[j]) + dp[i]);
        }
    }

    printf("%s\n", dp[n].c_str());

    return 0;
}
