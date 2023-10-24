from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control','placeholder': 'Entrer votre nom d\'utilisateur'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Entrer votre mot de passe'}))



class RegistrationForm(UserCreationForm):
    username=forms.CharField(label='Nom d\'utilisateur',widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control','placeholder': 'Entrer votre nom d\'utilisateur'}))
    Nom=forms.CharField(label='Prénoms',widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control','placeholder': 'Entrer votre prénom'}))
    Prenom=forms.CharField(label='Nom',widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control','placeholder': 'Entrer votre nom'}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Entrer votre  e-mail'}))
    password1=forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Au moins 8 caractères'}))
    password2=forms.CharField(label='Confirmer votre mot de passe',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirmer votre mot de passe'}))
    class Meta:
        model=Utilisateur
        fields=['username','Nom','Prenom', 'Email','password1', 'password2']
