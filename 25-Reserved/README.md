## [25. Reserved](http://ksnctf.sweetduet.info/problem/25)

タイトルからして、このコードらしき文字列には何らかのプログラミング言語の予約語が多く含まれているのだろう。
特徴的な `getservbyname`, `setnetent`, `endprotoent` でググると、Perlの組み込み関数であることが分かる。
その他の単語もPerlのものらしい。

そこで、Perlでこのコードを実行してみるとflagを得る。

Flagと同時に表示されるものを調べると元ネタが分かる。
