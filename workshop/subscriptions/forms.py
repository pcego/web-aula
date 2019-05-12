from django import forms
from django.core.exceptions import ValidationError
from workshop.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.Form):

    name = forms.CharField(label='Nome',
                           widget=forms.TextInput(attrs={'class': 'contact_input',
                                                         'placeholder': 'Nome'}))
    cpf = forms.CharField(label='CPF',validators=[validate_cpf],
                          widget=forms.TextInput(attrs={'class':'contact_input',
                                                        'placeholder':'CPF'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class':'contact_input',
                                                            'placeholder':'Email'}), required=False)
    phone = forms.CharField(label='Telefone',
                            widget=forms.TextInput(attrs={'class':'contact_input',
                                                          'placeholder':'Telefone'}), required=False)

    def clean_name(self):

        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]

        return ' '.join(words)


    def clean(self):

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu Email ou CPF')

        return self.cleaned_data
