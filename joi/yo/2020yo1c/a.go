package main

import "fmt"

func main() {
	var x, l, r, ans int
	fmt.Scan(&x, &l, &r)
	if x < l {
		ans = l
	} else if x <= r {
		ans = x
	} else {
		ans = r
	}
	fmt.Println(ans)
}
