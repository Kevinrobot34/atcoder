#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

long long int a[100005];
int b[100005];
int dp[]

int main(){
	int i, j;
	int n, k;

	scanf("%d%d", &n, &k);
	for (i = 0; i < n; i++) {
		scanf("%lld%d", &a[i], &b[i]);
		printf("%lld %d\n", a[i], b[i]);
	}

	

	return 0;
}
