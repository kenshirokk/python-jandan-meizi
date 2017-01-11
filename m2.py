#coding:utf-8

import requests
import re
import os
import threading
from bs4 import BeautifulSoup

def writetotmpfile(content, file):
	f = open(file, "w")
	f.write(content)

def saveimg(url, dir):
	try:
		ext = url[url.rfind("."):]
		ir=requests.get(r"http://"+url[2:])
		open(dir + url[url.rfind("/")+1:url.rfind(".")] + ext, "wb").write(ir.content)
	except:
		print "xxxxxxxxxxxxxxxxx%s" % url


baseurl = "http://jandan.net/ooxx/"
page_start = 1001
page_end = 1100
basedir = "pic" + os.path.sep

dir = ""
for page in xrange(page_start, page_end+1, 1):
	#每100页创建一个文件夹,并且获得文件夹位置 dir
	if (page - 1) % 100 == 0:
		dirname = basedir + "%d-%d" % (page, page+99)
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		dir = dirname + os.path.sep

	#先取得每一页的html 然后循环下载图片
	html = requests.get(baseurl+"page-%d" % page).text
	soup = BeautifulSoup(html, "lxml")

	for a in soup.find_all("a", class_="view_img_link"):
		print u"下载第%d页, url:%s" % (page, a["href"])
		threading.Thread(target = saveimg, args = (a["href"], dir)).start()