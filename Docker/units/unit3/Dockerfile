# On pull l'image python taggé en version 3 depuis le repository Docker
FROM python:3.7

# On install cron
RUN apt-get update && apt-get -y install cron

# On copie le script de génération de la donnée vers les conteneurs
COPY script.py /home/scripts

# Cron into the container
COPY crontab /home/crontab

# On donne les droits 
RUN chmod +x /home/crontab

# On lance la crontab
RUN crontab /home/crontab

# On copie le fichier de conf de l'unité
COPY conf.json /home/config
