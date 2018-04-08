import random
import struct


def read_i32(f):
    b = f.read(4)
    assert(b)
    return int.from_bytes(b, 'little')


def write_i32(f, i32):
    b = i32.to_bytes(4, 'little')
    f.write(b)


def backcalc_keys(plain, crypto):
    plain = open(plain, 'rb')
    crypto = open(crypto, 'rb')

    len_ = read_i32(crypto)
    assert(len_ % 4 == 0)
    len_ //= 4

    keys = []

    for i in range(len_):
        p = read_i32(plain)
        c = read_i32(crypto)
        k = p ^ c
        keys.append(k)

    crypto.close()
    plain.close()

    return keys


def untemper(x):
    def unbitshift_right_xor(x, shift):
        i = 1
        y = x
        while i * shift < 32:
            z = y >> shift
            y = x ^ z
            i += 1
        return y

    def unbitshift_left_xor(x, shift, mask):
        i = 1
        y = x
        while i * shift < 32:
            z = y << shift
            y = x ^ (z & mask)
            i += 1
        return y

    x = unbitshift_right_xor(x, 18)
    x = unbitshift_left_xor(x, 15, 0xefc60000)
    x = unbitshift_left_xor(x, 7, 0x9d2c5680)
    return unbitshift_right_xor(x, 11)


def decrypto(plain, crypto, mt_state):
    plain = open(plain, 'wb')
    crypto = open(crypto, 'rb')

    len_ = read_i32(crypto)
    assert(len_ % 4 == 0)
    len_ //= 4

    random.setstate((3, mt_state, None))

    for _ in range(len_):
        c = read_i32(crypto)
        k = random.getrandbits(32)
        p = c ^ k
        write_i32(plain, p)

    crypto.close()
    plain.close()


def main():
    MT_PREDICT_LEN = 624

    keys = backcalc_keys('encrypt.cpp', 'encrypt.enc')
    assert(len(keys) >= MT_PREDICT_LEN)

    # mt_state = tuple([untemper(k)
    #                   for k in keys[:MT_PREDICT_LEN]] + [MT_PREDICT_LEN])
    # random.setstate((3, mt_state, None))
    # predicted = [random.getrandbits(32)
    #              for _ in range(len(keys) - MT_PREDICT_LEN)]
    # assert(predicted == keys[MT_PREDICT_LEN:])

    mt_state = tuple([untemper(k)
                      for k in keys[-MT_PREDICT_LEN:]] + [MT_PREDICT_LEN])
    decrypto('flag.jpg', 'flag.enc', mt_state)


if __name__ == '__main__':
    main()
