#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int x = (s[0]-'0')*100 + (s[1]-'0')*10 + (s[2]-'0');
    int y = 753;

    int ans = abs(x - y);
    for (int i = 3; i < s.length(); i++) {
        x = (x%100)*10 + (s[i]-'0');
        ans = min(ans, abs(x-y));
    }

    printf("%d\n", ans);
    return 0;
}
