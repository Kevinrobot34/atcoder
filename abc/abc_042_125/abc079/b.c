#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int a[1100];

int main(){
	int i, j, n, k;
	
	scanf("%d", &n);

	long long int a = 2, b = 1, c = 1;
	for (i = 1; i < n; i++) {
		c = a + b;
		a = b;
		b = c;
	}
	printf("%lld\n", c);

	return 0;
}
