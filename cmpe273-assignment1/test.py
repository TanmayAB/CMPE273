#!/usr/bin/env python3
import base64
import requests
import sys, getopt

def main(argv):
    if (len(argv) == 0):
        print('No URL Passed in argument, Please pass github URL')
    else:
        temp = argv[0]
	if (temp[0:19]=='https://github.com/' or temp[0:23] == 'https://www.github.com/'):
	    splited_url  = temp.split(".com/",1)[1]
            url = 'https://api.github.com/repos/'
            url = url + splited_url
            url = url + '/contents/dev-config.yml'
	    req = requests.get(url)
	    if req.status_code == requests.codes.ok:
		req = req.json()  # the response is a JSON
        	# req is now a dict with keys: name, encoding, url, size ...
        	# and content. But it is encoded with base64.
        	content = base64.decodestring(req['content'])
        	print content
    	    else:
        	print('Please make sure that your Github repo path is correct')
	else:
	    print('Invalid URL, Check your URL') 


if __name__ == "__main__":
   main(sys.argv[1:])
