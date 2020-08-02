#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int i, j, n, a, b, a_min, b_min;

	scanf("%d", &n);

	scanf("%d%d", &a_min, &b_min);
	for (i = 1; i < n; i++) {
		scanf("%d%d", &a, &b);
		
		if (a > a_min) {
			a_min = a;
			b_min = b;
		}
	}
	printf("%d\n", a_min + b_min);

	return 0;
}
