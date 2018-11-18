#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

char ban[55][55];
int dx[] = {-1, 0,   1, -1, 1, -1, 0, 1};
int dy[] = {-1, -1, -1,  0, 0,  1, 1, 1};

int main(){
	int i, j, k, n, m;
	int h, w;
	
	scanf("%d%d", &h, &w);

	for (i = 0; i < h; i++) {
		scanf("%s", ban[i]);
	}
	
	int x, y, cnt;
	for (i = 0; i < h; i++) {
		for (j = 0; j < w; j++) {
			if (ban[i][j] == '#') continue;

			cnt = 0;
			for (k = 0; k < 8; k++) {
				y = i + dx[k];
				x = j + dy[k];
				if (x < 0 || y < 0 || x >= w || y >= h) continue;

				if (ban[y][x] == '#') cnt++;
			}
			ban[i][j] = '0' + cnt;
		}
	}
	
	for (i = 0; i < h; i++) printf("%s\n", ban[i]);

	return 0;
}
