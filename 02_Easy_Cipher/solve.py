CODE = 'EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.'

ALPHABET_NUM = 26
A = 65
Z = A + ALPHABET_NUM
a = 97
z = a + ALPHABET_NUM


def rotate(rot, c):
    o = ord(c)
    if A <= o <= Z:
        o = (o - A + rot) % ALPHABET_NUM + A
    elif a <= o <= z:
        o = (o - a + rot) % ALPHABET_NUM + a
    return chr(o)


def main():
    for rot in range(1, ALPHABET_NUM):
        print("rot: ", rot)
        for c in [rotate(rot, c) for c in CODE]:
            print(c, end="")
        print("\n")


if __name__ == '__main__':
    main()
