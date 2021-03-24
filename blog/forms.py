from django import forms 

class LoginForm(forms.Form): 
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите свой email',}), label = '')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите свой пароль',}), label = '')
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return self.cleaned_data 