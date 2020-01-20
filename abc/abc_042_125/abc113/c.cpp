#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

struct Town {
    int p, y, i;
};
bool cmp1(const Town &a, const Town &b) {
    if (a.p == b.p) return (a.y < b.y);
    else return (a.p < b.p);
}
bool cmp2(const Town &a, const Town &b) {
    return (a.i < b.i);
}

int main() {
    int n, m, p, y;
    vector<Town> towns;

    scanf("%d%d", &n, &m);

    for (int i = 0; i < m; i++) {
        scanf("%d%d", &p, &y);
        towns.push_back((Town){p,y,i});
    }


    sort(towns.begin(), towns.end(), cmp1);

    int p_cur = 0;
    int x = 1;
    for (int i = 0; i < m; i++) {
        if (towns[i].p == p_cur) {
            x++;
        } else {
            x = 1;
            p_cur = towns[i].p;
        }
        towns[i].y = x;
    }

    sort(towns.begin(), towns.end(), cmp2);
    for (int i = 0; i < m; i++) {
        printf("%06d%06d\n", towns[i].p, towns[i].y);
    }
    return 0;
}
