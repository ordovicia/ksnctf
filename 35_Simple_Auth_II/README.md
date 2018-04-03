## [35. Simple Auth II](http://ksnctf.sweetduet.info/problem/25)

PHPのソースが与えられている。
フォームの入力に従って、DBからユーザ名・パスワードを読むのは以下の部分である。

```php
if (!isset($_POST['id']) or !is_string($_POST['id']))
    $_POST['id'] = '';
if (!isset($_POST['password']) or !is_string($_POST['password']))
    $_POST['password'] = '';

$try = false;
$ok = false;

if ($_POST['id']!=='' or $_POST['password']!=='')
{
    $try = true;
    $db = new PDO('sqlite:database.db');
    $s = $db->prepare('SELECT * FROM user WHERE id=? AND password=?');
    $s->execute(array($_POST['id'], $_POST['password']));
    $ok = $s->fetch() !== false;
}
```

SQLインジェクションするのかと思ったが、よく見るとDBのファイル名が書かれている。
`http://ctfq.sweetduet.info:10080/~q35/database.db` からDB本体がダウンロードできる。
これに接続して読み出せばよい。

```console
$ sqlite3 database.db
sqlite> SELECT * FROM user;
```
