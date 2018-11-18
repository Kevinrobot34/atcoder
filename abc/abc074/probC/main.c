#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX(x,y) ((x>y)?(x):(y))
#define Min(x,y) ((x<y)?(x):(y))

double dp[3005];
int sugar[3005];
int main(){
	int i,j;
	int a, b, c, d, e, f;

	scanf("%d%d%d%d%d%d", &a, &b, &c, &d, &e, &f);

	for (i = 0; i <=f; i++) dp[i] = -1.0;
	dp[100*a] = 0.0;
	sugar[100*a] = 0;
	if (100*b <= f) {
		dp[100*b] = 0.0;
		sugar[100*b] = 0;
	}
	
	for (i = 0; i <= f; i++) {
		if (dp[i] == -1.0) continue;
		
		// water : + 100A
		if (i + 100*a <= f &&
		    dp[i + 100*a] <  100 * (double)sugar[i] / (double)(i + 100*a)) {
			dp[i + 100*a] = 100 * (double)sugar[i] / (double)(i + 100*a);
			sugar[i + 100*a] = sugar[i];
		}
		// water : + 100B
		if (i + 100*b <= f &&
		    dp[i + 100*b] <  100 * (double)sugar[i] / (double)(i + 100*b)) {
			dp[i + 100*b] = 100 * (double)sugar[i] / (double)(i + 100*b);
			sugar[i + 100*b] = sugar[i];
		}
		// sugar : +c
		if (i + c <= f &&
		    dp[i + c] < 100 * (double)(sugar[i] + c) / (double)(i + c) && 
		    e * (i - sugar[i]) >= (sugar[i] + c) * 100) {
			dp[i + c] = 100 * (double)(sugar[i] + c) / (double)(i + c);
			sugar[i + c] = sugar[i] + c;
		}
		// sugar : +d
		if (i + d <= f &&
		    dp[i + d] < 100 * (double)(sugar[i] + d) / (double)(i + d) && 
		    e * (i - sugar[i]) >= (sugar[i] + d) * 100) {
			dp[i + d] = 100 * (double)(sugar[i] + d) / (double)(i + d);
			sugar[i + d] = sugar[i] + d;
		}
	}

	int ans_w, ans_s;
	double ans_p;
	ans_p = 0.0;
	ans_w = 100*a;
	ans_s = 0;
	for (i = 100*a + 1; i <= f; i++) {
		if (ans_p < dp[i]) {
			ans_s = sugar[i];
			ans_w = i - sugar[i];
			ans_p = dp[i];
		}
	}
	
	printf("%d %d\n", ans_w+ans_s, ans_s);

	return 0;
}
