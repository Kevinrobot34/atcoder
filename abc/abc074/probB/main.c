#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int i,j;
	int n, k, x, a, b, ans;
	
	scanf("%d", &n);
	scanf("%d", &k);
	
	ans = 0;
	for(i = 0; i < n; i++){
		scanf("%d", &x);
		a = x * 2;
		b = (k - x) * 2;
		b = ((b > 0) ? b : (-b));

		ans += ((a < b) ? a : b);
	}

	printf("%d\n", ans);

	return 0;
}
