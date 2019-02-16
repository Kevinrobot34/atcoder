#include <cstdio>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

int a[2][100000+5];
int main() {
    int n;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i%2][(int)(i/2)]);

    vector< pair<int,int> > tmp[2];
    for (int i = 0; i < 2; i++) {
        sort(a[i], a[i] + n/2);
        //for (int j = 0; j < n/2; j++) printf("%d\n", a[i][j]);

        int c = 0;
        int m = a[i][0];
        for (int j = 0; j <= n/2; j++) {
            if (j == n/2) {
                tmp[i].push_back(make_pair(c, m));
            }else if (m != a[i][j]) {
                tmp[i].push_back(make_pair(c, m));
                m = a[i][j];
                c = 1;
            } else {
                c++;
            }
        }

        sort(tmp[i].begin(), tmp[i].end(), greater< pair<int,int> >());
        //printf("1st - %d %d\n", tmp[i][0].first, tmp[i][0].second);
        //printf("2nd - %d %d\n", tmp[i][1].first, tmp[i][1].second);
    }

    int ans;
    if (tmp[0][0].second != tmp[1][0].second) {
        ans = n - tmp[0][0].first - tmp[1][0].first;
    } else {
        ans = n;
        if (tmp[0].size() == 1 && tmp[1].size() == 1) {
            ans = n/2;
        } else {
            for (int i = 0; i < 2; i++) {
                if (tmp[i].size() == 1) continue;
                for (int j = 1; j < tmp[i].size(); j++) {
                    if (tmp[i][j].second != tmp[(i+1)%2][0].second) {
                        ans = min(ans, n - tmp[(i+1)%2][0].first - tmp[i][j].first);
                        break;
                    }
                }
            }
        }
    }
    printf("%d\n", ans);
    return 0;
}
