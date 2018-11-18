#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<queue>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;

int l;
vector <int> vc;

int main(){
	int i, j;
	int n, c;

	scanf("%d%d", &n, &c);
	for (i = 0; i < n; i++) {
		scanf("%d", &l);
		vc.push_back(l*(-1));
	}
	vector<int>::iterator it;
	sort(vc.begin(), vc.end());	
	
	/*
	for (it = vc.begin(); it != vc.end(); it++) {
		printf("%ld : %d\n", it-vc.begin(), *it);
	}
	*/
	int ans = 0;
	for (it = vc.begin(); n != 0; it = vc.begin()) {
		int l_now = (*it) * (-1);
		int res = (c - l_now - 1)*(-1);
		vc.erase(it);
        if (l_now == c-1 || l_now == c) {
            ans++;
			n--;
        } else {
            vector<int>::iterator lit = lower_bound(vc.begin(), vc.end(), res);
            vector<int>::iterator uit = upper_bound(vc.begin(), vc.end(), res);
            //printf("%d %d %d\n", l_now, *uit, *lit);
            if (*lit == 0 && *uit ==0 ){
				ans++;
            	n--;
			}else {
                ans++;
				n -=2;
				vc.erase(lit);
            }
        }
		printf("%lu\n",vc.size());
    }
	printf("%d\n", ans);

	return 0;
}
