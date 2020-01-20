#include<cstdio>
#include<cstdlib>
#include<map>
using namespace std;

int a[100005], b[100005], num;

int main(){
	int n;
	map<int, int> d;

	scanf("%d", &n);
	while (n--) {
		int a;
		scanf("%d", &a);
		if (d.count(a) == 0) {
			d[a] = 1;
		} else {
			d[a]++;
		}
	}

	int ans = 0;
	for (auto a: d) {
		if (a.second % 2 == 1) ans++;
	}
	printf("%d\n", ans);

	return 0;
}
