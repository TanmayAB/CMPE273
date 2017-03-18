from flask import Flask
#!/usr/bin/env python3
import base64
import requests
import sys, getopt

app= Flask(__name__)

globalurl = ""
def main(argv):
	if (len(argv) == 0):
		print('No URL Passed in argument, Please pass github URL')
	else:
		temp = argv[0]
		if (temp[0:19]=='https://github.com/' or temp[0:23] == 'https://www.github.com/'):
			splited_url  = temp.split(".com/",1)[1]
			url = 'https://api.github.com/repos/'
			url = url + splited_url
			url = url + '/contents/'
			global globalurl 
			globalurl = url
			req = requests.get(globalurl)
			if req.status_code == requests.codes.ok:
				print "Github Repo found"  # the response is a JSON
				# req is now a dict with keys: name, encoding, url, size ...
				# and content. But it is encoded with base64.
			else:
				print('Please make sure that your Github repo path is correct')
		else:
			print('Invalid URL, Check your URL') 
		app.run(debug=True,host='0.0.0.0')

@app.route("/")
def hello():
	return "Hello from Dockerized Flask App!!"

@app.route("/v1/<filename>")
def display(filename):
	url = globalurl + filename;
	req = requests.get(url)
	if req.status_code == requests.codes.ok:
		req = req.json()
		content = base64.decodestring(req['content'])
		return content
	else:
		return "Make sure that file name exists on Github. There might be an issue with File name."


if __name__ == "__main__":
	main(sys.argv[1:])
	

	
