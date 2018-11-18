#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main(){
	int i, j, n, m, k;
	int ans = 0;
	int kuro;

	scanf("%d%d%d", &n, &m, &k);

	
	for (i = 0; i <= n; i++) {
		for (j = 0; j <= m; j++) {
			kuro = m*i + n*j - i*j*2;
			if (kuro == k) break;
		}
		if (kuro == k) break;
	}
	
	printf("%s\n", (i == n+1 && j == m+1) ? ("No") : ("Yes"));
	
	return 0;
}
