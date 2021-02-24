package main

import "fmt"

func main() {
	var n, ans, cand int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

  ans = 0
  cand = 1
	a = append(a, 0)
	for i := 0; i < n; i++ {
		if a[i] <= a[i+1] {
			cand++
		} else {
			if ans < cand {
				ans = cand
			}
			cand = 1
		}
	}
  fmt.Println(ans)
}
