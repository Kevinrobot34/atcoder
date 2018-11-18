#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int main(){
	int n;

	scanf("%d", &n);
	if(n % 10 == 9 || n / 10 == 9){
		printf("Yes\n");
	}else{
		printf("No\n");
	}

	return 0;
}
