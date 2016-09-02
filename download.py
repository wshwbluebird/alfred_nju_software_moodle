#!/usr/local/cellar/python/2.7.12/bin/python2.7
# encoding: utf-8

import sys
import urllib2
import cookielib


reload(sys)
sys.setdefaultencoding('utf-8')
import alfred

def get_recent_posts(url_new,name):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    url_old = 'http://218.94.159.99/login/index.php'
    data ="username=151250145%40smail.nju.edu.cn&password=########&rememberusername=1&anchor="
    response1 = opener.open(fullurl=url_old,data=data)
    del response1
    response2 =opener.open(url_new)
    source = response2.read()

    with open("/Users/wshwbluebird/Desktop/"+name,'wb') as file:
        file.write(source)
    feedback = alfred.Feedback()
    feedback.addItem(
        title='open'+name,
        subtitle='press enter to enter this class',
        arg='/Users/wshwbluebird/Desktop/'+name,
        autocomplete='/Users/wshwbluebird/Desktop/'+name,
        icontype='filicon',
        icon="finish.png"
    )
    feedback.output()









def main():

    url = sys.argv[1]
    name = sys.argv[2]
    get_recent_posts(url,name)



if __name__ == "__main__":
    main()