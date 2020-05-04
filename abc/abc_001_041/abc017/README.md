# ABC017
* https://atcoder.jp/contests/abc017


## C - ハイスコア
* いもす法


## D - サプリメント
* keyword
  - DP, しゃくとり法, 累積和
* 解法
  - しゃくとりパート
    - `left[i] = ( [left[i], i)の区間にあるサプリの種類に重複はない )`
      - `left[i]`個目のサプリと`i`個目のサプリは同じ
  - DPパート
    - 更新に累積和を用いて高速化
    - `dp[i] = (i個目までのサプリを食べる方法の数(i個目を食べて一旦その日はもう他に食べない))`
      - `dp[i]`は次の和として求められる
        - `(..., left[i]) (left[i]+1, ..., i-1, i)`と食べる方法
          - `dp[left[i]]`通り
        - `(..., left[i]+1) (left[i]+2, ..., i-1, i)`と食べる方法
          - `dp[left[i]+1]`通り
        - ...
        - `(..., i-1) (i)`と食べる方法
          - `dp[i-1]`通り
      - よって `dp[i] = sum(dp[j] for j in range(left[i], j))`
        - ここを累積和を使って高速化
* comment
  - 難しい
* reference
  - [けんちょんさんの解説]( https://qiita.com/drken/items/ecd1a472d3a0e7db8dce#%E5%95%8F%E9%A1%8C-7abc-017-d-%E3%82%B5%E3%83%97%E3%83%AA%E3%83%A1%E3%83%B3%E3%83%88 )
