package main

import "fmt"

func main() {
	var a, b, c, ans int
	fmt.Scanf("%d %d %d", &a, &b, &c)
	if a <= c && c < b {
		ans = 1
	} else {
		ans = 0
	}

	fmt.Printf("%d\n", ans)
}
