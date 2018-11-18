#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<queue>
#include<numeric>
#include<map>
using namespace std;


int main(){
	int a[5], b[5];

	for (size_t i = 0; i < 3; i++) {
		scanf("%d", &a[i]);
	}
	for (size_t i = 0; i < 3; i++) {
		b[i] = abs(a[(i+1)%3] - a[i]);
	}

	int ans = accumulate(b, b+3, 0);
	//ans -= *max_element(b, b+3);
	ans -= max(b, b+3);
	printf("%d\n", ans);

	return 0;
}
