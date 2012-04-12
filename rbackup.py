#!/usr/local/bin/python
import sys
import os.path

def rbackup (source,dest): 

	print "Source Directory " , source
	print "Destination Directory " , dest

	#verify is source and dest found
		
	if not os.path.exists(source) : 
		print "Source not found.. Exiting..." 
		return 

	if not os.path.exists(dest) :
		print "Destination not found .. Exiting...." 
		return
	
	#Source and Dest found we can do the backup
	from subprocess import call
	call("echo rsync -avhe --progress " + source +" " + dest, shell=True)
	call("rsync -avhe --progress --delete " + source +" " + dest, shell=True)
	
	return "listo" 


def check_back ():

	if (len(sys.argv) > 2 and len(sys.argv) < 4):	
		source = sys.argv[1]
		dest = sys.argv[2]
		print rbackup (source,dest)
				
	else:
		print "Usage rbackup Source Destination"
		print "example: rbackup /home/rbenzaquen /Vol/rbenzaquen"
		print " This will Backup your home directory to an external drive"
		

check_back ()


