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

long long int gcd(long long int a, long long int b) {
    if (a == 0) return b;
    else return gcd(b%a, a);
}

int main() {
    long long int n, a, b;

    scanf("%lld", &n);
    scanf("%lld", &a);
    for (int i = 1; i < n; i++) {
        scanf("%lld", &b);
        a = gcd(a, b);
    }

    printf("%lld\n", a);

    return 0;
}
