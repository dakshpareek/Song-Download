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
from pickle import dump
import json
import time
from make_soup import make__soup

start_time = time.time()

def make__soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html,"lxml")

url = "https://songspk.name/browse/bollywood-singles"

soup = make__soup(url)
songs = soup.findAll("figure", {"class": "col-md-3 col-sm-3 col-xs-6 thumb-inline"})
all_data=[]
i=0
#all movies links are stored here
for every_movie in songs:
	a_tag=every_movie.findAll("a")
	title=a_tag[1].text
	singer=a_tag[2].text
	link=a_tag[0].attrs["href"]
	all_data.append(link)
	print "<a href='songdownload.py/{}'>{}</a>".format(i,title)
#	print singer
	print "</br>"
	print "<hr>"
	i=i+1

f1=open('mysongdata.txt','w')
dump(all_data,f1)
f1.close()	


'''
k=[]

for i in range(len(all_data)):
	soup2=make__soup(all_data[i][1])
	d_link=soup2.findAll("a",{"class": "buttn blue"})
	f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
	soup3=make__soup(f_link)
	last_link=soup3.findAll("a")
	final=last_link[len(last_link)-2].attrs["href"]
	k.append(final)
'''	
	



print "--- %s seconds ---" % (time.time() - start_time)
print '''
</body>
</html>
'''


	#print "Click to download: ",final
