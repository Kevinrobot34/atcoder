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
	string s, t;
	cin >> s;
	cin >> t;

	int n = s.length();
	int i = 0;
	for (; i < n; i++) {
		int j = 0;
		for (; j < n; j++) {
			if (s[j] != t[(i+j) % n]) break;
		}
		if (j == n) break;
	}

	printf("%s\n", (i == n) ? "No" : "Yes");

	return 0;
}
