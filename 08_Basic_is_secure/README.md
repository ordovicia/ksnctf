## [8. Basic is secure?](http://ksnctf.sweetduet.info/problem/8)

Basic認証を用いた通信のキャプチャが与えられているようだ。

[WikipediaのBasic認証に関する記事](https://ja.wikipedia.org/wiki/Basic%E8%AA%8D%E8%A8%BC) を見て、ユーザ名・パスワードを送信していそうな箇所を見つける。

```
Authorization: Basic cTg6RkxBR181dXg3eksyTktTSDhmU0dB
```

この部分がそれらしい。

> Basic認証では、ユーザ名とパスワードの組みをコロン ":" でつなぎ、Base64でエンコードして送信する。

とのことなので、`cTg6RkxBR181dXg3eksyTktTSDhmU0dB` をデコードするとflagを得る。
