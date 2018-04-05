## [16. Math I](http://ksnctf.sweetduet.info/problem/16)

RSA暗号の問題。
RSA暗号は、平文 $m$ から $c = m^e % n$ と暗号化するが、$n$ を素因数分解した $p, q$ が漏れると $m = c^d % n$ の $d$ が計算でき、解読されてしまう。

計算方法は [RSA暗号に関するWikipediaの記事](https://ja.wikipedia.org/wiki/RSA%E6%9A%97%E5%8F%B7) に書いてあるとおりで、
[拡張ユークリッドの互除法](https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E3%81%AE%E4%BA%92%E9%99%A4%E6%B3%95#%E6%8B%A1%E5%BC%B5%E3%81%95%E3%82%8C%E3%81%9F%E4%BA%92%E9%99%A4%E6%B3%95) を用いる。

* [Rust版](https://github.com/ordovicia/ksnctf/blob/master/16-Math_I/solve.rs)
* [Python**3**版](https://github.com/ordovicia/ksnctf/blob/master/16-Math_I/solve.py)
