package main

import "fmt"

func main() {
	var n, a, x, y, ans int
	fmt.Scan(&n, &a, &x, &y)
	if n > a {
		ans = a*x + (n-a)*y
	} else {
		ans = n * x
	}
	fmt.Println(ans)
}
