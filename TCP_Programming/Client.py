import sys
from socket import *

if len(sys.argv) != 4:
	print('Invalid command line arguments!')
	sys.exit()
try:
	serverName = sys.argv[1]
	serverPort = int(sys.argv[2])
	filename = sys.argv[3]
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
#sentence = raw_input('Input lowercase sentence:')
	sentence = 'GET /' + filename + ' HTTP/1.1'
	clientSocket.send(sentence)
	modifiedSentence = 'waiting for response...\n'
	printSentence = ""
	while modifiedSentence != "":
		modifiedSentence = clientSocket.recv(1024)
		printSentence += modifiedSentence
	clientSocket.close()
	print printSentence,
except IOError:
	print('ERRORRRR')
	clientSocket.close()