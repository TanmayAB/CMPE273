import psutil
from collections import OrderedDict

# def findChar(command_output, required, n):
#     parts= command_output.split(required, n+1)
#     if len(parts)<=n+1:
#         return -1
#     return len(command_output)-len(parts[-1])-len(required)


conns= psutil.net_connections('tcp');
#print conns;
myDict = dict();
mytuple = ();
same_pid = None;
i = 0;
j = 0;
k=0;
# for value in conns:
# 	print value;
for conn in conns:
	laddr_flag = 0;
	raddr_flag = 0;
	laddr = '';
	raddr = '';
	pid=getattr(conn,'pid');
	if pid==None:
		pid=0;
		# print "PID IS ZERO"
	laddr_tuple=getattr(conn,'laddr');
	raddr_tuple=getattr(conn,'raddr');
	status=getattr(conn,'status');
	
	i=i+1;
	if laddr_tuple:
		laddr_flag = 1;
		laddr= laddr_tuple[0] + '@' + str(laddr_tuple[1]);
	if raddr_tuple:
		raddr_flag = 1;
		raddr= raddr_tuple[0] + '@' + str(raddr_tuple[1]);
	if laddr_flag == 1 and raddr_flag ==1:
		if pid in myDict.keys():
			# print "repeating" + str(pid);
			temp_tuple = myDict.get(pid);
			temp_tuple = (pid,laddr,raddr,status);
			myDict[pid] = myDict[pid] + temp_tuple;
			# print "Yeah \n";
		else:
			# print "Not repeating"
			myDict[pid]=(pid,laddr,raddr,status);
	# else:
		# print "Nah \n";

sorted_myDict = OrderedDict(sorted(myDict.viewitems(), key=lambda x: len(x[1]), reverse=True))

print ("\"Pid\", \"Laddr\", \"raddr\", \"Status\"");

for key, value in sorted_myDict.items():
	for i in range(0,len(value)-1,4):
		print "\"%s\",\"%s\",\"%s\",\"%s\"" % (value[i],value[i+1],value[i+2],value[i+3]);
		# print " %d , %d , %d , %d " % (i,i+1,i+2,i+3);
		# print "now : %d " % i;
   # for value in mylist:
# 	if(value[0] = same_pid):
# 		print ("\"%d\", \"%s\", \"%s\", \"%s\"" % (value[0],value[1],value[2],value[3]));

# print "Mylist length : " + str(len(mylist));
# print "For loop length : " + str(i);
# print "How many times both were true : " + str(k);
# print "Value not present length : " + str(j);

	# laddr_start= findChar(conn_str,'(',1);
	# laddr_end= findChar(conn_str,')',0);
	# if laddr_end-laddr_start==1:
	# 	laddr = '';
	# else:
	# 	laddr_start= findChar(conn_str,'(',1);
	# 	laddr_end= findChar(conn_str,'\'',1);
	# 	laddr_start= laddr_start + 2;
	# 	laddr_end= laddr_end;
	# 	laddr = conn_str[laddr_start:laddr_end];

	# raddr_start= findChar(conn_str,'(',2);
	# raddr_end= findChar(conn_str,')',1);
	# if (raddr_end-raddr_start)== 1:
	# 	raddr = '';
	# else:
	# 	if laddr_end-laddr_start > 1:
	# 		raddr_end= findChar(conn_str,'\'',3);
	# 	else:
	# 		raddr_end= findChar(conn_str,'\'',1);
	# 	raddr_start= raddr_start + 2;
	# 	raddr_end= raddr_end;
	# 	raddr= conn_str[raddr_start:raddr_end];

	# pid_start= findChar(conn_str,'pid',0);
	# pid_end= findChar(conn_str,')',2);
	# pid_start= pid_start + 4;
	# pid_end= pid_end;
	# pid= conn_str[pid_start:pid_end];
	
	# status_start= findChar(conn_str,'status',0);
	# status_end= findChar(conn_str,'pid',0);
	# status_start= status_start + 8;
	# status_end= status_end - 3;
	# status= conn_str[status_start:status_end];
	# print "raddr : " + raddr;	
	# print "laddr : " + laddr;
	# print "pid : " + pid;
	# print "status : " + status;
# 11343