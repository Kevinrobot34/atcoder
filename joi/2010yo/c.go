package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n)
	fmt.Scan(&m)
	graph := make([][]int, n)

	// load graph
	for i := 0; i < m; i++ {
		var ai, bi int
		fmt.Scan(&ai, &bi)
		ai--
		bi--
		graph[ai] = append(graph[ai], bi)
		graph[bi] = append(graph[bi], ai)
	}

	// count
	depth := make([]int, n)
	for i := 1; i < n; i++ {
		depth[i] = -1
	}
	for _, vt := range graph[0] {
		depth[vt] = 1
		for _, vtt := range graph[vt] {
			if depth[vtt] == -1 {
				depth[vtt] = 2
			}
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		if depth[i] > 0 && depth[i] <= 2 {
			ans++
		}
	}
	// fmt.Println(depth)
	fmt.Println(ans)
}
