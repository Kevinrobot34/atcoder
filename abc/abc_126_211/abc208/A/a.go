package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	var ans string
	if a <= b && b <= 6*a {
		ans = "Yes"
	} else {
		ans = "No"
	}
	fmt.Println(ans)
}
