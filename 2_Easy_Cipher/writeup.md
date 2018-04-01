## 2. [Easy Cipher](http://ksnctf.sweetduet.info/problem/2)

```
EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.
```

見るからにシーザー暗号。
シフトする量を変えながら復号を試してみる。

* [Rust版](https://github.com/ordovicia/ksnctf/blob/master/2_Easy_Cipher/solve.rs)
* [Python版](https://github.com/ordovicia/ksnctf/blob/master/2_Easy_Cipher/solve.py)

するとシフト量13で次の文章が得られ、flagがわかる。

```
ROT XIII is a simple letter substitution cipher that replaces a letter with the letter XIII letters after it in the alphabet. ROT XIII is an example of the Caesar cipher, developed in ancient Rome. Flag is FLAGSwzgxBJSAMqwxxAU. Insert an underscore immediately after FLAG.
```
