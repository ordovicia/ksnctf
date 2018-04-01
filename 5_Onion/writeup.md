## [5. Onion](http://ksnctf.sweetduet.info/problem/5)

印字可能な英数字のみで成り立っているので、Base64でデコードしてみる。
するとまた似たような文字列が現れるので、またBase64でデコードしてみる。
これを何回か繰り返すことができ、デコードのたびに文字列が短くなっていくことが分かる。
ここまで来ると、タイトル "Onion" の意味が分かる。

最終的に16回デコードすると、

```
begin 666 <data>
51DQ!1U]&94QG4#-3:4%797I74$AU

end
```

という文字列が得られる。
これはBase64でエンコードされたものではない。

`begin 666` などでググってみると [uuencode](https://ja.wikipedia.org/wiki/Uuencode) というフォーマットがあることが分かる。
これをデコーダ `uudecode` でデコードすると、flagを得る。

ちなみに、Arch Linuxなら、`uudecode` は `sharutils` パッケージに入っている。
