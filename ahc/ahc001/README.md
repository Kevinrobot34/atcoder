# AHC001
* https://atcoder.jp/contests/ahc001


## My Trials
* `minimum.py`
  - 入力の`(xi, yi)`を左上とする一辺一の正方形を出力するだけ
  - https://atcoder.jp/contests/ahc001/submissions/20782852
    - `823,090`点
    - 32ms
* `random_baseline.py`
  - `minimum.py`からはじめる
  - ランダムに長方形を大きくしていく
  - 「面積が`ri`を越える」・「他の長方形と被る」まで続ける
  - https://atcoder.jp/contests/ahc001/submissions/20783265
    - `45,240,488,904`点
    - 1904ms
    - 試行回数を変更しても変わらない
* `retry_baseline.py`
  - `random_baseline.py`を何度か試して最良のものを提出する
  - https://atcoder.jp/contests/ahc001/submissions/20784192
    - `45,322,823,628`点
    - 3703ms	
