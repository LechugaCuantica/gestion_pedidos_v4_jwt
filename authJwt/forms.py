
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, 
                               label='Usuario', 
                               widget=forms.TextInput(attrs={'class': "w-full px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition", 'placeholder': 'Ingresa tu usuario', 'autocomplete': 'off'}))
    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition', 'placeholder': 'Ingresa tu contraseña'}))
    
    
