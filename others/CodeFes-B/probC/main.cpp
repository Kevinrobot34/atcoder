#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<list>
using namespace std;

list<int> edge[100005];
int flag[100005];

int main(){
	int i, j, n, m;
	int x, y, z;

	scanf("%d%d", &n, &m);
	for (i = 0; i < m; i++) {
		scanf("%d%d", &x, &y);
		x--;y--;
		edge[x].push_back(y);
		edge[y].push_back(x);
	}
	
	//for (i = 0; i < n; i++) printf("%lu ", edge[i].size());printf("\n");
	list<int>::iterator it1, it2, it3, it4;
	
	int ans = 0;
	for (i = 0; i < n; i++) {
		memset(flag, 0, sizeof(int) * n);
		for (it1 = edge[i].begin(); it1 != edge[i].end(); it1++) {
			flag[*it1] = 1;
		}
		//for (j = 0; j< n; j++) printf("%d ", flag[j]);printf("\n");
		for (it1 = edge[i].begin(); it1 != edge[i].end(); it1++) {
			x = *it1;
			if (i == x) continue;
			for (it2 = edge[x].begin(); it2 != edge[x].end(); it2++) {
				y = *it2; 
				if (i == y || x == y) continue;
				for (it3 = edge[y].begin(); it3 != edge[y].end(); it3++) {
					z = *it3;
					if (x == z || y == z || i == z)  continue;
					//printf("%d %d %d %d\n", i+1, x+1, y+1, z+1);
					if (flag[z] == 0) {
						ans++;
						//edge[i].push_back(z);
						edge[z].push_back(i);
						flag[z] = 2;
					}
				}
			}
			//printf("size:%lu\n", edge[i].size());
		}
		for (j = 0; j < n; j++) {
			if (flag[j]==2) {
				edge[i].push_back(j);
			}
		}
	}
	printf("%d\n", ans);


	return 0;
}
