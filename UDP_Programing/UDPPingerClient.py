import sys
import time
from socket import *
try:
	min_RTT = sys.maxint
	max_RTT = -sys.maxint - 1
	failure = 0
	total_RTT = 0
	for pings in range(10):
		clientSocket = socket(AF_INET, SOCK_DGRAM)
		clientSocket.settimeout(1)
		message = "Ping " + str(pings+1) +" " + time.asctime()
		address = ("127.0.0.1", 12000)
		sendTime = time.time()
		clientSocket.sendto(message, address)
		try:
			modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
			recvTime = time.time()
			elapsedtime = recvTime-sendTime
			total_RTT += elapsedtime
			print '%s %d, RTT is %f seconds' % (modifiedMessage, pings, elapsedtime)
			if elapsedtime > max_RTT:
				max_RTT = elapsedtime
			if elapsedtime < min_RTT:
				min_RTT = elapsedtime
		except timeout:
			failure += 1
			print "Request timed out"
	print 'maximum RTT is %f, minimum RTT is %f, average RTT is %f' % (max_RTT, min_RTT, total_RTT/10)
	print 'packet loss rate is %d percent' % (failure * 10)
except IOError:
	print('ERRORRRR')
	clientSocket.close()
