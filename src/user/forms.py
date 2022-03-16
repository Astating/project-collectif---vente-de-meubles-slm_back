from django import forms

# A utiliser pour la gestion des mots de passe


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
