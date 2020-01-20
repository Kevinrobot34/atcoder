#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <cmath>

#define min(x, y)  (((x) < (y)) ? (x) : (y))
#define INF 100000000


int travel[202];
int dp[202][202];
int tsl[(1<<8)+5][10]; //[now][past-sets]
int ans[202];
int n, m, r;


void warshall_floyd() {
	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
			}
		}
	}
	return;
}


int tsp(int start){
	for (int i = 0; i < (1<<r); i ++) for (int j = 0; j < r; j++)tsl[i][j] = INF;
	
	tsl[1<<start][start] = 0;
	for (int S = (1<<start); S < (1<<r); S++) {
		for (int u = 0; u < r; u++) {
			for (int v = 0; v < r; v++){
				if ((S & (1<<u)) != 0) { // u in S & v not in S
					tsl[S|(1<<v)][v] = min(tsl[S|(1<<v)][v], tsl[S][u] + dp[travel[u]][travel[v]]);
				}
			}
		}
	}
	int ans=tsl[(1<<r)-1][0];
	for (int i = 1; i < r; i++) ans = min(ans, tsl[(1<<r)-1][i]);
	return ans;
}

int main(){
	int i, j, k, a, b, c;
	
	scanf("%d %d %d\n", &n, &m, &r);
	for (i = 0; i < r; i++) {
		scanf("%d", &travel[i]);
		travel[i] -= 1;
	}
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (i == j) dp[i][j] = 0;
			else dp[i][j] = INF;
		}
	}
	for (i = 0; i < m; i++) {
		scanf("%d %d %d\n", &a, &b, &c);
		a -=1; b -= 1;
		dp[a][b] = c;
		dp[b][a] = c;
	}

	warshall_floyd();
	int ans = tsp(0);
	for (i = 1; i < r; i++) ans = min(ans, tsp(i));
	printf("%d\n", ans);

	return 0;
}
