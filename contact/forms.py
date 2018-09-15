from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nomnre", required="True")
    email = forms.EmailField(label = "Email", required="True")
    contect = forms.CharField(label = "Contenido", required="True", widget=forms.Textarea)