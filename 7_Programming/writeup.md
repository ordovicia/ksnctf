## [7. Programming](http://ksnctf.sweetduet.info/problem/7)

与えられたC++コードをコンパイルして実行しても、flagは得られない。
このコードは大量の空白があからさまに配置されていて、しかもスペースやタブが入り混じっている。
C++コードとしてではなく、この空白に意味があるはずだ。

そこで [Whitespace](https://ja.wikipedia.org/wiki/Whitespace) というプログラム言語を思い出す。
これはスペースとタブ（と改行）で記述する言語である。

ググってみると、Whitespaceの [インタプリタ・JavaScriptへのトランスパイラ](http://ws2js.luilak.net/interpreter.html) があったので、これに食わせてみる。
[トランスパイル結果](https://github.com/ordovicia/ksnctf/blob/master/7_Programming/converted.js) を実行するとPINの入力が求められる。
トランスパイル結果のコードを読んでみるとPINらしいものがなんとなく分かるので、これを入力するとflagを得る。
