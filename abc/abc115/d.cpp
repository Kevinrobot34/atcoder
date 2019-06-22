#include<cstdio>

long long int blength(long long int n) {
    return (1LL<<(n+2)) - 3;
}

long long int func(long long int n, long long int x) {
    if (n == 0) {
        if (x == 1) return 1;
        else return 0;
    }
    if (x <= 1 + blength(n-1)) {
        return func(n-1, x-1);
    } else {
        return ( (1LL<<(n+1)) - 1 ) - func(n, blength(n)-x);
    }
}
int main() {
    long long int n, x;

    scanf("%lld%lld", &n, &x);
    printf("%lld\n", func(n, x));

    return 0;
}
