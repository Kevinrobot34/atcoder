# 幾何
* https://www.hamayanhamayan.com/entry/2018/02/27/105814
* https://www.ioi-jp.org/camp/2017/2017-sp_camp-hide.pdf

## 誤差を考慮した計算
* アリ本 P228

誤差を考慮して、計算する必要がある。
```python
EPS = 1e-10
def sgn(a: float):
    if a < -EPS:
        return -1
    elif a > EPS:
        return 1
    else:
        return 0
```

## 平面幾何
### 二次元ベクトルのクラス
```python
import math
EPS = 1e-7
class P2():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.norm = (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def __mul__(self, c: float):
        return P2(self.x * c, self.y * c)

    def __truediv__(self, c: float):
        return P2(self.x / c, self.y / c)

    def __eq__(self, other):
        return (abs(self.x - other.x) < EPS) and (abs(self.y - other.y) < EPS)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def det(self, other) -> float:
        return self.x * other.y - self.y * other.x

    def rot90(self):
        return P2(-self.y, self.x)
```

* complexを使った実装
    * https://atcoder.jp/contests/abc157/submissions/10459719
    * 早いらしい（要検証）


### 円のクラス
```python
class Circle():
    def __init__(self, p: P2, r: float):
        self.p = p  # center of the circle
        self.r = r  # radius of the circle

    def contains(self, p: P2, allow_on_edge: bool) -> bool:
        if allow_on_edge:
            return (self.p - p).norm < self.r + EPS
        else:
            return (self.p - p).norm < self.r - EPS

    def cct(self, other) -> int:
        # count common tangent / 共通接線の数
        if self.p == other.p:
            # center is same
            if abs(self.r - other.r) < EPS:
                return float('inf')  # same
            else:
                return 0  # 内包

        d = other.p - self.p
        if d.norm > self.r + other.r + EPS:
            return 4  # 離れてる
        elif d.norm > self.r + other.r - EPS:
            return 3  # 外接
        elif d.norm > abs(self.r - other.r) + EPS:
            return 2  # 交点2つ
        elif d.norm > abs(self.r - other.r) - EPS:
            return 1  # 内接
        else:
            return 0  # 内包

    def intersection_points_with_circle(self, other) -> list:
        cct = self.cct(other)
        d = other.p - self.p

        if cct == 1:
            # 内接
            if self.r > other.r:
                return [self.p + d * (self.r / d.norm)]
            else:
                return [self.p - d * (self.r / d.norm)]
        elif cct == 3:
            # 外接
            return [self.p + d * (self.r / d.norm)]
        elif cct == 2:
            # 交点2個
            x = (self.r**2 - other.r**2 + d.norm**2) / (2 * d.norm)
            h = math.sqrt(max(self.r**2 - x**2, 0.0))
            v = d.rot90() * (h / d.norm)
            dx = self.p + d * (x / d.norm)
            return [dx + v, dx - v]

        return []
```

### 直線のクラス
```python
class Line():
    def __init__(self, v_dir: P2, b: P2):
        self.v_dir = v_dir  # 方向ベクトル
        self.b = b  # 切片的なベクトル

    def crosspoint(self, other):
        b = other.b - self.b
        c = self.v_dir.det(other.v_dir)
        if sgn(c) == 0:
            # 2つの直線が平行だったら以下を返す
            return False, None
        a = -other.v_dir.rot90().dot(b) / c
        return True, self.v_dir * a + self.b
```

### 3点ABCの位置関係
$`\vec{AB}`$と$`\vec{BC}`$を考えた時に、
* $`\vec{AB}`$から見て$`\vec{BC}`$が左にある時 +1 を
* $`\vec{AB}`$から見て$`\vec{BC}`$が右にある時 -1 を
* それ以外、つまり（誤差の範囲で）平行な時 0 を


返す。
```python
def simple_ccw(a, b, c):
    # Simple Counterclockwise test
    # 3点A-B-Cの順番に見た時、左曲がりか平行か右曲がりかを判定する関数
    return sgn((b - a).det(c - a))
```


### 三角形の外心
```python
def gaisin(p1, p2, p3):
    # 点p1、点p２、点p3を頂点とする三角形の外心を求める関数
    l1 = Line((p2 - p1).rot90(), (p2 + p1).smul(0.5))
    l2 = Line((p3 - p1).rot90(), (p3 + p1).smul(0.5))
    return l1.crosspoint(l2)  # (bool, P2)
```

### 点が線分上にあるか
```python
def on_seg(p1, p2, q) -> bool:
    # 点p1と点p2を端点とする線分上に、点qが乗っているかを判定する関数
    is_online = sgn((p1 - q).det(p2 - q)) == 0
    is_between = sgn((p1 - q).dot(p2 - q)) == -1
    return is_online and is_between
```

### 線分の交差判定
```python
def is_crossing(p1, p2, q1, q2) -> bool:
    # 点p1と点p2を端点とする線分と、点q1と点q2を端点とする線分が交差するかを判定する関数
    if sgn((q2 - q1).det(p2 - p1)) == 0:
        # 誤差の範囲で平行
        return False
    ta = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    tb = (p2 - p1).det(p1 - q1) / (p2 - p1).det(q2 - q1)
    return (0.0 <= ta <= 1.0) and (0.0 <= tb <= 1.0)
```
問題
* [ABC016 D - 一刀両断]( https://atcoder.jp/contests/abc016/tasks/abc016_4 )
* [ARC042 B - アリの高橋くん]( https://atcoder.jp/contests/arc042/tasks/arc042_b )

### 線分の交点
```python
def intersection(p1, p2, q1, q2):
    # 点p1と点p2を端点とする線分と、点q1と点q2を端点とする線分の交点を求める関数
    t = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    return p1 + (p2 - p1).smul(t)
```

### 最小包含円
* [ABC151 F - Enclose All (600点)]( https://atcoder.jp/contests/abc151/tasks/abc151_f )


### 凸包
* [ABC022 D - Big Bang]( https://atcoder.jp/contests/abc022/tasks/abc022_d )


## 偏角ソート
* [ABC033 D - 三角形の分類]( https://atcoder.jp/contests/abc033/tasks/abc033_d )
* [ABC139 F - Engines (600点)]( https://atcoder.jp/contests/abc139/tasks/abc139_f )
