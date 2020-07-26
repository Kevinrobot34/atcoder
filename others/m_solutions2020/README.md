# M-SOLUTIONS プロコンオープン 2020
* https://atcoder.jp/contests/m-solutions2020


## D - Road to Millionaire　(400点)
* submissions
  - [コンテスト中の自分の提出]( https://atcoder.jp/contests/m-solutions2020/submissions/15433506 )
  - [自分の提出-DP]( https://atcoder.jp/contests/m-solutions2020/submissions/15469441 )
  - [自分の提出-貪欲]( https://atcoder.jp/contests/m-solutions2020/submissions/15469557 )
* keywords
  - 貪欲法、DP
* 解法1
  - DP
  - `dp[i] = i日目終了時点での金額の最大値`
    - `i`日目に株を売らない場合と売る場合の2通りがある
      - 売らない場合は前日までの金額の最大値: `dp[i-1]`
      - 売る場合は`j`日に株を買い、`i`日に株を売る: `dp[j-1] % a[j] + (dp[j-1] // a[j]) * a[i]`
        - `0<j<i`
    - 漸化式：`dp[i] = max(dp[i-1], {dp[j-1] % a[j] + (dp[j-1] // a[j]) * a[i] | 0<j<i})`
    - 答え：`dp[n]`
    - `O(N^2)`
* 解法2
  - 貪欲法
  - editorial参照
  - `O(N)`
* comments
  - 所持金の最大値は`1000 * 2**40`
    - 株価が`100, 200, 100, 200, ...`と繰り返すとき、2日ごとに所持金は2倍にできる


## E - M's Solution (500点)


## F - Air Safety (600点)
