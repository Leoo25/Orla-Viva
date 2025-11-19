from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormUsuario(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = "Digite um nome sem espaços."        
        self.fields['email'].help_text = None
        self.fields['password1'].label = "Senha"
        self.fields['password1'].help_text = "Use pelo menos 8 caracteres."
        self.fields['password2'].label = "Confirmar Senha"
        self.fields['password2'].help_text = None
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = (
                'w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm '
                'focus:outline-none focus:ring-2 focus:ring-sky-200 focus:border-sky-200 '
                'text-gray-700 bg-gray-50'
            )
    