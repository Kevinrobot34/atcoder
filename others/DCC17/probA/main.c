#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int i, j, n, m;
	char str[10];

	scanf("%s", str);

	if (str[0] == str[1] && str[1] != str[2] && str[2] == str[3]) printf("Yes\n");
	else printf("No\n");

	return 0;
}
