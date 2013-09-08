import sys
import httplib2
import HTMLParser
import urllib

def getPageContent(url):

	headers={'user-agent':'Mozilla/5.0(compatible;MSIE9.0;Windows NT 6.1;Trident/5.0)',
	'cache-control':'no-cache'}
	if url:
		response,content = httplib2.Http().request(url,headers=headers)

		if response.status == 200:
			print "Get the content from the URL"
			return content



class stack:
	def __init__(self,size=100,list=None):
		self.contain = []
		self.msize = size
		self.top = 0

	def getTop(self):
		if(self.top>0):
			return 	self.contain[self.top-1]
		else:
			return None
	def getLength(self):
		return len(self.contain)

	def push(self,data):
		if (self.top==self.msize):
			return -1

		self.contain.append(data)
		self.top = self.top+1

	def pop(self):
		try:
			res = self.contain.pop()
			if(self.top>0):
				self.top=self.top-1
			return res
		except IndexError:
			return None

class ParserOschinaNew(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.st = stack(size=1000)
		self.st.push('over')

	def handle_starttag(self,tag,attrs):
		stack_size = self.st.getLength()
		if stack_size==1 and tag=='ul':
			for name,value in attrs:
				if (name=='class' and value =='BlogList'):
					self.st.push('ul')
					break

		if stack_size == 2 and tag == 'li':
			self.st.push('li')

		if stack_size ==3 and tag=='h3':
			self.st.push('h3')
			text = 'Title of Blog:'
			print '%s' %text

		if stack_size == 3 and tag=='p':
			self.st.push('p')
			text='Context:'
			print '%s' %text

		if stack_size == 3 and tag=='div':
			for name ,value in attrs:
				if name=='class' and value =='data':
					self.st.push('div')
					text = 'author:'
					print '%s' %text


	def handle_data(self,data):
		stack_size=self.st.getLength()
		#if stack_size == 3:
			#if self.st.getTop()=='h3':
		#	print 'Title test',data
		if stack_size==4:
			print data#.decode('utf-8').encode('gb2312','ignore')

	def handle_endtag(self,tag):
		stack_size = self.st.getLength() 
		stack_tag = self.st.getTop() 
		if ('h3'==tag and 'h3'==stack_tag): 
			print self.st.getTop()
			self.st.pop() 
		if ('p'==tag and 'p'==stack_tag): 
			print self.st.getTop()
			self.st.pop() 
		if ('div'==tag and 'div'==stack_tag): 
			print self.st.getTop()
			self.st.pop() 
		if ('li'==tag and 'li'==stack_tag): 
			print self.st.getTop()
			self.st.pop() 
		if ('ul'==tag and 'ul'==stack_tag): 
			print self.st.getTop()
			self.st.pop() 
		if('over'==self.st.getTop()):           
			pass
			#print "this is end!" 

if __name__ == '__main__': 
    pageC = getPageContent('http://www.oschina.net/blog/more?p=1') 
     
    my = ParserOschinaNew() 
    my.feed(pageC) 