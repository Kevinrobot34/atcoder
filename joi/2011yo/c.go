package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	for i := 0; i < k; i++ {
		var ai, bi int
		fmt.Scan(&ai, &bi)
		ai--
		bi--
		if ai > (n-1)/2 {
			ai = n - 1 - ai
		}
		if bi > (n-1)/2 {
			bi = n - 1 - bi
		}
		if ai > bi {
			ai, bi = bi, ai
		}
		// 0 <= ai <= bi <= (n-1)/2
		ci := ai%3 + 1
		fmt.Println(ci)
	}
}
