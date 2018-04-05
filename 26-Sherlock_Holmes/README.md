## [26. Sherlock Holmes](http://ksnctf.sweetduet.info/problem/26)

Sherlock Holmes "A Scandal in Bohemia" が載っている。
この文章自体にはおかしなところはない。

まず気づくことは、ページ名が `index.pl` とPerlスクリプトになっていること。
従ってPerl CGIだろうと予測される。

"A Scandal in Bohemia" の文章を表示するURLが
`http://ctfq.sweetduet.info:10080/~q26/index.pl/a_scandal_in_bohemia_1.txt`
などであるから、`a_scandal_in_bohemia_1.txt` の部分にほかのファイル名をいれるとそれが表示されるかもしれないと考える。

そこで `http://ctfq.sweetduet.info:10080/~q26/index.pl/index.pl` にアクセスすると、裏で動いているPerlスクリプトが表示され、どの部分を攻撃すればよいか分かる。
（ちなみに `flag.txt` というファイルもあるが、flag自体は書かれていない。）

```perl
# Can you crack me? :P
open(F,'cracked.txt');
my $t = <F>;
chomp($t);
if ($t eq 'h@ck3d!') {
    print 'FLAG_****************<br><br>';
}
unlink('cracked.txt');
```

`cracked.txt` から一行読んで `h@ck3d!` と同じならflagを表示するようになっているので、`cracked.txt` に書き込みできればよい。

"perl cgi vulnerabilities" などでググると、これに関連する脆弱性が [ヒットする](http://www.cgisecurity.com/lib/sips.html) 。
シェルコマンドの任意実行が出来るようだ。
`http://ctfq.sweetduet.info:10080/~q26/index.pl/|echo h@ck3d! >& cracked.txt` にアクセスしてみるとflagを得る。
