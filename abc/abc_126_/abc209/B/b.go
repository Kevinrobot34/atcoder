package main

import "fmt"

func main() {
	var n, x, total_cost int
	fmt.Scanf("%d %d", &n, &x)

	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		total_cost += ai
	}
	total_cost -= n / 2

	var ans string
	if x >= total_cost {
		ans = "Yes"
	} else {
		ans = "No"
	}
	fmt.Println(ans)
}
