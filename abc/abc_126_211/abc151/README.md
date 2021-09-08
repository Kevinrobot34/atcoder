# ABC151
* https://atcoder.jp/contests/abc151


## C - Welcome to AtCoder (300点)
* 問題文をよく読んで実装
  - 「ペナルティ数は、高橋君が **ACを1回以上出した** 各問題において...」


## D - Maze Master (400点)
* BFS
* 全ての`.`をスタート地点にBFSして、一番遠い点を探す
  - 一回のBFSに`O(HW)`
  - スタート地点の候補は`O(HW)`
  - 全体で`O(H^2 W^2)`
* 別解：ワーシャルフロイドの`O(H^3 W^3)`


## E - Max-Min Sums (500点)
* `f(X) = max(X) - min(X)`を全ての点集合`X`について **足す** だけ
* `A[i]`が何回maxとして足され、何回minとして引かれるを考えれば良い
  - `A`は昇順にソート済みとする
  - `K`個選んで、`A[i]`がmaxになるのは、`A[1]`から`A[i-1]`までの`i-1`個から`K-1`個選んだような`X`の場合
    - `comb(i-1, K-1)`
  - minについても同様


## F - Enclose All (600点)
* 最小包含円
  - https://tubo28.me/compprog/algorithm/minball/
  - http://drken1215.hatenablog.com/entry/2020/01/12/224200

* 二分探索
  - editorialの解法
  - `R`を決め打ちし、「最小包含円の半径は`R`以下であるか」を判定する形の二分探索と見る
    - 「最小包含円の半径は`R`以下であるか」の判定パート
      - `O(N^3)`
    - 全体で`O(N^3 * log X_MAX)`
* 全探索
  - 最小包含円の中心の候補となる点は以下のみ
    - 与えられた点集合のうちの異なる2点の中点
    - 与えられた点集合のうちの相異なる3点からできる三角形の外心
    - つまり`O(N^3)`個
  - 1つの中心点候補に対して半径は`O(N)`で求まる
    - よって全体で`O(N^4)`
  - http://drken1215.hatenablog.com/entry/2020/01/12/224200
* 最適化
  - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html
  - scipy使っちゃう（賢い
