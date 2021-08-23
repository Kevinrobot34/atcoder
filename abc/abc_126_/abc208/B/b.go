package main

import "fmt"

func main() {
	var p int
	fmt.Scan(&p)

	coins := make([]int, 11)
	coins[0] = 1
	for i := 1; i < 11; i++ {
		coins[i] = coins[i-1] * i
	}

	ans := 0
	for i := 10; i > 0; i-- {
		ans += p / coins[i]
		p %= coins[i]
	}
	fmt.Println(ans)
}
