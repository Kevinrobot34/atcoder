# 文字列系
## 辞書順
問題
* [ABC009 C - 辞書式順序ふたたび]( https://atcoder.jp/contests/abc009/tasks/abc009_3 )


## suffix array
 * https://qiita.com/flare/items/20439a1db54b367eea70

## LCP array
* https://blog.shibayu36.org/entry/2017/01/06/103956

## KMP法
長さ$`N`$の文字列$`S`$に対して、
* $`\mathrm{KMP}[i] = `$( 文字列$`S[:i]`$の接頭辞と接尾辞が最大何文字一致しているか)

を$`0\leq i < N`$なるすべての$`i`$について、$`O(N)`$で計算するアルゴリズム。
```
S  : aabaabaaa
KMP: _010123452 (_=-1)
```
解説
* https://snuke.hatenablog.com/entry/2014/12/01/235807
* http://potetisensei.hatenablog.com/entry/2017/07/10/174908

使い道
* 最小の周期長を求める
    * 「文字列$`S`$の最小の周期長」＝「$`k`$ 文字ずらしたものが元の文字列と一致するような最小の $`k ~(k>0)`$」
        * 例えば`ababa`の最小の周期長は2
          ```
          ababa
          __ababa
          ```
  * 1-indexedで `i-KMP[i]`
    * 具体例
        ```
        S  : aabaabaaa
        KMP: _010123452 (_=-1)
        mpl: 113333337
        ```
* 文字列検索
    * 文字列`S`の中に`T`が含まれるか検索したい時には、`kmp(T+'#'+S)`をすると良い

```python
def kmp(s):
    n = len(s)
    kmp = [0] * (n+1)
    kmp[0] = -1
    j = -1
    for i in range(n):
        while j >= 0 and s[i] != s[j]:
            j = kmp[j]
        j += 1
        kmp[i+1] = j

    return kmp
```


## Manacherのアルゴリズム
回文関連のやつ
* https://snuke.hatenablog.com/entry/2014/12/02/235837


## Z Algorithm
長さ$`N`$の文字列$`S`$に対して、
* $`Z[i] = `$($`S`$と$`S[i:]`$の最長共通接頭辞(LCP)の長さ)

を$`0\leq i < N`$なるすべての $`i`$ について、$`O(N)`$で計算するアルゴリズム。例えば具体例はこんな感じ。
```
S:aaabaaaab
Z:921034210
```

使い道
* LCP
* 文字列検索
    * 文字列`S`の中に`T`が含まれるか検索したい時には、`z_algorithm(T+'#'+S)`をすると良い


解説
* https://snuke.hatenablog.com/entry/2014/12/03/214243
* http://codeforces.com/blog/entry/3107

```python
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n

    i = 1
    lcp = 0
    while i < n:
        while i+lcp < n and s[i+lcp] == s[lcp]:
            lcp += 1
        z[i] = lcp

        if lcp == 0:
            i += 1
            continue

        k = 1
        while i+k < n and k+z[k] < lcp:
            z[i+k] = z[k]
            k += 1
        i += k
        lcp -= k

    return z
```

問題
* [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )
* [ABC135 F - Strings of Eternity (600点)]( https://atcoder.jp/contests/abc135/tasks/abc135_f )


## Rooling Hash
* https://odan3240.hatenablog.com/entry/2015/02/16/111938
* https://ei1333.github.io/luzhiled/snippets/string/rolling-hash.html
* https://scrapbox.io/pocala-kyopro/ローリングハッシュ
* http://perogram.hateblo.jp/entry/rolling_hash
* アリ本 第２版 「4-7 文字列を華麗に扱う」

### ハッシュ関数
そもそも[ハッシュ関数]( https://ja.wikipedia.org/wiki/ハッシュ関数  )とは、文字列・数列といった何かしらのデータが与えられた時に、そのデータに対応したなんらかの数値を得るなんらかの操作(関数)のこと。
データをハッシュ関数にかけて得られた数値のことをハッシュ値という。
元データの比較処理が重いような場合(文字列・数列など)、ハッシュ値に変換してから比較することで高速化が望めたりする。
```{latex}
\text{HashFunction} : \text{Data(str, series, ...)} \mapsto \text{HashValue}
```

### RollingHashの概要
ただし、ハッシュ値の計算に時間がかかっていては意味がない。
そこで数列に対するハッシュ関数として、高速で便利なのがローリングハッシュである。
ローリングハッシュ(多項式ハッシュ, Karp-Rabin Fingerprint)とは、数列$`a ~=~[a_0, ~a_1, ~\cdots,~ a_{n-1} ]`$に対して
```{latex}
\begin{align*}
 H(a, b, m)
&= \left[~ a_0~b^{n-1} + a_1~b^{n-2} + \cdots  + a_{n-1}~b^{0} ~\right] ~\mathrm{mod}~~ m \\
&= \left[~ \sum_{i=0}^{n-1} a_i ~b^{n-1-i} ~\right] ~\mathrm{mod}~~ m
\end{align*}
```
と定義されるハッシュ関数のこと。文字列にも適用可能。（ 文字列$`S=S_0S_1\cdots S_{n-1}`$ を数列$`a = \left[\mathrm{ord}(S_0), ~\mathrm{ord}(S_1), ~\cdots, ~\mathrm{ord}(S_{n-1}) \right]`$ に変換すれば良い。$`\mathrm{ord}(\cdot)`$は文字の[アスキーコードを返す関数]( https://docs.python.org/ja/3/library/functions.html#ord )。）

多項式の形なので、**（累積和のようなイメージで）効率的に計算できる** のがミソ。具体的には、長さ$`N`$の数列$`S`$に対して$`H(S[:i], b, h)`$を全ての $`i`$ に対して計算するという前処理$`O(N)`$を行なっておくと、$`S`$の任意の部分列$`S[l:r]`$のハッシュ値を$`O(1)`$で次式のように計算できるようになる。
```{latex}
H(S[l:r], b, m) = \left[~ H(S[:r], b, m) - H(S[:l], b, m) ~ b^{r-l} ~\right] ~\mathrm{mod}~~ m \\
\left(
\begin{align*}
 H(S[:r], b, m) &= \left[~ S_0~b^{r-1} + \cdots + S_{l-1}~b^{r-l} + S_l~b^{r-l-1} + \cdots  + S_{r-1}~b^{0} ~\right] ~\mathrm{mod}~~ m \\
H(S[:l], b, m)&= \left[~ S_0~b^{l-1} + \cdots  + S_{l-1}~b^{0}  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  \right] ~\mathrm{mod}~~ m \\
H(S[l:r], b, m)&= \left[  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  S_l~b^{r-l-1} + \cdots  + S_{r-1}~b^{0} ~\right] ~\mathrm{mod}~~ m
\end{align*}
\right)
```


直接文字列を比較するのではなく、効率的に計算されるハッシュ値の比較をすることで処理の高速化を図る。

### ハッシュの衝突について
ハッシュは衝突することもある。
複数の$`b`$と$`h`$に対してハッシュを計算するようにしておくことで、衝突する確率を下げるのが比較的容易な対策の一つ。
* https://snuke.hatenablog.com/entry/2017/02/03/035524

```python
class RollingHash:
    def __init__(self, s: str, base: int=1007, mod: int=10**9+7):
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod

        # preprocess
        self.hash_cum = [0] * (self.n + 1) # hash_cum[i] = (hash of s[:i])
        self.base_pow = [1] * (self.n + 1) # base_pow[i] = base ** i
        for i in range(self.n):
            self.hash_cum[i+1] = (self.hash_cum[i] * base + ord(s[i])) % mod
            self.base_pow[i+1] = (self.base_pow[i] * base) % mod

    def get_hash(self, l: int, r: int) -> int: # get hash value of the substring: s[l:r]
        hash_val = self.hash_cum[r] - self.hash_cum[l] * self.base_pow[r-l] % self.mod
        if hash_val < 0:
            hash_val += self.mod
        return hash_val


class RollingHashMulti:
    def __init__(self, s: str, base_list: list=[1007, 2009], mod_list: list=[10**9+7, 10**9+9]):
        self.n = len(base_list)
        self.base_list = base_list
        self.mod_list = mod_list
        self.rh_list = [RollingHash(s, base_list[i], mod_list[i]) for i in range(self.n)]

    def get_hash(self, l: int, r: int) -> tuple:
        return tuple( self.rh_list[i].get_hash(l, r) for i in range(self.n) )

```


```python
class RollingHash2D:
    def __init__(self, s, n, m, b=1007, c=2009, mod=10**9 + 7):
        self.s = s
        self.n = n
        self.m = m
        self.b = b
        self.c = c
        self.mod = mod

        # preprocess
        self.hash_cs = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        self.b_pow = [1] * (self.n + 1)  # base_pow[i] = base ** i
        self.c_pow = [1] * (self.m + 1)  # base_pow[i] = base ** i
        for i in range(self.n):
            self.b_pow[i + 1] = (self.b_pow[i] * self.b) % mod
        for i in range(self.m):
            self.c_pow[i + 1] = (self.c_pow[i] * self.c) % mod

        for i in range(self.n):
            for j in range(self.m):
                self.hash_cs[i + 1][j + 1] = \
                    self.hash_cs[i + 1][j] * self.c \
                    + self.hash_cs[i][j + 1] * self.b \
                    - self.hash_cs[i][j] * self.b * self.c \
                    + self.s[i][j]
                self.hash_cs[i + 1][j + 1] %= self.mod

    def calc_rolling_hash(self, il: int, ir: int, jl: int, jr: int) -> int:
        hash_val = \
            self.hash_cs[ir][jr] \
             - self.hash_cs[ir][jl] * self.c_pow[jr-jl] \
             - self.hash_cs[il][jr] * self.b_pow[ir-il] \
             + self.hash_cs[il][jl] * self.b_pow[ir-il] * self.c_pow[jr-jl]
        hash_val %= self.mod
        return hash_val

    def calc_hash(self, t, nt, mt):
        h = 0
        for i in range(nt):
            for j in range(mt):
                h += t[i][j] * self.b_pow[nt - i - 1] * self.c_pow[mt - j - 1]
                h %= self.mod
        return h
```
ToDo
* `RollingHashBase`という基底クラスを作って、`RollingHashStr`と`RollingHashStrMulti`と`RollingHash2dim`をそれを継承したクラスとして実現する

問題
* [ABC054 B - Template Matching (200点)]( https://atcoder.jp/contests/abc054/tasks/abc054_b )
    * 二次元のRollingHashでも解ける
* [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )
    * RollingHashと二分探索
* [ABC150 F - Xor Shift (600点)]( https://atcoder.jp/contests/abc150/tasks/abc150_f )
    * 数列の比較をRollingHashで行う問題
