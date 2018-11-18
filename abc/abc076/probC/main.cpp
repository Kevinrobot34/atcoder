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
	int i, j, k, n, m, a, b;
	char s[55], t[55];

	scanf("%s", s);
	scanf("%s", t);
	int slen = strlen(s);
	int tlen = strlen(t);

	for (i = slen - tlen; i >= 0; i--) {
		for (j = 0; j < tlen; j++) {
			if (s[i+j] == '?') continue;
			else if (s[i+j] != t[j]) break;
		}

		if (j == tlen) {
			for (j = 0; j < tlen; j++) {
				s[i+j] = t[j];
			}
			for (j = 0; j < slen; j++){
				if (s[j] == '?') s[j] = 'a';
			}
			printf("%s\n", s);
			break;
		}
	}
	if (i == -1) printf("UNRESTORABLE\n");

	return 0;
}
