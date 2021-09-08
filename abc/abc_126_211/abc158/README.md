# ABC158
* https://atcoder.jp/contests/abc158


## C - Tax Increase (300点)
* 小さい方から探す


## D - String Formation (400点)
* dequeを用いて、反転されているかという情報だけ持ちながらシミュレーション
* 双方向連結リストを使えば実際に反転するのもO(1)な気がするけど違うんかなぁ


## E - Divisible Substring (500点)
* `u[i] = int(s[i:])`としてあげると`int(s[i:j]) = (u[i] - u[j]) // (10**(j-i))`的な感じ
* `p`と10が互いに素なら`u[i]`と`u[j]`を`p`で割った余りが同じなら割り切れる


## F - Removing Robots (600点)
