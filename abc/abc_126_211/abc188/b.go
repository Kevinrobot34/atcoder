package main

import (
	"fmt"
)

func main() {
	var n int
	var ans string
	fmt.Scan(&n)
	a := make([]int, n)
	b := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	for i := 0; i < n; i++ {
		fmt.Scan(&b[i])
	}

	p := 0
	for i := 0; i < n; i++ {
		p += a[i] * b[i]
	}

	if p == 0 {
		ans = "Yes"
	} else {
		ans = "No"
	}
	fmt.Println(ans)
}
