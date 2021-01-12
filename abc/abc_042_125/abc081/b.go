package main

import (
	"fmt"
)

func main() {
	var n, ai int
	fmt.Scan(&n)

	ans := 1000000000
	for i := 0; i < n; i++ {
		fmt.Scan(&ai)
		cnt := 0
		for ; ai%2 == 0; ai /= 2 {
			cnt += 1
		}
		if cnt < ans {
			ans = cnt
		}
	}
	fmt.Println(ans)
}
