package main

import "fmt"

const games = 3

func main() {
	var n int
	fmt.Scan(&n)
	p := make([][]int, n)
	for i := 0; i < n; i++ {
		p[i] = make([]int, games)
	}
	ans := make([]int, n)

	for i := 0; i < n; i++ {
		for j := 0; j < games; j++ {
			fmt.Scan(&p[i][j])
		}
	}

	for i := 0; i < games; i++ {
		for j := 0; j < n; j++ {
			isSame := false
			for k := 0; k < n; k++ {
				if j == k {
					continue
				}
				if p[j][i] == p[k][i] {
					isSame = true
					break
				}
			}
			if !isSame {
				ans[j] += p[j][i]
			}
		}
	}
	for i := 0; i < n; i++ {
		fmt.Println(ans[i])
	}
}
