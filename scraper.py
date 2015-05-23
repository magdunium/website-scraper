__author__ = 'Magdum'
#coding: utf-8

import urllib2
from bs4 import BeautifulSoup
import re

userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': userAgent}


def openMainSite(html):
    request = urllib2.Request(html, None, headers)
    response = urllib2.urlopen(request)
    return response

def fetchedSite(response):
    html = response.read()
    soup = BeautifulSoup(html)
    return soup

def getTitle(soup):
    title = soup('title')
    print title

def getDescription(soup):
    description = soup.findAll(attrs={"name":"description"})
    print description


if __name__ == "__main__":
    print "Enter page URL (with http://): "
    page = raw_input()
    soup = fetchedSite(openMainSite(page))
    getTitle(soup)
    getDescription(soup)