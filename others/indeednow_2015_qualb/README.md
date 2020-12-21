# Indeedなう（予選B）
* https://atcoder.jp/contests/indeednow-qualb


## C - 木
* keywords
  - 木、BFS、priority_queue、heapq
* 解法
  - 木の上でBFSする感じ
  - queueとしてpriority_queueを使ってあげれば良い


## D - 高橋くんと数列
* keywords
* 解法
  - 連続する部分列は`O(N^2)`あるので全探索は無理
  - また、ある数字を一つでも含む部分列を数えるのは大変なので、余事象を考える
  - `O(N+c)`
