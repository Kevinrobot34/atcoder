#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    string t = "357";
    cin >> s;
    int x = stoi(s);

    int p3[15];
    p3[0] = 1;
    for (int i = 1; i <= s.size(); i++) p3[i] = p3[i-1] * 3;

    int ans = 0;
    for (int n = 0; n < p3[s.size()]; n++) {
      string s2
    }

    printf("%d\n", ans);
    return 0;
}
