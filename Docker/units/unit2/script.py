import random
import json
import time
import os
import datetime
import socket

i = 1

if '../config/conf.json':
        with open('../config/conf.json', 'r') as f:
            confstore = json.load(f)

finalData = {"unitNumber" : confstore["unitNumber"],}

oldFileName = "1_" + str(datetime.datetime.now() - datetime.timedelta(minutes=1))

while i <= 10:

    # if 'data.json':
    #     with open("%s.json" % oldFileName, 'r') as f:
    #         datastore = json.load(f)

    currAuto = "automate" + str(i)

    #poids_lait_cuve_old = datastore[currAuto]["data"]["poids_lait_cuve"]
    poids_lait_cuve = round(random.uniform(3512, 4607))

    data = {
        "temp_cuve" : round(random.uniform(2.5, 4), 1),
        "temp_ext" : round(random.uniform(8, 14), 1),
        "poids_lait_cuve" : poids_lait_cuve,
        #"poids_produit" : abs(poids_lait_cuve_old - poids_lait_cuve),
        "poids_produit" : 0,
        "mesure_ph" : round(random.uniform(6.8, 7.2), 1),
        "mesure_k" : round(random.uniform(35, 47)),
        "NaCi" : round(random.uniform(1, 1.7), 1),
        "n_bact_salmon" : round(random.uniform(17, 37)),
        "n_bact_ecoli" : round(random.uniform(35, 49)),
        "n_bact_listeria" : round(random.uniform(28, 54)),
    }
    
    finalData[currAuto] = {
            "automateNumber" : confstore["automate"][currAuto]["automateNumber"],
            "automateType" : confstore["automate"][currAuto]["automateType"],
            "data" : data
        },

    i+=1

fileName = "1_" + str(time.time()) + ""

with open("%s.json" % fileName, 'w') as outfile:
    json.dump(finalData, outfile)


hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

fp = open(fileName, 'rb')
socket.send(fp.read())

socket.close()