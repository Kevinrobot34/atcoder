package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var n int
	fmt.Scan(&n)
	s := make([]string, n)
	t := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&s[i])
	}
	for i := 0; i < n; i++ {
		fmt.Scan(&t[i])
	}
	ans := n * n
	for r := 0; r < 4; r++ {
		cand := min(r, 4-r)
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if s[i][j] != t[i][j] {
					cand++
				}
			}
		}
		ans = min(ans, cand)

		// rotation 90 degree
		u := make([]string, n)
		for i := 0; i < n; i++ {
			u[i] = ""
			for j := 0; j < n; j++ {
				u[i] += string(s[j][n-1-i])
			}
		}
		for i := 0; i < n; i++ {
			s[i] = u[i]
		}
	}
	fmt.Println(ans)
}
