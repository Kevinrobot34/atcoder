#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
    int n, l;

    scanf("%d%d", &n, &l);

    int sum = n*(l-1) + n*(n+1)/2;
    int ans = sum;
    int x = abs(sum);
    for (int i = 1; i <= n; i++) {
      if (x > abs((l+i-1))) {
        x = abs((l+i-1));
        ans = sum - (l+i-1);
      }
    }
    printf("%d\n", ans);
    return 0;
}
