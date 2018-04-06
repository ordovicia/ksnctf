from urllib import request

URL = 'http://ctfq.sweetduet.info:10080/~q9/flag.html'
URI = '/~q9/flag.html'

# A1 = username:realm:password
# A2 = "HTTP method":"Content URI"
# response = MD5(MD5(A1):nonce:nc:cnonce:qop:MD5(A2))

# /~q9/htdigest = A1:
#     q9:secret:c627e19450db746b739f41b64097d449
MD5_A1 = 'c627e19450db746b739f41b64097d449'

A2 = 'GET:' + URI


# Authorization Required from Server to Client:
#     Digest  realm="secret",
#             nonce="bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b",
#             algorithm=MD5,
#             qop="auth"
REALM = 'secret'
ALGORITHM = 'MD5'
QOP = 'auth'

# Authorization from Client to Server:
#     Digest  username="q9",
#             realm="secret",
#             nonce="bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b",
#             uri="/~q9/",
#             algorithm=MD5,
#             response="c3077454ecf09ecef1d6c1201038cfaf",
#             qop=auth,
#             nc=00000001,
#             cnonce="9691c249745d94fc"
USER_NAME = 'q9'
NC = '00000001'
CNONCE = '9691c249745d94fc'


def md5(data):
    import hashlib
    if type(data) == str:
        data = bytes(data, 'utf-8')
    return hashlib.md5(data).hexdigest()


def get_nonce():
    from urllib import error

    try:
        response = request.urlopen(URL)
    except error.HTTPError as e:
        nonce = e.info()['WWW-Authenticate'].split('"')[3]
        return nonce

    assert(False)


def gen_response(nonce):
    md5_A2 = md5(A2)
    response = '{}:{}:{}:{}:{}:{}'.format(
        MD5_A1, nonce, NC, CNONCE, QOP, md5_A2)
    return md5(response)


def gen_auth(nonce, response):
    auth = '''\
Digest username="{}", \
realm="{}", \
nonce="{}", \
uri="{}", \
algorithm={}, \
response="{}", \
qop={}, \
nc={}, \
cnonce="{}"\
'''.format(USER_NAME, REALM, nonce, URI, ALGORITHM, response, QOP, NC, CNONCE)
    return auth


def main():
    nonce = get_nonce()
    response = gen_response(nonce)
    auth = gen_auth(nonce, response)

    req = request.Request(URL)
    req.add_header('Authorization', auth)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
