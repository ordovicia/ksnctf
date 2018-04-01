static CODE: &str = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.";

const ALPHABET_NUM: u8 = 26;

fn main() {
    for rot in 1..ALPHABET_NUM {
        println!(
            "rot: {}\n{}\n",
            rot,
            CODE.bytes()
                .map(|c| rotate(rot, c) as char)
                .collect::<String>()
        );
    }
}

fn rotate(rot: u8, c: u8) -> u8 {
    match c {
        b'A'...b'Z' => (c - b'A' + rot) % ALPHABET_NUM + b'A',
        b'a'...b'z' => (c - b'a' + rot) % ALPHABET_NUM + b'a',
        _ => c,
    }
}
