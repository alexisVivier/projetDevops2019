# On pull l'image python taggé en version 3.7 depuis le repository Docker
FROM python:3.7

WORKDIR /usr/src/app

# On copie le script de génération de la donnée vers les conteneurs
ADD ./units/unit1/script.py .
RUN chmod 755 ./script.py

# Copy du fichier qui va remplacer le cron
ADD ./units/unit1/initialize.py .

# On copie le fichier de conf de l'unité
ADD ./units/unit1/conf.json .
RUN chmod 755 ./conf.json

CMD [ "python", "initialize.py" ]