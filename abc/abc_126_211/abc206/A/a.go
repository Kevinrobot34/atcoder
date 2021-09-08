package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	p := n * 108 / 100

	var ans string
	if p < 206 {
		ans = "Yay!"
	} else if p == 206 {
		ans = "so-so"
	} else {
		ans = ":("
	}
	fmt.Println(ans)
}
