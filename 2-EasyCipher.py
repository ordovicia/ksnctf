code = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."

alph_num = 26
A = 65
Z = A + alph_num
a = 97
z = a + alph_num

rot = -13
print("rot =", rot)

for c in code:
    o = ord(c)
    if A <= o <= Z:
        o = (o - A + rot) % alph_num + A
    elif a <= o <= z:
        o = (o - a + rot) % alph_num + a
    c = chr(o)
    print(c, end="")
print()
