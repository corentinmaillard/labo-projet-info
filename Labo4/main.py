import socket

def Premier():
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


#SERVEUR
def SERVEUR():
    s = socket.socket()

    #comprent l'IP et le port (on met 0.0.0.0 qui correspont a n'importe quelle adresse IP)
    serverAddress = ('0.0.0.0', 3000)

    #on se connect
    s.bind(serverAddress)

    #on va ensuite écouter le réseau
    s.listen()

    #c'est une méthode bloquante (tant qu'elle n'a pas eu de réponse on ne continu pas) et elle reçoit un client et une adresse
    client, address = s.accept()

    #on peut utiliser le client pour recevoir les messages
    message = client.recv(2048).decode()

    #on peut répondre avec 'send()'

    s.close()

    #on peut faire une commucation local avec localhost ou '127.0.0.1'

    ##ici on crée une boucle infini pour tjrs recevoir les messages
    #while True:
    #    client, address = s.accept()
    #    with client:
    #        message = client.recv(2048).decode()

