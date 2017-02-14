import subprocess
import operator



def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

hosts_names = ["US EAST - North Virginia [72.44.32.8]","US EAST - Ohio [52.14.64.0]","US WEST - North California [184.72.56.36]","US WEST - Oregon [54.202.0.1]","US WEST - GovCloud [52.222.9.163]","CANADA - Central [52.60.50.0]","EU - Ireland [176.34.127.254]","EU - Frankfurt [52.57.255.254]","EU - London [52.56.34.0]","ASIA PACIFIC - Tokyo [103.4.10.139]","ASIA PACIFIC - Seoul [52.78.63.252]","ASIA PACIFIC - Singapore [54.254.128.1]","ASIA PACIFIC - Sydney [13.54.63.252]","ASIA PACIFIC - Mumbai [35.154.63.252]","SOUTH AMERICA - Sao Paulo [54.207.127.254]"]
hosts_list =["72.44.32.8","52.14.64.0","184.72.56.36","54.202.0.1","52.222.9.163","52.60.50.0","176.34.127.254","52.57.255.254","52.56.34.0","103.4.10.139","52.78.63.252","54.254.128.1","13.54.63.252","35.154.63.252","54.207.127.254"]

i = 0
dictionary = {}
for host in hosts_list:
	ping = subprocess.Popen(
	    ["ping", "-c", "3", host],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	out, error = ping.communicate()
	#print out
	s_index = findnth(out,'/',3)
	e_index = findnth(out,'/',4)
	#print hosts_names[i]
	#print out[s_index+1:e_index]
	dictionary.update({hosts_names[i] : float(out[s_index+1:e_index])})
	i = i + 1
#print "Length is %d" % len(dictionary)

#for key,val in dictionary.items():
#	print key,"==>",val

sorted_list = sorted(dictionary.items(), key = operator.itemgetter(1))
num = 1
for item in sorted_list:
	print ("%d. %s - %s ms" % (num,item[0].ljust(42), item[1]))
	num+=1

