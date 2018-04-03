## [14. John](http://ksnctf.sweetduet.info/problem/14)

与えられた文書は、`/etc/passwd` のフォーマットのように見える。
`user00` の暗号化されたパスワードが `$6$Z4xEy/1KTCW.rz$Yxkc8XkscDusGWKan621H4eaPRjHc1bkXDjyFtcTtgxzlxvuPiE1rnqdQVO1lYgNOzg72FU95RQut93JF6Deo/` である。

文書を最後まで読んでみると、`user99` のパスワードが実際には出題者からのメッセージであることが分かる。
`$6$SHA512IsStrong$DictionaryIsHere.http//ksnctf.sweetduet.info/q/14/dicti0nary_8Th64ikELWEsZFrf.txt`
とのことなので、パスワードがSHA512で暗号化されているらしい。
また、メッセージに含まれているファイルが `dicti0nary_8Th64ikELWEsZFrf` とのことなので、これを辞書として辞書攻撃をすれば良さそうだ。

辞書に含まれている文字列を `sha512sum` しても、もとの文書にあるパスワードには一致するものは現れない。
そもそも暗号化されたパスワードは数値ではないので、SHA512そのものではない。

問題のタイトルがヒントになることがある。
"John SHA512" とかでググると、"John the Ripper" なるパスワードクラッキングツールがヒットするので、これを試してみる。

`dicti0nary_8Th64ikELWEsZFrf` を辞書として、与えられた `/etc/passwd` を解析する。
（`fork` は並列度を指定する。環境に合わせて適当に。）

```console
$ john --wordlist=dicti0nary_8Th64ikELWEsZFrf.txt passwd.txt --fork=4
```

すこし待つと解析が終了し、 `$ john passwd.txt --show` で結果が表示される。
`user00` から `user03` までのパスワードの頭をつなげると `FLAG` となっているので、`user20` までの頭をつなげればflagを得る。
