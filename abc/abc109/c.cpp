#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int main() {
    int n, x;
    vector<int> a, b;

    scanf("%d%d", &n, &x);
    a.push_back(x);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        a.push_back(x);
    }

    sort(a.begin(), a.end());
    int ans = a[1] - a[0];
    for (int i = 2; i < a.size(); i++) {
        ans = gcd(ans, a[i] - a[i-1]);
    }
    printf("%d\n", ans);

    return 0;
}
