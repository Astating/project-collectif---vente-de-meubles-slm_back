from django.db import models

# formulaire pour les utilisateurs
# c'est le modèle pour la bdd


class Clients (models.Model):
    id = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=10, default='Choose an alias')
    email = models.CharField(max_length=35, default='Add your e-mail here')
    #password = models.CharField#
    zipcode = models.IntegerField(default='Add your zip code')
    bio = models.TextField(max_length=280, default='Add a bio')
