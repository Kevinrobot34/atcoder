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

int test_func(){

	printf("test");

}

int main(){
	string s, t;
	cin >> s;
	cin >> t;

	for (size_t i = 0; i < s.size(); i++) {
		printf("%c ", s[i]);
	}

	for (size_t i = 0; i < s.size(); i++) {
		for (size_t j = 0; j < s.size(); j++) {
			if (s[i] != t[(i+j)%3]) break;
		}
		if (j == s.size()) break;
	}
	if (i == s.size()) {
		printf("Yes\n");
	}else{
		printf("No\n");
	}
	printf("%s\n", s.c_str());

	return 0;
}
