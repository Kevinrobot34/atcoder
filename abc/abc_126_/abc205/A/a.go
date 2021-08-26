package main

import "fmt"

func main() {
	var a, b int
	var ans float64

	fmt.Scan(&a, &b)

	ans = float64(a) / 100.0 * float64(b)
	fmt.Println(ans)
}
