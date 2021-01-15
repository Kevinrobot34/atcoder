package main

import "fmt"

func main() {
	var n, sum, max, ans int

	fmt.Scan(&n)
	a := make([]int, n, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
		if a[i] > max {
			max = a[i]
		}
		sum += a[i]
	}
	for _, ai := range a {
		if ai == max {
			break
		}
		ans += ai
	}
	fmt.Println(ans)
	fmt.Println(sum - ans - max)
}
