package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n)
	x := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i])
	}
	fmt.Scan(&m)
	a := make([]int, m)
	for i := 0; i < m; i++ {
		fmt.Scan(&a[i])
	}

	for _, ai := range a {
		ai -= 1
		if x[ai] == 2019 {
			continue
		}
		is_possible := true
		for _, xj := range x {
			if xj == x[ai]+1 {
				is_possible = false
				break
			}
		}
		if is_possible {
			x[ai]++
		}
	}

	for _, xi := range x {
		fmt.Println(xi)
	}
}
