#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int R, G;
	
	scanf("%d%d", &R, &G);

	printf("%d\n", R + (G-R)*2);

	return 0;
}
