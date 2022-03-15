import socket

s = socket.socket()

#on crée une adresse ici c'est un site avec son port
address = ('www.perdu.com', 80)

#on se connect ensuite au site
s.connect(address) 

#on encode une requête (ici c'est )
#encode utilise UTF-8
#en HTTP 1.1 on doit aussi précisser le host (on ne doit pas le faire en 1.0)
request = 'GET / HTTP/1.1\r\nHost: www.perdu.com\r\n\r\n'.encode()

# on peut envoyer des requêtes sur le site
s.send(request)

#on va recevoir la réponse du site avec 'recv(nbre d'octect)'.decode() pour transformer les bits
#ici on reçoit max 2048 bits
response = s.recv(2048).decode()

print(response)

#pour finir il faut fermer le socket
s.close()

##permet de fermer automatiquement le socket
#address = ('www.perdu.com', 80)
#request = 'GET / HTTP/1.0\r\n\r\n'.encode()
#with socket.socket() as s:
#    s.connect(address)
#    s.send(request)
#    response = s.recv(2048).decode()
#print(response)