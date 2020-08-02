#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main(){
	int i, j;
	char s[10];

	scanf("%s", s);

	j = 0;
	for (i = 0; i < 6; i++) {
		if (s[i] == '1') {
			j++;
		}
	}
	printf("%d\n", j);

	return 0;
}
