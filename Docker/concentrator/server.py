# coding: utf-8 

import socket
import threading
import json
import mysql


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(999999)
        print("Ouverture du fichier")

        self.clientsocket.send('Fichier correctement recu'.encode('utf-8'))

        file = json.loads(r.decode('utf-8'))

        for automate in file:

            cnx = mysql.connector.connect(user='root', password='MariaDBroot2019', host='192.168.180.147',
                                          database='devops')
            print(automate)
            cursor = cnx.cursor()

            insert = ("INSERT INTO automate "
                      "(unit_number, automate_number, automate_type, temp_cuve, temp_ext, poids_lait_cuve, poids_produit, mesure_ph, mesure_k, NaCi, n_bact_salmon, n_bact_listeria)"
                      "VALUES (%(UNITNUMBER)s, %(NUMBER)s, %(TYPE)s, %(TEMP_CUVE)s, %(TEMP_EXT)s, %(PLC)s, , %(PP)s, %(MPH)s, %(MK)s, %(NaCi)s, %(NBSALMON)s, %(NBECOLI)s, %(NBLISTERIA)s)"
                      )

            data = {
                'UNITNUMBER': automate['unitNumber'],
                'NUMBER': automate['automataNumber'],
                'TYPE': automate['automataType'],
                'TEMP_CUVE': automate['temp_cuve'],
                'TEMP_EXT': automate['temp_ext'],
                'PLC': automate['poids_lait_cuve'],
                'PP': automate['poids_produit'],
                'MPH': automate['mesure_ph'],
                'MK': automate['mesure_k'],
                'NaCi': automate['NaCi'],
                'NBSALMON': automate['n_bact_salmon'],
                'NBECOLI': automate['n_bact_ecoli'],
                'NBLISTERIA': automate['n_bact_listeria'],
            }

            cursor.execute(insert, data)
            cnx.commit()
            print("Donnée ajoutée")
            cnx.close()

    print("Client déconnecté...")


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
