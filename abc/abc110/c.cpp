#include <cstdio>
#include <cstring>
#include <vector>
#define MAX 200005
using namespace std;

char s[MAX], t[MAX];

int main() {
    scanf("%s", s);
    scanf("%s", t);
    int n = strlen(s);
    int ans;

    vector<int> m[30];
    for (int i = 0; i < n; i++) {
        m[s[i] - 'a'].push_back(i);
    }
    int i = 0;
    for (; i < 26; i++) {
        if (m[i].size() == 0) continue;

        char tmp = t[m[i][0]];
        int j = 0;
        for (; j < m[i].size(); j++) {
            if (tmp != t[m[i][j]]) break;
        }
        if (j != m[i].size()) break;
    }
    if (i == 26) ans = 1;
    else ans = 0;

    vector<int> mm[30];
    for (int i = 0; i < n; i++) {
        mm[t[i] - 'a'].push_back(i);
    }
    i = 0;
    for (; i < 26; i++) {
        if (mm[i].size() == 0) continue;

        char tmp = s[mm[i][0]];
        int j = 0;
        for (; j < mm[i].size(); j++) {
            if (tmp != s[mm[i][j]]) break;
        }
        if (j != mm[i].size()) break;
    }
    if (i == 26) ans *= 1;
    else ans *= 0;

    printf("%s\n", (ans==1) ? "Yes" : "No");

    return 0;
}
