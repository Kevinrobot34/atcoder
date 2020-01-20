#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
    char a[10];

    scanf("%s", a);

    if (a[0] == a[1] || a[1] == a[2] || a[2] == a[3]) printf("Bad\n");
    else printf("Good\n");
    return 0;
}
