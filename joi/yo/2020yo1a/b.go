package main

import "fmt"

func main() {
	var n, ans int
  var s string
	fmt.Scan(&n)
  fmt.Scan(&s)
	cnt := map[rune]int{'a': 0, 'i': 0, 'u': 0, 'e': 0, 'o': 0}
  for _, si := range s {
    if _, isin := cnt[si]; isin {
      ans++
    }
  }
	fmt.Println(ans)
}
