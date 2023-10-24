from django.db import models
from django.contrib.auth.models import AbstractUser

Role_Choices=(('Administrateur','Administrateur'),
('Membre','Membre'),
('Mentor','Mentor'),
('Evaluateur','Evaluateur'),
)
# Create your models here.
class Utilisateur(AbstractUser):
    Id=models.BigAutoField(primary_key=True)
    Nom=models.CharField(max_length=50)
    Prenom=models.CharField(max_length=70)
    Role=models.CharField(max_length=20, choices=Role_Choices,default='Membre')
    Etat=models.BooleanField(default=True)

    class Meta:
        db_table="Utilisateur"

    

    def __str__(self):
        return f"{self.Nom}-{self.Prenom}"


class Profil(models.Model):
    Utilisateur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    IdProfil=models.BigAutoField(primary_key=True)
    Photo=models.ImageField(upload_to='images/',default=None)
    Note=models.PositiveIntegerField()
    Etat=models.BooleanField(default=True)


class Certification(models.Model):
    Profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    IdCertif=models.BigAutoField(primary_key=True)
    Libelle=models.CharField(max_length=50)
    Fichier=models.FileField(upload_to='Fichier_Certif/',blank=True)
    Etat=models.BooleanField(default=True)


Statut_Choices=(('En attente','En attente'),
('Evalué','Evalué'),)
class CV(models.Model):
    Profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    IdCv=models.BigAutoField(primary_key=True)
    FichierCv=models.FileField(upload_to='Fichier_CV/')
    Statut=models.CharField(max_length=20,choices=Statut_Choices,default='En attente')
    Etat=models.BooleanField(default=True)



Critere_Choices=(('Mise en forme','Mise en forme'),
('Pertinence','Pertinence'),
('Section','Section'),)
class Evaluation(models.Model):
    IdEval=models.BigAutoField(primary_key=True)
    Date=models.DateTimeField(auto_now=True)
    Critere=models.CharField(max_length=30,choices=Critere_Choices)
    Recommandations=models.TextField()
    Etat=models.BooleanField(default=True)



class Commentaire(models.Model):
    IdCommentaire=models.BigAutoField(primary_key=True)
    Remarque=models.TextField()
    Date=models.DateTimeField(auto_now=True)
    Etat=models.BooleanField(default=True)



class Annonce(models.Model):
    IdAnnonce=models.BigAutoField(primary_key=True)
    Libelle=models.CharField(max_length=200)
    DateDebut=models.DateTimeField()
    DateFin=models.DateTimeField()
    Description=models.TextField()
    Etat=models.BooleanField(default=True)



