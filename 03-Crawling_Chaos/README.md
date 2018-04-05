## [3. Crawling chaos](http://ksnctf.sweetduet.info/problem/3)

貼られているリンク先にアクセスしてみるとフォームが一つあるだけ。
適当な文字列を送ってみると "No" が返る。

ページのソースを見ると [このようなJavaScriptコード](https://github.com/ordovicia/ksnctf/blob/master/3-Easy_Cipher/orig.js) が埋め込まれている。
[調べてみると](http://sanya.sweetduet.info/unyaencode/) 何らかのJSのコードを変換したものらしく、変換後も有効なJavaScriptとして実行できるようだ。

そこでNode.jsで実行してみる。
すると次のようにエラーで落ちるが、どのようなコードを実行しているかが分かる。

```
undefined:2
$(function(){$("form").submit(function(){var t=$('input[type="text"]').val();var p=Array(70,152,195,284,475,612,791,896,810,850,737,1332,1469,1120,1470,832,1785,2196,1520,1480,1449);var f=false;if(p.length==t.length){f=true;for(var i=0;i<p.length;i++)if(t.charCodeAt(i)*(i+1)!=p[i])f=false;if(f)alert("(」・ω・)」うー!(/・ω・)/にゃー!");}if(!f)alert("No");return false;});});
^

ReferenceError: $ is not defined
    at eval (eval at <anonymous> (/home/hyab/Repos/ordovicia/ksnctf/3-Crawling_Chaos/orig.js:1:17299), <anonymous>:2:1)
    at Object.<anonymous> (/home/hyab/Repos/ordovicia/ksnctf/3-Crawling_Chaos/orig.js:1:17333)
    at Module._compile (module.js:649:30)
    at Object.Module._extensions..js (module.js:660:10)
    at Module.load (module.js:561:32)
    at tryModuleLoad (module.js:501:12)
    at Function.Module._load (module.js:493:3)
    at Function.Module.runMain (module.js:690:10)
    at startup (bootstrap_node.js:194:16)
    at bootstrap_node.js:666:3
```

整形すると、

```javascript
$(function() {
    $("form").submit(function() {
        var t = $('input[type = "text"]').val();
        var p = Array(70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449);
        var f = false;
        if (p.length == t.length) {
            f = true;
            for (var i = 0;i < p.length; i++)
                if (t.charCodeAt(i) * (i + 1) != p[i])
                    f = false;
            if (f)
                alert("(」・ω・)」うー!(/・ω・)/にゃー!");
        }
        if (!f)
            alert("No");
        return false;
    });
});
```

となり、フォームの入力 `t` に簡単な操作を施したものが `p` と同じなら "(」・ω・)」うー!(/・ω・)/にゃー!" が表示される。
これを満たす入力を逆算してみるとflagが分かる。

* [Rust版](https://github.com/ordovicia/ksnctf/blob/master/3-Crawling_Chaos/solve.rs)
* [Python版](https://github.com/ordovicia/ksnctf/blob/master/3-Crawling_Chaos/solve.py)
