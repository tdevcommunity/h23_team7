from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Annonce)
admin.site.register(CV)
admin.site.register(Certification)
admin.site.register(Commentaire)
admin.site.register(Profil)
admin.site.register(Evaluation)