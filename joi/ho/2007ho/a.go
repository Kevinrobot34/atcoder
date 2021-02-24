package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	var n, k int
	fmt.Scan(&n, &k)

	a := make([]int, n)
	s := 0
	ans := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
		s += a[i]
		if i == k-1 {
			ans = s
		} else if i >= k {
			s -= a[i-k]
			ans = max(ans, s)
		}
	}
	fmt.Println(ans)
}
