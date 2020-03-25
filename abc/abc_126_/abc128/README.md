# ABC128
* https://atcoder.jp/contests/abc128


## C - Switches (300点)
* bit使って全探索


## D - equeue (400点)
* 操作Aと操作Bと操作CDを何回ずつするかで全探索


## E - Roadwork (500点)
* イベントソート
* 座標`x[i]`を`[s[i], t[i])`通行止めにする
  - 時刻`0`の時`(x[i] - t[i], x[i] - s[i]]`にいる人はこの通行止めに止められる
* query
  - 時刻`d[i]`に座標`0`を出発する人
  - `x = 1(t - d[i])`

## F - Frog Jump (600点)
