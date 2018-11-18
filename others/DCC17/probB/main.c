#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int i, j, n, m;
	int a,b,c,d;

	scanf("%d%d%d%d", &a, &b, &c, &d);

	printf("%d\n", a*1728 + b*144 + c*12 + d);

	return 0;
}
