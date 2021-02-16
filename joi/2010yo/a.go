package main

import "fmt"

func main() {
	var s int
	fmt.Scan(&s)
	for i := 0; i < 9; i++ {
		var ci int
		fmt.Scan(&ci)
		s -= ci
	}
	fmt.Println(s)
}
