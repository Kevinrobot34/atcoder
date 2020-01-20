#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int table[305][305];
int main(){
	int i,j;
	int n;

	scanf("%d", &n);
	for (i = 0; i < n; i++) for (j = 0; j < n; j++) scanf("%d", &table[i][j]);

	return 0;
}
