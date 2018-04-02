## [28. Lo-Tech Cipher](http://ksnctf.sweetduet.info/problem/28)

とりあえずzipを展開すると、二つの画像が現れる。

こういう画像は初手でXORをとってみるのがよくあるらしい。
ImageMagickでできる。

```console
$ convert share1.png share2.png -fx "(((255 * u) & (255 * (1 - v))) | ((255 * (1 - u)) & (255 * v))) / 255" xor_shares.png
```

するとメッセージ "The last share is hidden in the ZIP" が現れる。
もうひとひねり要るようだ。

その後試行錯誤して、`secret.zip` がPNG画像としても有効なものであることがわかった。

```console
$ file secret.zip
secret.zip: PNG image data, 640 x 480, 8-bit/color RGBA, non-interlaced
```

そこで先ほどXORをとった画像と `secret.zip` のXORを再度とってみるとflagを得る。

```console
$ convert xor_shares.png secret.zip -fx "(((255 * u) & (255 * (1 - v))) | ((255 * (1 - u)) & (255 * v))) / 255" xor_all.png
```
