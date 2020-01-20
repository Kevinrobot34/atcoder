#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<queue>
#include<numeric>
#include<map>
#include<string>

using namespace std;

int main(){
	int n, m;
	vector< pair<int, int> > v;

	scanf("%d%d", &n, &m);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		v.push_back(make_pair(a, b));
	}

	sort(v.begin(), v.end());

	int tail = v[0].second;
	int ans = 1;
	for (int i = 1; i < m; i++) {
		if (v[i].first >= tail) {
			ans++;
			tail = v[i].second;
		} else {
			tail = min(v[i].second, tail);
		}
	}

	printf("%d\n", ans);

	return 0;
}
