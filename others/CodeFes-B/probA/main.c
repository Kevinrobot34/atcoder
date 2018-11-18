#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int i, j, n, m;
	char s[55];

	scanf("%s", s);

	for (i = 0; i < strlen(s) - 8; i++) {
		printf("%c", s[i]);
	}
	printf("\n");


	return 0;
}
