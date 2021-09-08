# ABC164
* https://atcoder.jp/contests/abc164


## C - gacha (300点)
* setを使えるか


## D - Multiple of 2019 (400点)
* 類題 : https://atcoder.jp/contests/abc158/tasks/abc158_e
* `a[i] = int(s[i:])` とする
  - すると`int(s[i:j])`は `(a[i] - a[j]) // (10**(n-j))`
  - これが2019で割り切れるためには、`a[i]`と`a[j]`の2019で割った余りが等しいことが必要十分条件
  - この数を数える


## E - Two Currencies (500点)
* keywords
  - グラフ、Dijkstra、頂点倍加
* 解法
  - 頂点倍化dijkstra(?)
    - ポイントは `Ai <= 50`
      - 使う銀貨は高々50*100=5000枚
    - graphの頂点をただ都市に対応させるのではダメ
      - 辺の重みは時間にして、頂点を工夫する
        - `頂点 = (都市, 残りの銀貨の枚数)`
      - 上記の考察のように高々使う銀貨は5000枚なので、第２引数は上限5000でOK
      - 頂点数は 50 * 5000 = 1.25 * 10**6
      - 辺の数は 100 * 5000 + 50 * 5000 = 7.5 * 10**5
        - dijkstraで解ける！


## F - I hate Matrix Construction (600点)
