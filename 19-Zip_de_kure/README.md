## [19. ZIP de kure](http://ksnctf.sweetduet.info/problem/19)

与えられたZIPファイルには鍵がかかっている。

```
$ unzip flag.zip
Archive:  flag.zip
Hint:
- It is known that the encryption system of ZIP is weak against known-plaintext attacks.
- We employ ZIP format not for compression but for encryption.
[flag.zip] flag.html password:
   skipping: flag.html               incorrect password
   skipping: Standard-lock-key.jpg   incorrect password
```

ヒントにある通り、ZIPの暗号化は既知平文攻撃に対して弱い。
この脆弱性を利用するツールとしてPkCrackがあり、これを使って本問が解ける。

既知平文攻撃は、暗号化されたZIPファイル内のあるファイルが平文でわかっている場合に適用できる。
今回は `flag.html` か `Standard-lock-key.jpg` のどちらかが分かっていないといけないが、`flag.html` はおそらくflagそのものなので分からない。
そこで "Standard-lock-key" でググると、このファイルがインターネット上で見つかる。
ダウンロードしてきて、PkCrackを動かせばflagを得る。

```console
$ pkcrack -C flag.zip -c Standard-lock-key.jpg -p ./Standard-lock-key.jpg -d answer.zip
```
