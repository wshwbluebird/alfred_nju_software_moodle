#!/usr/local/cellar/python/2.7.12/bin/python2.7
# encoding: utf-8

import sys
from bs4 import BeautifulSoup
import urllib2
import cookielib
import alfred



import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_recent_posts(url_new):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    url_old = 'http://218.94.159.99/login/index.php'
    data ="username=151250145%40smail.nju.edu.cn&password=#########&rememberusername=1&anchor="
    response1 = opener.open(fullurl=url_old,data=data)
    del response1
    response2 =opener.open(url_new)
    source = response2.read()
    # print source

    soup = BeautifulSoup(source, "lxml")
    precc = soup.find(id="region-main")
    course_list = precc.find_all("a")[1:]
    # print course_list
    # print course_list
    feedback = alfred.Feedback()

    for course in course_list:
       link = course.get("href")
       name = course.get_text()[:-3]
       feedback.addItem(
           title=name,
           subtitle='press enter to enter this class',
           arg=link+" "+name,
           autocomplete=link+" "+name,
           icontype='filicon',
           icon="down.png"
       )
    feedback.output()





def main():

    url = sys.argv[1]
    get_recent_posts(url)


if __name__ == "__main__":
    main()