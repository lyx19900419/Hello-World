import HTMLParser
import sys
import os
import string
import urllib
import re
import time
import MySQLdb
import socket
import thread

socket.setdefaulttimeout(3)
tags = []
ftptags = []
i = 0
j = 0
k = 0
myConnect = MySQLdb.connect(host='localhost',user='root',passwd='123',db='python')
cursor=myConnect.cursor()

class Parser(HTMLParser.HTMLParser):
	global tags
	def handle_starttag(self,tag,attrs):
		if tag == 'a':
			for i in range(0,len(attrs)):	
				if attrs[i][0]=='href' and attrs[i][1].startswith('http://'):
					if attrs[i][1] not in tags:
						tags.append(attrs[i][1])

class ftpParser(HTMLParser.HTMLParser):
	def handle_starttag(self,tag,attrs):
		if tag == 'img':
			for i in range(0,len(attrs)):
				if attrs[i][0]=='src'  and attrs[i][1].startswith('http://'):
					if attrs[i][1] not in ftptags:
						print attrs[i][1]
						ftptags.append(attrs[i][1])
def Run(no,testa):	
	global i
	while i < len(tags):
		i = i+1
		try:	
			print tags[i]
			print ftptags[i]
			Parser().feed(urllib.urlopen(tags[i]).read())
			ftpParser().feed(urllib.urlopen(tags[i]).read())
	 	except:
			pass
				

#def Do_insert(no,test):
#	global myConnect
#	global cursor
#	j = 0
#	while j < len(tags):
#		try:
#			cursor.execute('insert into URL values'+'("'+tags[i]+'")')
#			myConnect.commit()
#			j = j+1
#		except:
#			pass



html = urllib.urlopen('http://www.sina.com').read()
try:
	Parser().feed(html)
	ftpParser().feed(html)
except:
	pass
thread.start_new_thread(Run,(1,2))
thread.start_new_thread(Run,(1,2))
thread.start_new_thread(Run,(1,2))
thread.start_new_thread(Run,(1,2))
thread.start_new_thread(Run,(1,2))

time.sleep(100000)
myConnect.close()
