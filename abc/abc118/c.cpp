#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<queue>
#include<numeric>
#include<map>
#include<string>

using namespace std;

long long int a[100005];
int main() {
    long long int n;
    queue<long long int> q;

    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
        q.push(a[i]);
    }

    long long int am = q.front();

    while (!q.empty()) {
        long long int b = q.front();
        q.pop();

        if (b % am != 0) {
            q.push(b % am);
            am = b % am;
            for (int i = 0; i < n; i++) {
                if (a[i] % am != 0) {
                    q.push(a[i] % am);
                }
            }
        }
    }

    printf("%lld\n", am);

    return 0;
}
