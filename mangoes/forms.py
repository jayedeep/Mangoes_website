from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser,Mango_For_Sell,Mangoes_For_Buy,Deliver


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_pic','first_name','last_name','email','address','farm_name', 'password1', 'password2','contact')


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_pic','first_name','last_name','email','address','farm_name','contact']

class Mangoes_for_sell_form(forms.ModelForm):
    class Meta:
        model=Mango_For_Sell
        fields='__all__'

class Mangoes_for_buy_form(forms.ModelForm):
    class Meta:
        model=Mangoes_For_Buy
        fields="__all__"

class Delivery_form(forms.ModelForm):
    class Meta:
        model=Deliver
        fields=['owner_of_product','product','diliverd','delivery_at']