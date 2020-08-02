# 数学
## 簡単な計算
* 切り上げ
    * `math.ceil`
    * 自分で書く
        ```python
        (b + a - 1) // a
        ```
        * `b/a`の切り上げ
* 切り捨て
    * `math.floor`
    * `b//a`
    * 自分で書く
        ```python
        (b - b % a) // a
        ```
        * `b/a`の切り捨て
* 四捨五入
    ```python
    def round(x, d=0):
        x *= 10**d
        x = (x * 2 + 1) // 2
        x /= 10**d
        return x
    ```
    * Pythonの組み込み関数の[round(x)]( https://docs.python.org/ja/3/library/functions.html?highlight=round#round )だと[偶数への丸め]( https://ja.wikipedia.org/wiki/%E7%AB%AF%E6%95%B0%E5%87%A6%E7%90%86#%E5%81%B6%E6%95%B0%E3%81%B8%E3%81%AE%E4%B8%B8%E3%82%81%EF%BC%88round_to_even%EF%BC%89 )になっているので注意。


## 数値誤差について
* プログラム上では実数は近似的に扱われているので、なるべく整数で扱っちゃうのが良い
* 許容される誤差の範囲内で正しく動くプログラムを作る方法について
    * 幾何の方も要参照
    * Under construction

問題
* [Panasonic2020 C - Sqrt Inequality (300点)]( https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_c )
    * なるべく整数でいけるときはそうするのが楽と言うのがよくわかるいい問題
* 幾何の問題も要参照


## 期待値
問題
* [ABC008 C - コイン]( https://atcoder.jp/contests/abc008/tasks/abc008_3 )


## 約数
正整数$`n`$の約数の一覧は$`O(\sqrt{n})`$で取得できる。
```python
def get_divisor(n: int) -> list:
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor.append(i)
            if n // i != i:
                divisor.append(n // i)
    # divisor.sort() # if you want sorted divisors
    return divisor
```

## GCD / LCM
キーワード : GCD(最大公約数 - Greatest Common Divisor), LCM(最小公倍数 - Least Common Multiple), ユークリッドの互除法
```cpp
int GCD(int a, int b) { return b ? GCD(b, a % b) : a; }
int LCM(int a, int b) { return a * b / GCD(a, b) }
```
```python
def GCD(a:int , b: int) -> int:
    return a if b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)    
```
* Python3.5以降には`math`にgcdは実装してある。https://docs.python.org/ja/3/library/math.html#math.gcd
    * ただし、Python3.4.3では最大公約数を求めるgcdは”math"ではなくて、"fractions"の中にある: `from fractions import gcd`

問題
* [ABC131 C - Anti-Divisor (300点)]( https://atcoder.jp/contests/abc131/tasks/abc131_c )
* [ABC125 C - GCD on Blackboard (300点)]( https://atcoder.jp/contests/abc125/tasks/abc125_c )
    * 複数の数に対するGCD
* [ABC150 D - Semi Common Multiple (400点)]( https://atcoder.jp/contests/abc150/tasks/abc150_d )
* [JSUTC202004 D - Calculating GCD (400点)]( https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_d )


## MOD pの世界
* [「1000000007 で割ったあまり」の求め方を総特集！ 〜 逆元から離散対数まで 〜 by drken]( https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a )

競プロではしばしば「〜〜の値をmod $`10^9+7`$した値を答えなさい」といった処理が必要になる。

### Fermatの定理を利用した逆元の計算
$`a\times a^{-1} \equiv 1 ~ (\text{mod} ~p)`$なる$`a^{-1}`$を$`a`$の逆元という。
> **Fermatの小定理**
> $`p`$を素数、$`a`$を$`p`$の倍数でない整数とする時、
> ```{latex}
> a^{p-1} \equiv 1 ~ (\text{mod} ~p)
> ```
Fermatの小定理より、
```{latex}
\begin{align*}
    a^{p-1} &\equiv 1 ~ (\text{mod} ~p) \\
    \Leftrightarrow a \times a^{p-2} &\equiv 1 ~ (\text{mod} ~p)
\end{align*}
```
なので、$`a^{-1} \equiv a^{p-2} (\text{mod} ~p)`$である。
よって、pythonでは組み込み関数の[pow](https://docs.python.org/ja/3/library/functions.html#pow)を用いて以下のように逆言を求めることができる。
```python
def modinv(x: int, mod: int) -> int:
    return pow(x, mod - 2, mod)
```
時間計算量は繰返し二乗法で冪乗を計算すれば、$`O(\log \text{MOD})`$。

問題
* [ABC024 D - 動的計画法]( https://atcoder.jp/contests/abc024/tasks/abc024_d )

### 拡張Euclidの互除法を利用した逆元の計算
* [AOJ - Extended Euclid Algorithm]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=jp )


## 素数
### 素因数分解
正整数$`n`$の素因数分解は[Trial-Division]( https://en.wikipedia.org/wiki/Trial_division )と呼ばれるナイーブなアルゴリズムで$`O(\sqrt{n})`$で可能。
また一般に、正整数$`n`$の素因数の個数は$`O(\log n)`$。
```python
from collections import defaultdict
def factorize(n: int) -> dict:
    f = defaultdict(int)
    while n % 2 == 0:
        f[2] += 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            f[p] += 1
            n //= p
        p += 2
    if n != 1:
        f[n] += 1
    return f
```
問題
* [ABC052 C - Factors of Factorial (300点)]( https://atcoder.jp/contests/abc052/tasks/arc067_a )
* [ABC142 D - Disjoint Set of Common Divisors (400点)]( https://atcoder.jp/contests/abc142/tasks/abc142_d )


### 素数判定
ある正整数$`n`$が素数であるかは$`O(\sqrt{n})`$で判定可能。
```python
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True
```

問題
* [ABC149 C - Next Prime (300点)]( https://atcoder.jp/contests/abc149/tasks/abc149_c )
* [ARC044 A - 素数判定]( https://atcoder.jp/contests/arc044/tasks/arc044_a )
    * $` \mathbb{N} = \{1\} ~\cup~ \{\text{Prime number}\} ~\cup~ \{\text{Composite number}\} `$


### エラトステネスの篩
$`n`$までの素数を$`O(n\log\log n)`$で求められるアルゴリズム。
1. 2から$`n`$までの整数の配列を用意し全てTrueにする。
2. 小さい方から順に数字を見て`True`である数字は素数とみなす。その数字の倍数に対応する要素は`False`にする。
3. 2.を繰り返して行く。

オーダーは、$`n`$以下の素数の逆数和が$`O(\log\log n)`$であることから従う
（参考：[素数の逆数和が発散することの証明]( https://mathtrain.jp/primeinverse )）。
境界条件がちょっとだけ面倒なので、$`n`$ではなく大きな数字を入れておくとバグりにくいかも。
```python
def eratosthenes(n: int) -> list:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n // 2 + 1):
        if is_prime[i]:
            for j in range(2, n // i + 1):
                is_prime[i * j] = False
    return is_prime
```

問題
* [ABC084 D - 2017-like Number (400点)]( https://atcoder.jp/contests/abc084/tasks/abc084_d )
* [ABC170 D - Not Divisible (400点)]( https://atcoder.jp/contests/abc170/tasks/abc170_d )


## Permutation
```python
def perm(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    ans = 1
    for i in range(n - k + 1, n + 1):
        ans *= i
    return ans
```

自分で再帰とかで書いても良いけど、permutationとかの生成にはitertoolsが便利。
* https://docs.python.org/ja/3/library/itertools.html
* **ToDo** 早いのかどうか確認
```python
from itertools import permutations
for p in permutations(range(3)):
    print(p)
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)
```

## Combination with replacement
いわゆる重複組み合わせ
$`n`$種類のものから重複を許して$`r`$個選ぶ場合の数は$`_{n+r-1}C_{r}`$通りだが、この選び方を全列挙する方法はいくつかある。

* [itertools.combinations_with_replacement]( https://docs.python.org/ja/3/library/itertools.html#itertools.combinations_with_replacement )
    * 具体例
       ```python
       from itertools import combinations_with_replacement
       n = 3
       r = 2
       for l in combinations_with_replacement(range(1, n + 1), r):
           print(l)
       # (1, 1)
       # (1, 2)
       # (1, 3)
       # (2, 2)
       # (2, 3)
       # (3, 3)
       ```
* 自分でdfsして構成する

問題
* [ABC165 C - Many Requirements (300点)]( https://atcoder.jp/contests/abc165/tasks/abc165_c )


## Combination
```{latex}
 _nC_k = \frac{n!}{k!(n-k)!} = \frac{n}{1} \cdot \frac{n-1}{2} \cdot \frac{n-2}{3} \cdot ~\cdots~ \cdot \frac{n-k+1}{k}
```

$`{}_nC_k`$の計算は以下のような単純な実装だと$`O(\min(k, n-k))`$かかる。
```python
def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans
```



複数回のcombinationの計算やそのmodを取る処理を効率よく行うには工夫が必要。

### DPによる計算
```{latex}
{}_{n+1}C_k = {}_nC_k +  {}_nC _{k-1}
```
という関係式を利用して、combinationのテーブルを作る方法。
パスカルの三角形的な表を上の漸化式で作るという話。
$`n\leq N`$の範囲で、テーブルを作る前処理に$`O(N^2)`$、$`{}_n C_k`$の計算に$`O(1)`$の時間がかかる。

### Fermatの小定理を利用した高速な計算
```{latex}
 _nC_k = n! \times (k!)^{-1} \times ((n-k)!)^{-1}  
```
上記の式より、階乗とその逆元の事前計算をしておくことで高速にcombinationができるようになる。
以下のFermatの小定理を使うことで、「素数$`p`$を法とする(mod $`p`$ の時)時、ある整数$`a`$の逆元は$`a^{p-2}`$であることがわかる」ということがポイント。
> **Fermatの小定理**
> $`p`$を素数、$`a`$を$`p`$の倍数でない整数とする時、
> ```{latex}
> a^{p-1} \equiv 1 ~ (\text{mod} ~p)
> ```
> [ $`\Rightarrow`$  $`p`$を素数、$`a`$を任意の整数とする時、$`a^p \equiv a ~ (\text{mod} ~p) `$ ]

```python
MOD = 10**9 + 7
MAX = 2000 + 5
fact = [1] * MAX
finv = [1] * MAX
for i in range(2, MAX):
    fact[i] = fact[i - 1] * i % MOD
    finv[i] = pow(fact[i], MOD-2, MOD)

def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n-k] % MOD
```
この方法だと$`n\leq N`$なる$`{}_n C_k`$の計算をできるようにするために、前処理で$`O(N\log \text{MOD})`$、$`{}_n C_k`$の計算で$`O(1)`$の時間がかかる。

このままだと$`a!`$の逆元計算部分の`pow`が遅い。
* $`\text{MOD}=10^9+7`$に対して、$`(a!)^{\text{MOD}-2}`$を計算しないといけない。
* ダブリング使った実装だとしても$`O(\log \text{MOD})`$かかる（多分）。


### 更なる高速化
実はこの$`a!`$の逆元計算はさらに高速化できる。まず$`(a!)^{-1} = ((a-1)!)^{-1} \cdot a^{-1}`$と表せるので、$`a^{-1}`$が高速に計算できれば再帰的に$`(a!)^{-1} `$の計算が高速にできることになる。
ここで、以下合同式は全てmod $`p`$として、

```{latex}
\begin{align}
&p = (p//a) \cdot a + (p\%a) \\
\Leftrightarrow~ & (p//a) \cdot a + (p\%a) \equiv 0 \\
\Leftrightarrow~ & (p \% a) \equiv -(p//a) \cdot a  \\
\Leftrightarrow~ & (p \% a) \cdot a^{-1}  \equiv -(p//a)   \\
\Leftrightarrow~ & a^{-1}  \equiv - (p\%a)^{-1} \cdot (p//a)
\end{align}
```


（最初の式は$`p`$を$`a`$で割った商と余りに分けただけの式）
と表せる。$`(p \% a) < a`$であることに注意すると、上式を用いれば$`a^{-1}`$は1から順次高速に計算できることが分かる。
http://drken1215.hatenablog.com/entry/2018/06/08/210000
```cpp
const int MAX = 510000;
const int MOD = 1000000007;
long long int fac[MAX], finv[MAX], inv[MAX];
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

long long int COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}
```
```python
MOD = 10**9 + 7
MAX = 7 * 10**5
fact = [1] * (MAX + 1)  # i!
finv = [1] * (MAX + 1)  # (i!)^{-1}
iinv = [1] * (MAX + 1)  # i^{-1}
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD

def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n - k] % MOD
```
この方法だと$`n\leq N`$なる$`{}_n C_k`$の計算をできるようにするために、前処理で$`O(N)`$、$`{}_n C_k`$の計算で$`O(1)`$の時間がかかる。


### 前処理しないシンプルな実装
```{latex}
_nC_k = \frac{n}{1} \cdot \frac{n-1}{2} \cdot \frac{n-2}{3} \cdot ~\cdots~ \cdot \frac{n-k+1}{k}  = \prod _{i=1}^{k} (n-i+1)\cdot i^{-1}
```

combinationを**1回求めるだけ**なら以下でもOK。
上記のcombinationの表式を前から愚直に計算していくと同時に、$`i^{-1}`$を求めていく。
$`{}_nC_k`$の計算に$`O(\min(k, n-k))`$かかる。
```python
def comb(n: int, k: int, MOD: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1
    iinv = [1] * (k + 1)
    ans = n
    for i in range(2, k + 1):
        iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
        ans *= (n + 1 - i) * iinv[i] % MOD
        ans %= MOD
    return ans
```


問題
* [ABC011 D - 大ジャンプ]( https://atcoder.jp/contests/abc011/tasks/abc011_4 )
    * 立式自体は正統だが、確率を計算できるように$`\frac{_n C_k}{2^n}`$を計算する
* [ABC034 C - 経路]( https://atcoder.jp/contests/abc034/tasks/abc034_c )
* [ABC042 D - いろはちゃんとマス目 / Iroha and a Grid (400点)]( https://atcoder.jp/contests/abc042/tasks/arc058_b )
* [ABC110 D - Factorization (400点)]( https://atcoder.jp/contests/abc110/tasks/abc110_d )
* [ABC132 D - Blue and Red Balls (400点)]( https://atcoder.jp/contests/abc132/tasks/abc132_d )
* [ABC145 D - Knight (400点)]( https://atcoder.jp/contests/abc145/tasks/abc145_d )
* [ABC151 E - Max-Min Sums (500点)]( https://atcoder.jp/contests/abc151/tasks/abc151_e )
* [ABC154 F - Many Many Paths (600点)]( https://atcoder.jp/contests/abc154/tasks/abc154_f )
* [ABC156 D - Bouquet (400点)]( https://atcoder.jp/contests/abc156/tasks/abc156_d )
* [ABC156 E - Roaming (500点)]( https://atcoder.jp/contests/abc156/tasks/abc156_e )
* [ABC167 E - Colorful Blocks (500点)]( https://atcoder.jp/contests/abc167/tasks/abc167_e )
* [ABC171 F - Strivore (600点)]( https://atcoder.jp/contests/abc171/tasks/abc171_f )
* [ARC039 B - 高橋幼稚園]( https://atcoder.jp/contests/arc039/tasks/arc039_b )


## 数え上げ
問題
* [ABC150 E - Change a Little Bit (500点)]( https://atcoder.jp/contests/abc150/tasks/abc150_e )
* [ABC168 E - ∙ (Bullet) (500点)]( https://atcoder.jp/contests/abc168/tasks/abc168_e )

### 完全順列
撹乱順列とも。
数字の並びを完全にかくらんする（もとと同じ場所になる要素がない）順列のこと。
* [高校数学の美しい物語 - 攪乱順列の公式]( https://mathtrain.jp/montmort )


1から $`n`$ の順列 $`\{ p_i | i = 1, 2, \cdots, n \}`$ を考える。
任意の $`i`$ に対して、 $`p_i \neq i`$ であるような順列の個数を $`a_n`$ とすると以下の漸化式が成り立ち、 $`a_n`$ が求まる。
```{latex}
\begin{align*}
a_n &= n! \sum_{k=2}^{n} \frac{(-1)^k}{k!}  \\
a_n &= (n-1) (a_{n-1} + a_{n-2})
\end{align*}
```
* 要は $`[1,2,3,\cdots, n]`$を並び替え方は $`n!`$ 通りあるが、そのうち場所が変わっていない要素がないようなものは何通りあるかという話。
* $`a_n`$はモンモール数と呼ばれている。

問題
* [ABC172 E - NEQ (500点)]( https://atcoder.jp/contests/abc172/tasks/abc172_e )
* [ARC009 C - 高橋君、24歳]( https://atcoder.jp/contests/arc009/tasks/arc009_3 )

#### 漸化式について
「1がどこに移るか」という観点で考えると漸化式を立てやすい。
1の移動先を$`x`$とする。

1. $`x`$の移動先が1であるようなパターン
    * 以下のような表のイメージ
        | $`i`$ | $`1`$ | $`\cdots`$ | $`x`$ | $`\cdots`$ | $`n`$ |
        |:---:|:---:|:---:|:---:|:---:|:---:|
        | $`p`$ | $`x`$ | ? | $`1`$ | ? | ? |
    * ?は $`n-2`$個あり、$`1`$と$`x`$以外の$`n-2`$個の数が配置される
    * この$`n-2`$個が撹乱順列となっていれば良い
        * $`a_{n-2}`$通り
2. $`x`$の移動先が 1 **以外** であるようなパターン
    * 以下のような表のイメージ
        | $`i`$ | $`1`$ | $`2`$ | $`\cdots`$ | $`y`$ | $`\cdots`$ | * $`x`$ | $`\cdots`$ | $`n-1`$ | $`n`$ |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        | $`p`$ | $`z`$ | ? | ? | $`x`$ | ? | * $`1`$ | ? | ? | ? |
        * $`y \neq 1, x`$
        * $`z \neq 1, x`$
    * ポイント
        * アスタリスクのついている部分は今の仮定なので無視
        * 下段の$`p`$において、
            * $`x`$は$`i=1`$の位置(左端)にいってはいけない
            * その他の数$`a (\neq 1, x)`$はそのままで、$`i=a`$の場所にはいけない
    * 以上を踏まえると、上段について$`1`$を$`x`$と置き換えると分かりやすく、実質$`1`$以外の$`n-1`$個の数について撹乱順列を作ればよいことがわかる

        | $`i`$ | $`x`$ ~1~ | $`2`$ | $`\cdots`$ | $`y`$ | $`\cdots`$ | ( * $`x`$ ) | $`\cdots`$ | $`n-1`$ | $`n`$ |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        | $`p`$ | $`z`$ | ? | ? | $`x`$ | ? | ( * $`1`$ ) | ? | ? | ? |
        * 丸カッコ()以外の部分で撹乱順列を作れば良いと言うこと
        * $`a_{n-1}`$通り

以上より、$`x`$は1以外の全てを取りうるので、
```{latex}
\begin{align*}
a_n &= (n-1) (a_{n-1} + a_{n-2})
\end{align*}
```

#### 漸化式の解き方
* [高校数学の美しい物語 - 階乗を用いる漸化式の解法]( https://mathtrain.jp/bikkurizenka )
* [完全順列と包除原理]( https://igaris.hatenablog.com/entry/20110318/1300437620 )


#### 包除原理で求める
まず補集合を考えることで、$`a_n=n! ~-`$ (完全順列でない順列の総数) と表せることがわかる。

完全順列でない順列について考える。$`B_i = \{ p ~|~ p_i = i \} `$、つまり$`i`$番目が$`i`$であるような順列の集合とする。
ちなみに
* $`|B_i| = (n-1)!`$
* $`|B_i \cap B_j| = (n-2)! ~~~(i \neq j)`$
    * $`i`$と$`j`$は動いていないような順列の総数

である。
一方「完全順列でない順列の総数」は $` | B_1 \cup B_2 \cup \cdots \cup B_n | `$ で、包除原理が使えそうな形！

```{latex}
\begin{align*}
& | B_1 \cup B_2 \cup \cdots \cup B_n | \\
=
& ~~ (|B_1| + |B_2| + \cdots + |B_n|) \\
& - (|B_1 \cap B_2| + |B_1 \cap B_3| + \cdots + |B_{n-1} \cap B_n|) \\
& + (|B_1 \cap B_2 \cap B_3| + \cdots + |B_{n-2} \cap B_{n-1} \cap B_n|) \\
& - \cdots \\
& (-1)^{n-1} (|B_1 \cap B_2 \cap B_3 \cap \cdots \cap B_n|) \\
= & \sum_{k=1}^{n} (-1)^{k-1} (n-k)! ~ _n\mathrm{C}_k \\
= & \sum_{k=1}^{n} (-1)^{k-1} \frac{n!}{k!}
\end{align*}
```
以上より、$`a_n`$が求まった。



### 包除原理
* [高校数学の美しい物語 - 包除原理の２通りの証明]( https://mathtrain.jp/hojo )
* [「写像12相」を総整理！ 〜 数え上げ問題の学びの宝庫 〜]( https://qiita.com/drken/items/f2ea4b58b0d21621bd51 )

問題
* [ABC152 F - Tree and Constraints (600点)]( https://atcoder.jp/contests/abc152/tasks/abc152_f )
* [ABC172 E - NEQ (500点)]( https://atcoder.jp/contests/abc172/tasks/abc172_e )



## 三分探索
references
* [三分探索( Ternary search )]( https://en.wikipedia.org/wiki/Ternary_search )
* [三分探索を救いたい]( https://qiita.com/ganariya/items/1553ff2bf8d6d7789127 )
* http://kyopro.hateblo.jp/entry/2019/04/25/134128

三分探索は、ただ一つ極値を持つ関数の極値を探索するアルゴリズム。

```python
def func(x):
    pass

left = 0.0
right = 10**8
while right - left > 1e-8:
    c1 = (2 * left + right) / 3
    c2 = (left + 2 * right) / 3
    if func(c1) < func(c2):
        right = c2
    else:
        left = c1
```

問題
* [ARC049 B - 高橋ノルム君]( https://atcoder.jp/contests/arc049/tasks/arc049_b )
* [ARC054 B - ムーアの法則]( https://atcoder.jp/contests/arc054/tasks/arc054_b )


## bit演算
### bin
組み込み関数の[bin]( https://docs.python.org/ja/3/library/functions.html#bin )を使うと、簡単に整数を先頭に "0b" が付いた 2 進文字列に変換できる。
```python
bin(3)
# '0b11'
bin(-10)
# '-0b1010'
```

* 整数`x`の2進数表示した時の1の数は`bin(x).count('1')`


### 最下位bit (Least Significant Bit)
整数`x`の最下位の1bit分だけ取り出す
* `(x & (-x))`
* 負の数は「全てのbitを反転して1を足す」という補数で表現されていることを利用した技
    * BITの実装などに使える

| $`x_{(10)}`$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $`x_{(2)}`$                  | 00001 | 00010 | 00011 | 00100 | 00101 | 00110 | 00111 | 01000 |
| $`-x_{(2)}`$                | 11111 | 11110 | 11101 | 11100 | 11011 | 11010 | 11001 | 11000 |
| $`(x \& -x)_{(2)}`$ | 00001 | 00010 | 00001 | 00100 | 00001 | 00010 | 00001 | 01000 |


### 最上位bit (Most Significant Bit)
```python
def msb(x):
    cnt = 0
    while x:
        x >>= 1
        cnt += 1
    return cnt
```
* [Re: 明日使えないすごいビット演算]( https://rsk0315.hatenablog.com/entry/2019/11/02/064952 )

### bit演算テクニック
* `x|y = x + y - (x & y)`
* `x^y = x + y - 2*(x & y)`


### XOR
https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a

XOR関連の問題はDPなどと合わせて出たり、数学の問題として出ることが多々ある。
XORの性質について知っていると便利なことも多い。
以下$`\land`$をビットワイズなXORを表す演算子とする。


| $`a`$ | $`b`$ | $`a \land b`$ |
| --- | --- | --------------- |
| 0   | 0   | 0               |
| 0   | 1   | 1               |
| 1   | 0   | 1               |
| 1   | 1   | 0               |

* 基本的な性質
    * 2進数として表した時にbit毎に独立な演算
    * 可換 : $`a \land b =  b \land a`$
    * 結合律 : $`a \land (b \land c) = (a \land b) \land c`$
    * 単位元 : 0
    * 逆元 : $`a`$の逆元は$`a`$自身。つまり$`a \land a = 0`$
        * $`a  \land x \land x = a`$
        * つまりある$`a,b`$に対して$`a \land x = b`$なる$`x`$は、$`x = a \land b`$
* $`a \land b \leq a + b`$
* 任意の$`n`$について$`2n \land (2n+1) = 1`$
    * $`2n`$と$`2n+1`$は最下位bit以外は全て一致している -> 最下位bit以外についてはXor取ると0
    * 最下位のbitは0と1なので、1
* 任意の$`n`$について$`4n \land (4n+1) \land (4n+2) \land (4n+3) = 0`$
    * $`4n`$と$`4n+1`$と$`4n+2`$と$`4n+3`$は2進数で考えたとき、下2桁以外は全て$`4n`$で一致している -> Xor取ると、下２桁以外は全て0
    * 下２桁、つまり $`0 \land 1 \land 2 \land 3`$はよく考えると0
* $`x' = x \land a`$、$`y' = y \land a`$の時、
  ```{latex}
  x' \land y' = (x \land a) ~ \land ~ (y \land a) = (x \land y) ~ \land ~ (a \land a) = x \land y
  ```
* 2つの数列$`\{a_i \}`$と$`\{b_i \}`$が一致するということは以下のようにいくつかの言い方ができる
    * $`\forall i ~, ~ a_i = b_i`$
    * 初項が一致し、階差数列( $`a_i^\prime = a_{i+1} - a_i ~,~~b_i^\prime = b_{i+1} - b_i`$ )が一致する。
        * $`a_0 = b_0`$
        * $`\forall i ~, ~ a_i^\prime = b_i^\prime`$
            * $`a_i = (a_{i} - a_{i-1} ) + (a_{i-1} - a_{i-2} ) + \cdots + (a_{1} - a_{0} ) + a_0`$
    * 初項が一致し、Xor階差数列( $`a_i^{\prime\prime} = a_{i+1} \land a_i ~,~~ b_i^{\prime\prime} = b_{i+1} \land b_i`$ )
        * $`a_0 = b_0`$
        * $`\forall i ~, ~ a_i^{\prime\prime} = b_i^{\prime\prime}`$
            * $`a_i = (a_{i} \land a_{i-1} ) ~\land~ (a_{i-1} \land a_{i-2} ) ~\land \cdots \land~ (a_{1} \land a_{0} ) ~\land~ a_0`$

問題
* [ABC117 D - XXOR (400点)]( https://atcoder.jp/contests/abc117/tasks/abc117_d )
* [ABC121 D - XOR World (400点)]( https://atcoder.jp/contests/abc121/tasks/abc121_d )
* [ABC129 E - Sum Equals Xor (500点)]( https://atcoder.jp/contests/abc129/tasks/abc129_e )
* [ABC150 F - Xor Shift (600点)]( https://atcoder.jp/contests/abc150/tasks/abc150_f )
* [ABC171 E - Red Scarf (500点)]( https://atcoder.jp/contests/abc171/tasks/abc171_e )


### 有限体`F2`上の演算としてのXOR
2を法とした余りに注目した集合$`F_2 = \mathbb{Z}/2\mathbb{Z}`$上の演算としてXORは捉えることができる。
$`F_2`$上の加法がXORで乗法がANDということになる。
```{csv}
+(XOR), 0, 1
0, 0, 1
1, 1, 0
```

```{csv}
x(AND), 0, 1
0, 0, 0
1, 0, 1
```

#### 基底
例えば32bit整数の空間は、線形空間としては$`F_2^{32}`$として捉えることができ、
$`e_i = 2^i`$として、例えば$`\{ e_i ~|~ i=0, 1,\cdots, 31 \}`$が基底になる。
実際、任意の32bit整数$`a`$は $`a_i \in \{0, 1\}`$として
```{latex}
a = \left(a_0 \& e_0 \right) \land \left(a_1 \& e_1 \right) \land \cdots \land \left(a_{31} \& e_{31} \right)
```
と一意に表せる。

ある基底$`\{ e_i ~|~ i=1,2,\cdots, n \}`$に注目すると、これらの数の最上位ビット(MostSignificantBit)


#### 線型独立・線形従属
$`n`$個の整数$`\{ e_i ~|~ i=1,2,\cdots, n \}`$の張る線形空間($`F_2^{32}`$の部分線形空間)に注目する
$`x`$がこの線形空間の元かどうかを考える。
つまり、$`\{x\} \cup \{ e_i ~|~ i=1,2,\cdots, n \}`$が線形従属かどうかを考える。




#### references
* [Gauss-Jordan の掃き出し法と、連立一次方程式の解き方]( https://drken1215.hatenablog.com/entry/2019/03/20/202800 )
* https://betrue12.hateblo.jp/entry/2019/03/18/005750

問題
* [ABC141 F - Xor Sum 3 (600点)]( https://atcoder.jp/contests/abc141/tasks/abc141_f )
* [CodeFlyer D - 数列 XOR (600点)]( https://atcoder.jp/contests/bitflyer2018-final-open/tasks/bitflyer2018_final_d )
* [AGC045 A - Xor Battle (400点)]( https://atcoder.jp/contests/agc045/tasks/agc045_a )


## 複素数
標準ライブラリの[cmath]( https://docs.python.org/ja/3/library/cmath.html )で複素数を扱える。

* 極座標形式で複素数を作る
    ```python
    import cmath
    z = cmath.rect(r, th)
    # z = r * (math.cos(phi) + math.sin(phi)*1j)
    ```
