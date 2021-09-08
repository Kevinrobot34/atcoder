# ABC154
* https://atcoder.jp/contests/abc154


## C - Fennec vs Monster (300点)
* 算数


## D - Caracal vs Monster (400点)
* 算数


## E - Crested Ibis vs Monster (500点)
* シンプルな一次元DP
  - `dp[i] = (モンスターの体力をiにするのに必要な最小の魔力の合計)`
  - `O(HN)`


## F - Silver Fox vs Monster (600点)
* いろんな解法で解けるいい問題
* 解法１
  - 貪欲 + 尺取(or 二分探索) + imos
  - 貪欲パート
    - 一番左端のモンスターから見ていき、そのモンスターが左端となるように爆破していくのが最適
  - 尺取 or 二分探索
    - ある爆発に対してどのモンスターまで爆破に巻き込まれたかを判定する必要がある
    - 尺取
      - 事前に`xi + 2d`より大きくなるindexを尺取で求める
    - 二分探査
      - `xi + 2d`を`bisect_right`
  - imos
    - 巻き込まれた爆破によって右側のモンスターがいくらHPが減っているかを管理する
* 解法２
  - 区間加算が可能なデータ構造で殴る
* Reference
  - https://drken1215.hatenablog.com/entry/2020/01/26/234000
