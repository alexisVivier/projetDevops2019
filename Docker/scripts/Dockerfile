# On pull l'image python taggé en version 3 depuis le repository Docker
FROM python:3.5

# On copie le script de génération de la donnée vers les conteneurs
ADD ./scripts/script.py /home/scripts/
RUN chmod 755 /home/scripts/script.py

# Copy du fichier qui va remplacer le cron
ADD ./scripts/initialize.py /home/scripts/

# On copie le fichier de conf de l'unité
ADD ./units/unit2/conf.json /home/scripts/
RUN chmod 777 /home/scripts/conf.json


RUN python --version

CMD [ "python", "/home/scripts/initialize.py" ]
