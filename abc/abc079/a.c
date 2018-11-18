#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	char s[8];
	
	scanf("%s", s);

	if (s[0] == s[1] && s[1] == s[2]) {
		printf("Yes\n");
	} else if (s[1] == s[2] && s[2] == s[3]) {
		printf("Yes\n");
	} else {
		printf("No\n");
	}

	return 0;
}
