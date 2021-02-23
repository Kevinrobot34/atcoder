package main

import "fmt"

const nAalpha = 26

func main() {
	var s string
	fmt.Scan(&s)
	ans := ""
	for _, si := range s {
		ans += string('A' + (nAalpha+si-'A'-3)%nAalpha)
	}
	fmt.Println(ans)
}
