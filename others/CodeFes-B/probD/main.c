#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define max(x, y) (((x) > (y))? (x) : (y))

char str[500005];
int  num[250005];

int main(){
	int i, j, n, m;
	int num[5];
	
	scanf("%d", &n);
	scanf("%s", str);
	str[n] = '0';

	int ans = 0;
	
	memset(num, 0, sizeof(int)*n)
	m = 0;
	for(i = 0; i < n+1; i++) {
		if (str[i] == '1') {
			num[(m%2)]++;
		} else {
			if (m % 2 == 0) {
				if (num[0] > 0) {
					m++;
				}
			} else {
				if (num[1] > 0) {
					//printf("i = %d : %d %d\n", i+1, num[0], num[1]);
					ans += max(num[0], num[1]);
					num[0] = 0;
					num[1] = 0;
				} else {
					num[0] = 0;
				}
				m++;
			}
		}
	}
	printf("%d\n", ans);


	return 0;
}
