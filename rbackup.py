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
	from terminal import render
	
	if len(sys.argv) > 1 and sys.argv[1] == "-h":
			print render('%(BOLD)sNAME')
			print render ('%(NORMAL)s	rbackup - 	creates a incremental backup using rsync to a mounted device')
			print " "
			print render ('%(BOLD)sSYNOPSIS')
			print render ('%(NORMAL)s	rbackup [source directory or file] [destination directory or file]')
			print "" 
			print render ('%(BOLD)sEXAMPLE')
			print render ('%(NORMAL)s	rbackup /tmp/rbackup /tmp2/rbackup')
			return

	if (len(sys.argv) > 2 and len(sys.argv) < 4):		
		source = sys.argv[1]
		dest = sys.argv[2]
		print rbackup (source,dest)
	else:
		print "Usage: rbackup [Source] [Destination] or -h for help"
		

check_back ()


