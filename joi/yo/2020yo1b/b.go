package main

import "fmt"

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	var n, a, b int
	var s, ans string
	fmt.Scan(&n, &a, &b)
	a--
	fmt.Scan(&s)
	ans = string(s[:a]) + reverse(string(s[a:b])) + string(s[b:])
	fmt.Println(ans)
}
