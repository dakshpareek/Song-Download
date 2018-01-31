#!C:\Python27\python.exe 
print "Content-type:text/html\r\n\r\n"
print '''<html>
<head></head>
<body>
'''

import requests
import ssl
from bs4 import BeautifulSoup
from PIL import Image
import urllib, cStringIO
import cgi
import urlparse,os
from make_soup import make__soup
from pickle import load

f=open("mysongdata.txt","r")
data=load(f)


#finding id of movie
sid=os.environ['PATH_TRANSLATED']
id=sid.split('\\')
id=int(id[-1])
#print data[id][1]
main_link="https://songspk.name"+data[id]
#All images of movies 
#make_soup fxn required,soup2 using link required
soup2 = make__soup(main_link)
song_s = soup2.findAll("div", {"class": "col-sm-6 col-xs-12 text-center page-down-btns"})
for every_movie in song_s:
	a_tag=every_movie.findAll("a")
	for i in a_tag:
		quality=i.text
		quality=quality.encode('utf-8')
		d_link=i.attrs["href"]
		print "<a href='{}' download>{}</a>".format(d_link,quality)
		print "</br>"
print '''
</body>
</html>
'''