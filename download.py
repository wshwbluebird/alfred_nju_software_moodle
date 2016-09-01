#!/usr/local/cellar/python/2.7.12/bin/python2.7
# encoding: utf-8

import sys
import urllib2
import cookielib


reload(sys)
sys.setdefaultencoding('utf-8')

def get_recent_posts(url_new):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    url_old = 'http://218.94.159.99/login/index.php'
    data ="username=151250145%40smail.nju.edu.cn&password=########&rememberusername=1&anchor="
    response1 = opener.open(fullurl=url_old,data=data)
    del response1
    response2 =opener.open(url_new)
    source = response2.read()

    with open("/Users/wshwbluebird/Desktop/f1",'wb') as file:
        file.write(source)








def main():

    url = sys.argv[1]
    get_recent_posts(url)


if __name__ == "__main__":
    main()