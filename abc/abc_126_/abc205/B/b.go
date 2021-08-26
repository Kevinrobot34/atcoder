package main

import "fmt"

func main() {
	var n int
	var isPossible bool

	fmt.Scan(&n)
	check := make([]bool, n)
	for i := 0; i < n; i++ {
		var ai int
		fmt.Scan(&ai)
		ai--
		check[ai] = true
	}

	isPossible = true
	for i := 0; i < n; i++ {
		if !check[i] {
			isPossible = false
			break
		}
	}

	if isPossible {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
