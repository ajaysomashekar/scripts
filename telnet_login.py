#!/usr/bin/python2.7
import telnetlib
import time

#com = 'ps | grep -- "asterisk" | grep -v "grep" | wc -l\r'
com = "asterisk -rx'core show version'"
root_login = 'su'
tn= telnetlib.Telnet('192.168.0.24')    #Device IP Address
tn.read_until('login: ')
tn.write('admin\r\n')
tn.read_until('Password: ')
tn.write('******\r\n')
tn.read_until('$')
#time.sleep(3)
tn.write(root_login+'\r\n' )
tn.read_until('Password: ')
tn.write('******\r\n')
tn.read_until('$')
tn.write(com+'\r\n' )
tn.read_until('\n')
incorrect = tn.read_until('Unable', 2)
if incorrect == "Unable":
	print "asterisk not running"
	exit()
else:
	tn.write(com+'\r\n')
	tn.read_until('\n')
	asterisk = tn.read_until('Asterisk', 2)
tn.read_until('$', 2)
tn.write('exit\n')
tn.read_until('$')
tn.write('exit\n')
print asterisk


if asterisk == "Asterisk":
	print "execute sipp success"
else:
	print "asterisk not running failed"


