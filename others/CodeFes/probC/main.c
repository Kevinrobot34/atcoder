#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main(){
	int i, j, h, w;
	char str[105];
	int count[30];

	for (i = 0; i < 26; i++) count[i] = 0;
	scanf("%d%d", &h, &w);
	for (i = 0; i < h; i++) {
		scanf("%s", str);
		//printf("%s", str);
		for (j = 0; j < w; j++) {
			count[str[j] -'a']++;
		}
	}
	//for (j=0;j<26;j++)printf("%d ", count[j]);	
	int p1 = 0, p2 = 0, p4 = 0;
	if (h % 2 == 0 && w % 2 == 0) {
		p4 = h*w / 4;
	} else if (h % 2 == 0 && w % 2 != 0) {
		p4 = h * (w - 1) /4;
		p2 = h/2;
	} else if (h % 2 != 0 && w % 2 == 0) {
		p4 = (h - 1) * w /4;
		p2 = w / 2;
	} else {
		p1 = 1;
		p4 = (h - 1) * (w - 1) / 4;
		p2 = (h*w - p4*4 - p1) / 2;
	}
	
	int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
	for (j = 0; j < 26; j++) {
		if (count[j] == 0)continue;
		if (count[j] % 4 == 0) c4++;
		else if (count[j] % 4 == 1) c1++;
		else if (count[j] % 4 == 2) c2++;
		else c3++;
	}
	/*
	printf("p1:%d\n", p1);
	printf("p2:%d\n", p2);
	printf("p4:%d\n", p4);

	printf("c1:%d\n", c1);
	printf("c2:%d\n", c2);
	printf("c3:%d\n", c3);
	printf("c4:%d\n", c4);
	*/
	int ans = 0;
	if (p1 == c1 + c3 && p2 >= c2+c3 && (p2-c2-c3)%2 == 0) {
		ans = 1;
	}

	printf("%s\n", (ans == 1) ? ("Yes"):("No"));

	return 0;
}
