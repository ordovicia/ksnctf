## [21. Perfect Cipher](http://ksnctf.sweetduet.info/problem/21)

`encrypt.cpp` を読むと、`encrypt.cpp` を `encrypt.enc` に暗号化し、直後に `flag.jpg` を `flag.enc` に暗号化しているようだ。
`flag.jpg` を復元することを目指せばよいだろう。

暗号化には、`seed` というファイルの中身を初期シードとした
[Mersenne twister](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%AB%E3%82%BB%E3%83%B3%E3%83%8C%E3%83%BB%E3%83%84%E3%82%A4%E3%82%B9%E3%82%BF) が使われている。
MTで生成した疑似乱数と平文をワード（4バイト）ごとXORして暗号化している。
`encrypt.cpp`, `encrypt.enc` は与えられているので、XORをかけ直すことで `encrypt.cpp` の暗号化に使った疑似乱数列は復元できる。

したがって、この疑似乱数列から

* 初期シードを復元する、または
* 後続の疑似乱数列を推測する

ことを考える。
残念ながら前者はできないようだが、後者は疑似乱数列が連続する624ワードあれば可能である。
[Mersenne Twisterの出力を推測してみる - ももいろテクノロジー](http://inaz2.hatenablog.com/entry/2016/03/07/194147) に詳しい。
そして幸いにも `encrypt.cpp` は624ワードより長い。

この方針で実装し、`flag.jpg` を復元する。
`flag.jpg` 自体は壊れたJPEGになるようだが、EXIF情報の復元には成功し、EXIFのコメントにflagが書いてある。

* [Python版](https://github.com/ordovicia/ksnctf/blob/master/21-Perfect_Cipher/solve.py)

実さ装上の注意点として、暗号ファイルの先頭にはそのサイズが書き込まれるので、これを復元に使わないこと。
