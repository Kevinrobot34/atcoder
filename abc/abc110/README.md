## ABC110

### D - Factorization
素因数分解して，Combinationの計算をする．

#### 素因数分解
* https://en.wikipedia.org/wiki/Trial_division
```cpp
map<int,int> factorize(int m) {
    map<int, int> factor;

    while (m % 2 == 0) {
        factor[2]++;
        m /= 2;
    }

    int p = 3;
    while (p * p <= m) {
        if (m % p == 0) {
            factor[p]++;
            m /= p;
        } else {
             p += 2;
        }
    }

    if (m != 1) factor[m]++;
    return factor;
}
```

#### Combinationの計算
* http://drken1215.hatenablog.com/entry/2018/06/08/210000
