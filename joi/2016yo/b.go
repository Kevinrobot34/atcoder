package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	for k := 1; k <= m; k++ {
		for i := 0; i < n-1; i++ {
			if a[i]%k > a[i+1]%k {
				a[i], a[i+1] = a[i+1], a[i]
			}
		}
	}
	for i := 0; i < n; i++ {
		fmt.Println(a[i])
	}
}
