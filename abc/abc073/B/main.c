#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int i, j, n, l, r, ans;

	// input
	scanf("%d\n", &n);

	// calc
	ans = 0;
	for (i = 0; i < n; i++) {
		scanf("%d %d\n", &l, &r);
		ans += r - l + 1;
	}
	
	// output
	printf("%d\n", ans);

	return 0;
}
