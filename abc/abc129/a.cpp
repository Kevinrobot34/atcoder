#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
    int a, b, c;

    scanf("%d%d%d", &a, &b, &c);

    printf("%d\n", a+b+c - max(a, max(b, c)));

    return 0;
}
