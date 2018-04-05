## [18. USB flash drive](http://ksnctf.sweetduet.info/problem/18)

ZIPファイルが与えられるので、とりあえず `unzip` してみると、IMGファイルに展開される。
これをマウントして中身を確認すると、画像ファイルが3つあるが、これらに怪しいところは見つからない。

タイトルが "USB flash drive" なので、IMGファイル自体に鍵があるのだろう。
そこで Sleuth Kit を使うと、『民衆を導く自由の女神』の画像が隠されていた。

```console
$ fls drive.img
r/r 4-128-4:    $AttrDef
r/r 8-128-2:    $BadClus
r/r 8-128-1:    $BadClus:$Bad
r/r 6-128-4:    $Bitmap
r/r 7-128-1:    $Boot
d/d 11-144-4:   $Extend
r/r 2-128-1:    $LogFile
r/r 0-128-1:    $MFT
r/r 1-128-1:    $MFTMirr
r/r 9-128-8:    $Secure:$SDS
r/r 9-144-11:   $Secure:$SDH
r/r 9-144-5:    $Secure:$SII
r/r 10-128-1:   $UpCase
r/r 3-128-3:    $Volume
r/r 35-128-1:   Carl Larsson Brita as Iduna.jpg
r/r 37-128-1:   Mona Lisa.jpg
r/r 38-128-1:   The Great Wave off Kanagawa.jpg
-/r * 36-128-1: Liberty Leading the People.jpg
-/r * 36-128-4: Liberty Leading the People.jpg:00
-/r * 36-128-5: Liberty Leading the People.jpg:01
-/r * 36-128-6: Liberty Leading the People.jpg:02
-/r * 36-128-7: Liberty Leading the People.jpg:03
-/r * 36-128-8: Liberty Leading the People.jpg:04
-/r * 36-128-9: Liberty Leading the People.jpg:05
-/r * 36-128-10:        Liberty Leading the People.jpg:06
V/V 256:        $OrphanFiles
```

このファイルを取り出してみる。

```console
$ icat drive.img 36 > LLtP.jpg
```

画像をひらくと "The flag is in this file, but not in this image" と書かれている。
もうひとひねり要るが、flagに近づいているようだ。

先ほどの `fls` の結果を見ると、ファイルがいくつかに分かれている（？）。
それぞれ抜き出してみる。

```console
$ icat drive.img 36-128-1 > LLtP_00.jpg
$ ...
$ icat drive.img 36-128-10 > LLtP_06.jpg
```

これらのファイルを確認してみると、JPEGではなくASCIIであることが分かり、
さらに中身はflagを分割したものになっているので、連結してflagを得る。

```console
$ file LLtP_*.jpg
LLtP_00.jpg: ASCII text, with no line terminators
LLtP_01.jpg: ASCII text, with no line terminators
LLtP_02.jpg: ASCII text, with no line terminators
LLtP_03.jpg: ASCII text, with no line terminators
LLtP_04.jpg: ASCII text, with no line terminators
LLtP_05.jpg: ASCII text, with no line terminators
LLtP_06.jpg: ASCII text, with no line terminators

$ cat LLtP_00.jpg; echo
FLA
```
