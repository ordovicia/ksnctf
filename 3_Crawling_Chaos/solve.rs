const P: [usize; 21] = [
    70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196,
    1520, 1480, 1449,
];

fn main() {
    let flag: String = P.iter()
        .enumerate()
        .map(|(i, p)| (p / (i + 1)) as u8 as char)
        .collect();
    println!("{}", flag);
}
