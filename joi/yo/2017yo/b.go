package main

import "fmt"

func main() {
	var n, m, s, c, ans int
	fmt.Scan(&n, &m)
	for i := 0; i < m; i++ {
		var ai, bi int
		fmt.Scan(&ai, &bi)
		if ai < n {
			s += n - ai
			if c < n-ai {
				c = n - ai
			}
		}
	}
	ans = s - c
	fmt.Println(ans)
}
