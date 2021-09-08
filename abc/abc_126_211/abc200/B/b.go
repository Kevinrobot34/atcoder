package main

import "fmt"

func main() {
	var n, k int
	var ans int64

	fmt.Scan(&n, &k)
	ans = int64(n)
	for i := 0; i < k; i++ {
		if ans%200 == 0 {
			ans /= 200
		} else {
			ans = 1000*ans + 200
		}
	}
	fmt.Println(ans)
}
