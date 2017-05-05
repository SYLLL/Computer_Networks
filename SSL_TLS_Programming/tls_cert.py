import sys
import ssl
import socket
import time
import pprint

length = len(sys.argv)
try:
	serverName = sys.argv[length-3]
	serverPort = int(sys.argv[length-2])
	filename = sys.argv[length-1]

	#Instantiating an SSL/TLS context
	context = ssl.create_default_context()
	certpath = "cert.pem"
	#Setting TLS/SSL client options
	pos = 0
	version = ssl.PROTOCOL_SSLv23
	for flag in sys.argv:
		if flag == "--tlsv1.0":
			version = ssl.PROTOCOL_TLSv1
		elif flag == "--tlsv1.1":
			version = ssl.PROTOCOL_TLSv1_1
		elif flag == "--tlsv1.2":
			version = ssl.PROTOCOL_TLSv1_2
		elif flag == "--sslv3":
			version = ssl.PROTOCOL_SSLv3
		elif flag == "--ciphers":
			context.set_ciphers(sys.argv[pos+1])
		elif flag == "--cacert":
			certpath = sys.argv[pos+1]
		pos += 1
	#Instantiating a TCP socket
	s_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Wrapping the TCP socket with the SSL/TLS context
	s = ssl.wrap_socket(s_, ca_certs=certpath, cert_reqs=ssl.CERT_REQUIRED, ssl_version=version)
	#s = ssl.wrap_socket(s_, keyfile=None, certfile=None, server_side=False, cert_reqs=CERT_NONE, ssl_version={see docs}, ca_certs=None, do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)
	#Initiating connection
	# 
	# 
	s.connect((serverName,serverPort))
	ssl.match_hostname(s.getpeercert(), serverName)
	print repr(s.getpeername())
	print s.cipher()
	print pprint.pformat(s.getpeercert())
	sentence = 'GET /' + filename + ' HTTP/1.1'
	s.send(sentence)
	modifiedSentence = 'waiting for response...\n'
	printSentence = ""
	while True:
		modifiedSentence = s.recv(1024)
		if modifiedSentence == 'end':
			break
		printSentence += modifiedSentence
	#close socket
	s.close()
	#print printSentence
except IOError:
	print('ERRORRRR')