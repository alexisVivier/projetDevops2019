# On pull l'image python taggé en version 3 depuis le repository Docker
FROM python:3.7

WORKDIR /usr/src/app

# On copie le script de génération de la donnée vers les conteneurs
ADD ./scripts/script.py .
RUN chmod 755 ./script.py

# Copy du fichier qui va remplacer le cron
ADD ./scripts/initialize.py .

# On copie le fichier de conf de l'unité
ADD ./units/unit2/conf.json .
RUN chmod 777 ./conf.json


RUN python --version

CMD [ "python", "initialize.py" ]
