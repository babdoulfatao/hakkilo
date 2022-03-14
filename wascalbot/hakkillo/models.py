from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.json import JSONField

class intent(models.Model):
    tag = models.CharField(max_length=255, verbose_name="Titre")
    commentaire = models.CharField(max_length=255)
    pattern = JSONField(default=list, verbose_name="Question")
    response =JSONField(default=list, verbose_name="Reponse") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class organisation(models.Model):
    nom_org = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=255)
    ville_org = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)

class userprofile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone =  models.CharField(max_length=255)
    Organisation = models.ForeignKey(organisation, on_delete=models.CASCADE)
