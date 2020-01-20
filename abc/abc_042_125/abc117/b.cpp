#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
    int n, l;
    int m, s;

    scanf("%d", &n);
    m = s = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &l);
        s += l;
        m = max(m, l);
    }

    printf("%s\n", (m < s-m) ? "Yes" : "No");

    return 0;
}
