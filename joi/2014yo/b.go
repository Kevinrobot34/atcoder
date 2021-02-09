package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	vote := make([]int, n)
	for j := 0; j < m; j++ {
		var bj int
		fmt.Scan(&bj)
		for i := 0; i < n; i++ {
			if a[i] <= bj {
				vote[i]++
				break
			}
		}
	}
	ans := 0
	for i := 1; i < n; i++ {
		if vote[i] > vote[ans] {
			ans = i
		}
	}
	ans++
	fmt.Println(ans)
}
