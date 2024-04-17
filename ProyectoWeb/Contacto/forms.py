from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=10, label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)