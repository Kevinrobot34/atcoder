#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX(x, y) (((x)>(y))?(x):(y))

double time[105], limit[105], acc[105];

double calc(double *v1, double *v2, double *v3, double t) {
	double tp = MAX(*v2-*v1, 0);
	double tm = t - MAX(*v2-*v3, 0);

	double ans, s;
	if (tp <= tm) {
		ans = (*v1+*v2)*tp*0.5 + (tm-tp)* (*v2) + (*v2+*v3) * (t-tm)*0.5;
	} else {
		s = (tp+tm)*0.5;
		if (s < 0.0) {

		} else if (s > t) {
			// kangaenai??
		} else {
			ans = (*v1)*s + s*s*0.5 + (*v3)*(t-s) + (t-s)*(t-s)*0.5;
		}
	}

	//printf("tp: %lf   tm:%lf   ans:%lf\n", tp, tm, ans);

	return ans;
}

int main(){
	int i, j, n, m;

	scanf("%d", &n);
	for (i = 1; i <= n; i++) scanf("%lf", &time[i]);
	for (i = 1; i <= n; i++) scanf("%lf", &limit[i]);
	limit[0] = 0;
	limit[n+1] = 0;

	int vel = 0;

	double ans = 0;
	for (i = 1; i <= n; i++) {
        ans += calc(&limit[i-1], &limit[i], &limit[i+1], time[i]);
	}
	
	printf("%lf\n", ans);

	return 0;
}
