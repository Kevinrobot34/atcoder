#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<list>
#include<queue>
#include<map>
using namespace std;

list< pair<int, int> > edge;
list<int> edge_list[55];
int flag[55];
int edge_mat[55][55];

int main(){
	int i, j, n, m, a, b;

	scanf("%d%d", &n, &m);
	memset(edge_mat, 0, sizeof(int)*50*50);
	for (i = 0; i < m; i++) {
		scanf("%d%d", &a, &b);
		a--;b--;
		edge.push_back(make_pair(a, b));
		edge_list[a].push_back(b);
		edge_list[b].push_back(a);
		edge_mat[a][b] = 1;
		edge_mat[b][a] = 1;
	}
	/*for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) printf("%d", edge_mat[i][j]);
		printf("\n");
	}*/
	
	int ans = 0;
	list< pair<int, int> >::iterator it;
	for (it = edge.begin(); it != edge.end(); it++) {
		int x = (*it).first;
		int y = (*it).second;
		//printf("-----------%d %d\n", x, y);
		edge_mat[x][y] = 0;
		edge_mat[y][x] = 0;

		memset(flag, 0, sizeof(int)*n);
		queue<int> q;
		
		q.push(0);
		flag[0] = 1;
		int cnt = 1;
		while (q.size() != 0) {
			int index = q.front();
			q.pop();

			//printf("now::%d\n", index);
			
			list<int>::iterator it;
			for (it = edge_list[index].begin(); it != edge_list[index].end(); it++) {
				int nxt_index = (*it);
				
				if (edge_mat[index][nxt_index] == 0) continue;
				
				if (flag[nxt_index] == 0) {
					flag[nxt_index] = 1;
					q.push(nxt_index);
					cnt++;
				}
			}
		}
		if (cnt != n) {
			ans++;
			//printf("bridge!!\n");
		}

		edge_mat[x][y] = 1;
		edge_mat[y][x] = 1;
	}

	printf("%d\n", ans);

	return 0;
}
