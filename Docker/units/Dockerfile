# On pull l'image python taggé en version 3 depuis le repository Docker
FROM python:3.7

# On install cron
RUN apt-get update && apt-get -y install cron

# On copie le script de génération de la donnée vers les conteneurs
COPY script.py /scripts

# Cron into the container
COPY crontab /home

# On donne les droits 
RUN chmod +x /crontab

# On lance la crontab
RUN crontab /crontab
