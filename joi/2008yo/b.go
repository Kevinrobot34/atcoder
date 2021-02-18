package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	ans1 := 0
	ans2 := 0
	for i := 0; i < len(s)-2; i++ {
		if s[i:i+3] == "JOI" {
			ans1++
		} else if s[i:i+3] == "IOI" {
			ans2++
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
