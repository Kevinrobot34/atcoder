package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	sugoroku := make([]int, n)
	dice := make([]int, m)
	for i := 0; i < n; i++ {
		fmt.Scan(&sugoroku[i])
	}
	for i := 0; i < m; i++ {
		fmt.Scan(&dice[i])
	}
	cur := 0
	ans := 0
	for i := 0; i < m; i++ {
		if cur < n-1 {
			cur += dice[i]
		}
		if cur >= n-1 {
			ans = i + 1
			break
		}
		if cur < n-1 {
			cur += sugoroku[cur]
		}
		if cur >= n-1 {
			ans = i + 1
			break
		}
	}
	fmt.Println(ans)
}
