import psutil

# def findChar(command_output, required, n):
#     parts= command_output.split(required, n+1)
#     if len(parts)<=n+1:
#         return -1
#     return len(command_output)-len(parts[-1])-len(required)


conns= psutil.net_connections('tcp');
#print conns;

mylist = [];
i = 0;
j = 0;
k=0;

for conn in conns:
	laddr_flag = 0;
	raddr_flag = 0;
	laddr = '';
	raddr = '';
	pid=getattr(conn,'pid');
	if pid==None:
		pid=0;
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
	if laddr_flag==1 or raddr_flag ==1:
		k = k + 1;
		mylist.append([pid,laddr,raddr,status]);
	else:
		j=j+1;
mylist.sort();
print ("\"Pid\", \"Laddr\", \"raddr\", \"Status\"");
for value in mylist:
		print ("\"%d\", \"%s\", \"%s\", \"%s\"" % (value[0],value[1],value[2],value[3]));

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
