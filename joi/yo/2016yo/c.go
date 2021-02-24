package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	flag := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&flag[i])
	}

	ans := n * m
	for w := 1; w < n-1; w++ {
		for b := w + 1; b < n; b++ {
			cand := 0
			for i := 0; i < n; i++ {
				var c rune
				if i < w {
					c = 'W'
				} else if i < b {
					c = 'B'
				} else {
					c = 'R'
				}
				for _, flagij := range flag[i] {
					if flagij != c {
						cand++
					}
				}
			}
			if cand < ans {
				ans = cand
			}
		}
	}
	fmt.Println(ans)
}
