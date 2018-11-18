#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;

vector <int> vd, vt;

int main(){
	int i, j, n, m;

	scanf("%d", &n);
	for (i = 0; i < n; i++) scanf("%d", &j), vd.push_back(j);
	scanf("%d", &m);
	for (i = 0; i < m; i++) scanf("%d", &j), vt.push_back(j);

	if (n < m) {
		printf("NO\n");
		return 0;
	}

	sort(vd.begin(), vd.end());
	vector<int>::iterator it;
	for (it = vt.begin(); it != vt.end(); it++) {
		vector<int>::iterator lit = lower_bound(vd.begin(), vd.end(), *it);
		vector<int>::iterator uit = upper_bound(vd.begin(), vd.end(), *it);
		if (uit - lit == 0) {
			break;
		} else {
			vd.erase(lit);
		}
	}

	if (it == vt.end()) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}

	return 0;
}
