static PI_STR: &str = "31415926535897";
const DIGITS_LEN: usize = 10;

fn main() {
    let pi_str_len = PI_STR.len();

    for i in 0..(pi_str_len - DIGITS_LEN + 1) {
        let digits = &PI_STR[i..(i + DIGITS_LEN)];
        if digits.chars().nth(0).unwrap() == '0' {
            continue;
        }

        let digits = digits.parse::<i64>().unwrap();
        if is_prime(digits) {
            println!("{}", digits);
            break;
        }
    }
}

fn is_prime(x: i64) -> bool {
    let ceil = (x as f64).sqrt().ceil() as i64;
    for i in 2..ceil {
        if x % i == 0 {
            return false;
        }
    }

    true
}
