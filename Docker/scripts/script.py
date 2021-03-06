#!/usr/bin/env python

import random
import json
import time
import os
import datetime
import socket
import calendar

with open('conf.json', 'r') as f:
    confstore = json.load(f)

finalData = []
data = {}

# oldFileName = "1_" + str(datetime.datetime.now() - datetime.timedelta(minutes=1))

for i in range(1, 11):
    # if 'data.json':
    #     with open("%s.json" % oldFileName, 'r') as f:
    #         datastore = json.load(f)

    currAuto = "automata" + str(i)

    # poids_lait_cuve_old = datastore[currAuto]["data"]["poids_lait_cuve"]
    # poids_lait_cuve = round(random.uniform(3512, 4607))

    mesure_ph= round(random.uniform(6.8, 7.2), 1),
    mesure_k = round(random.uniform(35, 47)),
    NaCi = round(random.uniform(1, 1.7), 1),
    n_bact_salmon = round(random.uniform(17, 37)),
    n_bact_ecoli = round(random.uniform(35, 49)),
    n_bact_listeria = round(random.uniform(28, 54)),
    temp_cuve = round(random.uniform(2.5, 4), 1),
    temp_ext = round(random.uniform(8, 14), 1),
    poids_lait_cuve = round(random.uniform(3512, 4607)),

    data = {
        "unitNumber": confstore["unitNumber"],
        "automataNumber": confstore["automata"][currAuto]["automataNumber"],
        "automataType": confstore["automata"][currAuto]["automataType"],
        "temp_cuve": temp_cuve[0],
        "temp_ext": temp_ext[0],
        "poids_lait_cuve": poids_lait_cuve[0],
        # "poids_produit" : abs(poids_lait_cuve_old - poids_lait_cuve),
        "poids_produit": 0,
        "mesure_ph": mesure_ph[0],
        "mesure_k": mesure_k[0],
        "NaCi": NaCi[0],
        "n_bact_salmon": n_bact_salmon[0],
        "n_bact_ecoli": n_bact_ecoli[0],
        "n_bact_listeria": n_bact_listeria[0],
    }

    finalData.append(data)

    i += 1

time = calendar.timegm(time.gmtime())
fileName = "1_" + str(time) + ".json"

with open(fileName, 'w+') as outfile:
    json.dump(finalData, outfile, indent=1)

hote = "172.28.1.3"
port = 1111

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

with open(fileName, 'rb') as _file:
    socket.send(_file.read())

socket.recv(2048)

socket.close()
