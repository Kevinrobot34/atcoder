#include<bits/stdc++.h>
using namespace std;

int main(){
	string s, t;
	cin >> s;
	cin >> t;

	s = s + s;

	printf("%s\n", (s.find(t) == -1) ? "No" : "Yes");

	return 0;
}
