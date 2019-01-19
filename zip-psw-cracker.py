# modules
import zipfile
import optparse
from threading import Thread

zFile = zipfile.ZipFile("test.zip")

def extractFile(zFile, pwd):
	# try the password
	try:
		zFile.extractall(pwd=bytes(pwd, encoding='utf-8'))
		print('\n[+] Success! The password of the archive is: ', pwd+'\n')
		exit(0)
	except Exception as e:
		pass

def main():
	# specify usage and params
	parser = optparse.OptionParser('[Usage] '+'-f <zipfile> -d <dictionary>')
	parser.add_option('-f', dest='zname', type='string', help="Specify zip file")
	parser.add_option('-d', dest='dname', type='string', help="Specify dictionary file")
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print(parser.usage)
		exit(0)
	else:
		zname = options.zname
		dname = options.dname
	# open dictionary and file to unlock
	try: 
		dictionary = open(dname)
		zFile = zipfile.ZipFile(zname)
	except Exception as e:
		print('[+] Error! ',e)
		exit(0)
	# loop the dictionary
	for word in dictionary.readlines():
		pwd = word.strip('\n')
		print('[+] Trying "'+pwd+'" ...')
		t = Thread(target=extractFile, args=(zFile, pwd))
		t.start()
if __name__ == '__main__':
	main()
		