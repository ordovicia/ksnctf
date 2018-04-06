## [9. Digest is secure!](http://ksnctf.sweetduet.info/problem/9)

[Digest認証](https://ja.wikipedia.org/wiki/Digest%E8%AA%8D%E8%A8%BC) の問題である。
与えられたpcapをHTTPでフィルタして眺めると、次のような通信がおこなわれている。

サーバ (`ctfq.sweetduet.info:10080/`) からクライアントへ `401 Authorization Required`:

```
Authorization Required from Server to Client:
    Digest  realm="secret",
            nonce="bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b",
            algorithm=MD5,
            qop="auth"
```

それに対し、クライアントからサーバへ `GET /~q9/`:

```
Authorization from Client to Server:
    Digest  username="q9",
            realm="secret",
            nonce="bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b",
            uri="/~q9/",
            algorithm=MD5,
            response="c3077454ecf09ecef1d6c1201038cfaf",
            qop=auth,
            nc=00000001,
            cnonce="9691c249745d94fc"
```

これによって、以下の情報を得る。

* ユーザ名: "q9"
* realm: "secret"
* algorithm: MD5
* qop: "auth"
* nc: 00000001
* cnonce: "9691c249745d94fc"

また、クライアントが取得した `/~q9/` を覗くと、`flag.html` というファイルにflagが書かれていそうな事が分かる。

Digest認証を通過するには、クライアントは以下で計算される response を生成する必要がある。

```
A1 = ユーザ名 ":" realm ":" パスワード
A2 = HTTPのメソッド ":" コンテンツのURI
response = MD5(MD5(A1) ":" nonce ":" nc ":" cnonce ":" qop ":" MD5(A2))
```

まだ分かっていない情報はA1またはMD5(A1)である。

Pcapをさらに見ていくと、クライアントが `/~q9/htdigest` をGETしていることが分かる。
このファイルには `MD5(A1)` が書かれている。
よって認証に必要な情報は全て揃ったことになるので、あとは `/~q9/flag.html` をGETするリクエストを生成して投げればよい。

* [Python版](https://github.com/ordovicia/ksnctf/blob/master/09-Digest_is_secure/solve.py)
