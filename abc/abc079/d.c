#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX(x, y) (((x)>(y))?(x):(y))
#define min(x, y) (((x)<(y))?(x):(y))

int c[20][20];
int d[20][20];

int main(){
	int i, j, k, h, w;

	scanf("%d%d", &h, &w);

	for (i = 0; i < 10; i ++) for (j = 0; j < 10; j ++) scanf("%d", &d[i][j]);

	for (k = 0; k < 10; k++) {
		for (i = 0; i < 10; i++) {
			for (j = 0; j < 10; j++) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}
	
	//for (i = 0; i < 10; i++) {for (j = 0; j < 10; j++) {printf("%d ", d[i][j]);} printf("\n");}

	int x;
	int ans = 0;
	for (i = 0; i < h; i++) {
		for (j = 0; j < w; j++) {
			scanf("%d", &x);
			
			if (x != -1) {
				ans += d[x][1];
			}
		}
	}

	printf("%d\n", ans);

	return 0;
}
