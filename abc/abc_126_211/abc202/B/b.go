package main

import "fmt"

func main() {
	var s, ans string
	m := map[byte]byte{'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

	fmt.Scan(&s)
	for i := len(s) - 1; i >= 0; i-- {
		ans += string(m[s[i]])
	}
	fmt.Println(ans)
}
