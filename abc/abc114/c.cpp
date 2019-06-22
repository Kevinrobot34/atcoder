#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

int main() {
    string s;
    string t = "357";
    cin >> s;
    int x = stoi(s);

    int ans = 0;
    if (s.length() >= 4) {
        for (int i = 0; i < s.length() - 3; i++) {

        }
    } else {
        if (x < 357) ans = 0;
        else if (x < 375) ans = 1;
        else if (x < 537) ans = 2;
        else if (x < 573) ans = 3;
        else if (x < 735) ans = 4;
        else if (x < 753) ans = 5;
        else ans = 6;
    }

    printf("%d\n", ans);
    return 0;
}
