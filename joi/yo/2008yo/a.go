package main

import "fmt"

func main() {
	var n int
	var coins = []int{500, 100, 50, 10, 5, 1}
	fmt.Scan(&n)
	n = 1000 - n
	ans := 0
	for _, c := range coins {
		ans += n / c
		n %= c
	}
	fmt.Println(ans)
}
