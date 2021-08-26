package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	ans := 0
	total := 0
	for i := 1; ; i++ {
		total += i
		ans++
		if total >= n {
			break
		}
	}

	fmt.Println(ans)
}
