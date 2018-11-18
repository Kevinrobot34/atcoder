#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<list>
#include<queue>
#include<map>
using namespace std;

int main(){
	int i, j, k, n;
	char s[8];

	scanf("%s", s);
	int a = s[0] - '0';
	int b = s[1] - '0';
	int c = s[2] - '0';
	int d = s[3] - '0';

	for (i = 0; i < 2; i++) {
		b *= (-1);
		for (j = 0; j < 2;j++) {
			c *= (-1);
			for (k = 0; k < 2; k++) {
				d *= (-1);

				if (a+b+c+d == 7) break;
			}
			if (a+b+c+d == 7) break;
		}
		if (a+b+c+d == 7) break;
	}

	printf("%d%c%d%c%d%c%d=7\n", a, 
							((b>=0)?'+':'-'), ((b>=0)?b:(-b)),
							((c>=0)?'+':'-'), ((c>=0)?c:(-c)),
							((d>=0)?'+':'-'), ((d>=0)?d:(-d)));

	return 0;
}
