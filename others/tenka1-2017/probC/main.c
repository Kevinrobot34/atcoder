#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define min(x, y) (((x)<(y)) ? (x) : (y))

int main() {
	int i, j;
	int m, h, w, n;

	scanf("%d", &m);

	for (h = 1; h <= 3500; h++) {
		for (w = 1; w <=3500; w++) {
			if (4 * h*w <= m *(h+w)) continue;
			
			long long int x = (long long int)m * (long long int)(h*w);
			long long int y = (long long int)4*h*w - (long long int)(m*(h+w));
			
			long long int z = x / y;
			if (z * y == x ) {
				printf("%d %d %lld\n", h, w, z);
				return 0;
			}
		}
	}

	return 0;
}
