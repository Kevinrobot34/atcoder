#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int ans[505][505];
int main(){
	int i, j, h, w, d;
	char color[6] = "RGBY";

	scanf("%d%d%d", &h, &w, &d);

	int z, x, y;
	if (d % 2 == 1) {
		z = (d+1)/2;
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++) {
				x = i / z;
				y = j / z;
				ans[i][j] = (x+y)%2;
			}
		}
	} else {
		z = d / 2 + 2;
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++) {
				x = i / (z-1);
				y = j / (z-2);
				if (x%2==0 && y%2==0)ans[i][j] = 0;
				else if(x%2==0 && y%2==1)ans[i][j] = 1;
				else if(x%2==1 && y%2==0)ans[i][j] = 2;
				else ans[i][j]=3;
			}
		}
	}
	
	for (i = 0; i < h; i++) {
		for (j = 0; j < w; j++){
			printf("%c", color[ans[i][j]]);
		}
		printf("\n");
	}

	return 0;
}
