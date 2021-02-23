package main

import "fmt"

func main() {
	var n, m, d int
	fmt.Scan(&n, &m, &d)
	s := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&s[i])
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			isPossibleV := true
			isPossibleH := true
			for k := 0; k < d; k++ {
				if i+k >= n || s[i+k][j] == '#' {
					isPossibleV = false
				}
				if j+k >= m || s[i][j+k] == '#' {
					isPossibleH = false
				}
			}
			if isPossibleV {
				ans++
			}
			if isPossibleH {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
