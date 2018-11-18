#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main(){
	int i, j, n, m;
	char str[20];
	char key[5] = "YAKI";

	scanf("%s", str);

	for (i = 0; i < 4; i++) {
		if (str[i] != key[i])break;
	}
	printf("%s\n", (i == 4) ? ("Yes") : ("No"));

	return 0;
}
