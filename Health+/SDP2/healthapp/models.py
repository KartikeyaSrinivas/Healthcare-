from django.db import models

class Appointment(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    hospitalname = models.CharField(max_length=100)
    date = models.DateField(auto_now=False,auto_now_add=False)

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField(auto_now=False,auto_now_add=False)
    Medicinename = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Postalcode=models.CharField(max_length=100)
    address = models.TextField(blank=True)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField() 
    experience = models.IntegerField()
    hospital_currently_working = models.CharField(max_length=100)
    languages_known = models.IntegerField()
    specilization = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Diseases(models.Model):
    diseases_name = models.CharField(max_length=100)
    medicine_prescribed = models.CharField(max_length=100)
    cause_of_the_disease = models.CharField(max_length=100)
    affected_people_number = models.IntegerField()
    Specialist_doctor = models.CharField(max_length=100)

class Pay(models.Model):
    Name_on_card = models.CharField(max_length = 100)
    Credit_card_number = models.CharField(max_length = 20)
    Exp_Month = models.CharField(max_length=20)
    Exp_Year = models.CharField(max_length=4)
    CVV = models.CharField(max_length=4)
    Amount_to_be_paid = models.CharField(max_length=3 , default="500")

class Contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.CharField(max_length=100)
    contact_phone=models.CharField(max_length=100)
    contact_message=models.TextField(blank=True)


    


