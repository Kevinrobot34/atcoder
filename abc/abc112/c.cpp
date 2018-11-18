#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int n;
    int x[101], y[101], h[101];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d%d%d", &x[i], &y[i], &h[i]);

    for (int cx = 0; cx < 101; cx++) {
        for (int cy = 0; cy < 101; cy++) {
            int H_max = 2000000000;
            int H_cand = -1;
            int i = 0;
            for (; i < n; i++) {
                int dist = abs(x[i]-cx) + abs(y[i]-cy);
                if (h[i] == 0) {
                    H_max = min(H_max, dist);
                } else {
                    if (H_cand == -1) {
                        H_cand = dist + h[i];
                    } else if (H_cand != dist + h[i]) {
                        break;
                    }
                }
            }

            if (i == n && H_cand <= H_max && H_cand > 0) {
                printf("%d %d %d\n", cx, cy, H_cand);
                return 0;
            }
        }
    }
    return 0;
}
