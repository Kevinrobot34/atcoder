package main

import "fmt"

func abs(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var h, w int
	fmt.Scan(&h, &w)
	a := make([][]int, h)
	for i := range a {
		a[i] = make([]int, w)
	}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			fmt.Scan(&a[i][j])
		}
	}
	ans := 100 * 25 * 25 * 25
	for i0 := 0; i0 < h; i0++ {
		for j0 := 0; j0 < w; j0++ {
			cnt := 0
			for i := 0; i < h; i++ {
				for j := 0; j < w; j++ {
					cnt += a[i][j] * min(abs(i-i0), abs(j-j0))
				}
			}
			ans = min(ans, cnt)
		}
	}
	fmt.Println(ans)
}
