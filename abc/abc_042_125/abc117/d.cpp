#include<cstdio>
#include<algorithm>

using namespace std;

long long int a[100005], a_sum;
int m[100], n;

long long int digit2(long long int x) {
    int digit = 0;
    while (x > 1) {
        digit++;
        x = x / 2;
    }
    return digit;
}

long long int solve(long long int x){
    if (x == 0) return a_sum;

    long long int x_digit = digit2(x);
    //printf("%lld %lld\n", x, x_digit);
    long long int a = solve(x - ((long long int)1<<x_digit));
    a += ((long long int)1<<x_digit) * max(0, (n-m[x_digit]) - m[x_digit]);

    long long int b = a_sum;
    for (int i = 0; i < x_digit; i++) {
        b += ((long long int)1<<i) * max(0, (n-m[i]) - m[i]);
    }

    //printf("%lld %lld %lld\n", x, a, b);
    return max(a, b);
}
int main() {
    long long int k;

    scanf("%d%lld", &n, &k);
    long long int k_digit = digit2(k);


    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
        a_sum += a[i];
        for (int j = 0; j <= k_digit; j++) m[j] += (a[i]>>j) & 1;
    }
    //printf("%lld\n", a_sum);

    //for (int j = 0; j <= k_digit; j++) printf("%d ", m[j]);
    //printf("\n");

    //printf("%lld, %lld\n", k_digit, (long long int)1 << k_digit);

    printf("%lld\n", solve(k));

    return 0;
}
