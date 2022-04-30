from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment , Medicine , Pay

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name','last_name','email', 'password1','password2']

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['email','name','phonenumber','gender','hospitalname','date']

class MedicineForm(forms.ModelForm):
	class Meta:
		model = Medicine
		fields = ['name','DOB','Medicinename','mobilenumber','Postalcode','email','address']

class PayForm(forms.ModelForm):
	class Meta:
		model = Pay
		fields = ['Name_on_card','Credit_card_number','Exp_Month','Exp_Year','CVV','Amount_to_be_paid']			


