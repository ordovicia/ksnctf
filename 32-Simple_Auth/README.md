## [32. Simple Auth](http://ksnctf.sweetduet.info/problem/32)

PHPのコードが与えられる。
シンプルなコードなので、脆弱性がありそうな箇所についてググってみる。
例えば `strcasecmp()` に目をつけ、"PHP strcasecmp vulnerability" などでググると、[いくつかヒットする](http://danuxx.blogspot.jp/2013/03/unauthorized-access-bypassing-php-strcmp.html)。

PHPの `strcmp()`, `strcasecmp()` には脆弱性があるようだ。
引数に文字列以外、例えば配列を渡すと0が返るらしい。

そこで、`password[]=foo` というデータをPOSTしてみると、`strcasecmp()` をバイパスしてflagを得る。

* [Rust版](https://github.com/ordovicia/ksnctf/blob/master/32-Simple_Auth/solve.rs)
* [Python版](https://github.com/ordovicia/ksnctf/blob/master/32-Simple_Auth/solve.py)
