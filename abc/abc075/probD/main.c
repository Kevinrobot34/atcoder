#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int a[100005], b[100005], num;

int main(){
	int i, j, n, m;


	scanf("%d", &n);
	num = 0;
	while (n--) {
		scanf("%d", &m);
		for (i = 0; i < num; i++) {
			if (a[i] == m) break;
		}

		if (i == num) {
			a[num] = m;
			b[num] = 1;
			num++;
		} else {
			b[i]++;
		}
	}

	int ans = 0;
	for (i = 0; i < num; i++) {
		if (b[i] % 2 == 1) ans++;
	}
	printf("%d\n", ans);

	return 0;
}
