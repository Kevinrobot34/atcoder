# パナソニックプログラミングコンテスト2020
* https://atcoder.jp/contests/panasonic2020


## B - Bishop (200点)
* コーナーケースを学ぶのにいい問題


## C - Sqrt Inequality (300点)
* 数値誤差の問題があるので、比較はなるべく整数で


## D - String Equivalence (400点)
* 例えば、いくつかを書き下してみる
  - `n=2`の時
    - aa
    - ab
  - `n=3`の時
    - aaa
    - aab
    - aba
    - ~baa~ **abb**
    - abc
  - `n=4`の時
    - aaaa
    - aaab
    - aaba
    - abaa
    - ~baaa~ **abbb**
    - aabb
    - abab
    - ~baab~ **abba**
    - aabc
    - abac
    - abca
    - ~baac~ **abbc**
    - ~baca~ **abcb**
    - ~bcaa~ **abcc**
    - abcd
* 長さ`n`の標準形の文字列から、`n+1`の標準形の文字列を生成できることがわかる
  - 長さ`n`の標準形の文字列を辞書順で前から`w[i]`とし、前から順番に見ていく
  - `w[i]`が`m`種類の文字で構成されている時、`w[i]`の末尾に`a`から`m+1`番目までのアルファベット一つを追加する
    - これは長さ`n+1`の標準形になっている
    - 辞書順に小さい方から生成できている


## E - Three Substrings (500点)
* `N=max(|A|, |B|, |C|)`とする
* 文字列の長さが短いので、どれか一つの文字列を固定し、残り2つの相対的な位置を全探索できる
  - `O(N^2)`
* ある二つの文字列に重なりがある場合、それが可能かどうかを判定するには高々2000文字の比較が必要
  - `O(N)`
  - `(a,b)`・`(b,c)`・`(c,a)`とそれぞれ独立に判定を行えるということも重要
* 安直に上記二つを組み合わせると`O(N^3)`になってしまうので、判定を事前計算して保存しておく
  - これで`O(N^2)`