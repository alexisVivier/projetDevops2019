# On pull l'image python taggé en version 3 depuis le repository Docker
FROM python:3.7

# On copie le script de génération de la donnée vers les conteneurs
ADD ./units/unit4/script.py /home/scripts

# Copy du fichier qui va remplacer le cron
ADD ./units/unit4/initialize.py /home/scripts

# On copie le fichier de conf de l'unité
ADD ./units/unit4/conf.json /home/config

CMD [ "python", "initialize.py" ]
