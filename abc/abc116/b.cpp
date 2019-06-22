#include<cstdio>
#include<map>
using namespace std;

int func(int n) {
    if (n % 2 == 0) return n / 2;
    else return 3 * n + 1;
}

int main() {
    int s, n;
    map<int, int> d;

    scanf("%d", &s);

    n = 1;
    while (d.count(s) == 0) {
        d[s] = n;
        s = func(s);
        n++;
    }

    printf("%d\n", n);

    return 0;
}
