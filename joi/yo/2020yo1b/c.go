package main

import "fmt"

func main() {
	var n, m, ans int
	fmt.Scan(&n, &m)
	cnt := make([]int, n+1)
	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		cnt[ai]++
		if cnt[ai] > ans {
			ans = cnt[ai]
		}
	}
	fmt.Println(ans)
}
