//#include<bits/stdc++.h>
#include<cstdio>
using namespace std;

int main(){
	int n, x, ans;

	scanf("%d", &n);

	ans = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		ans += x;
	}
	ans -= n;

	printf("%d\n", ans);

	return 0;
}
