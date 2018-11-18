#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int a[1100];

int main(){
	int i, j, n, k;
	
	scanf("%d%d", &n, &k);

	int ans = 1;
	for (i = 0; i < n; i++) {
		if (ans < k) ans = ans*2;
		else ans += k;
	}
	printf("%d\n", ans);

	return 0;
}
