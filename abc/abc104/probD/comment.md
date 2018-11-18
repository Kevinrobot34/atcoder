### 方針
DPでやる．

$\mathrm{dp}[i][str]$
* dp[i]['A'] = (Tの1-i文字目までの中に含まれる'A'の数)
* dp[i]['AB'] = (Tの1-i文字目までの中に含まれる'A'とそれより右にある'B'の組の数)
* dp[i]['ABC'] = (Tの1-i文字目までの中に含まれる'A'とそれより右にある'B'と更にそれより右にある'C'の組の数)

count[i]
* count[i] = (Tの1-(i-1)文字目までの中に含まれる'?'の数)

とする．
この時，
* 初期値
* 漸化式
  * dp[i+1]['A'] =
    * dp[i]['A']\*3 + 3\*count[i] (s[i]=='?')
    * dp[i]['A'] + 3\*count[i] (s[i]=='A')
    * dp[i]['A'] (otherwise)

\[
\begin{align}
    dp[i+1]['A']
\end{align}
\]
