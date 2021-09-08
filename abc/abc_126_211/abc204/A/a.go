package main

import "fmt"

func main() {
	var x, y, ans int

	fmt.Scan(&x, &y)

	if x == y {
		ans = x
	} else {
		if x+y == 1 {
			ans = 2
		} else if x+y == 2 {
			ans = 1
		} else {
			ans = 0
		}
	}
	fmt.Println(ans)
}
