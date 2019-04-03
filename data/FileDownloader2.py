# First ensure that you have following libraries installed:
# BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
# html2text: https://github.com/Alir3z4/html2text/blob/master/docs/usage.md
# Commands for EMR:
# sudo easy_install bs4 (or sudo pip install bs4)
# sudo easy_install html2text


# Python 3 commands

from bs4 import BeautifulSoup
import ntpath
import urllib.request 
import html2text
baseurl = "http://lite.cnn.io" 
soup = BeautifulSoup(urllib.request.urlopen(baseurl), "html5lib")
links=soup.findAll("a")
for link in links[5:]:
	print (link.text)
	if (link.get('href').startswith("/") and "CNN" not in link.text):
		with urllib.request.urlopen(baseurl+link.get('href')) as f:
			fout = open(ntpath.basename(link.get('href'))+".txt", "w")
			fout.write(html2text.html2text(f.read().decode('utf-8')))
			fout.close()
			
'''
# Python 2 commands

from bs4 import BeautifulSoup
import ntpath
import urllib2
import html2text
import codecs
baseurl = "http://lite.cnn.io" 
soup = BeautifulSoup(urllib2.urlopen(baseurl), "lxml")
links=soup.findAll("a")
for link in links[5:]:
	print (link.text)
	if (link.get('href').startswith("/") and "CNN" not in link.text):
		f = urllib2.urlopen(baseurl+link.get('href'))
		fout = codecs.open(ntpath.basename(link.get('href'))+".txt", "w", "utf-8")
		# str = unicode(f.read(), 'utf-8')
		str = f.read()
		h = html2text.HTML2Text()
		outstr = h.handle(str.decode('utf-8'))
		fout.write(outstr)
		fout.close()
		f.close()
'''
