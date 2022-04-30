from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment ,Medicine ,Pay
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from .models import Diseases


from django.contrib import messages

from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_protect
#from .models import *
from .forms import CreateUserForm,AppointmentForm,MedicineForm,PayForm
# Create your views here.
def homePage(request):
    return render(request,'home.html')
def forgotpage(request):
  return render(request,'forgot.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('new')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user_email = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + user_email)
                subject = 'welcome to HWS '
                message = f'HI {user_email}, thank you for registering with HWS.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user_email,]
                # send_mail(subject, message, email_from, recipient_list)
                return render(request,'new.html',{'message':message})
    context = {'form': form}
    return render(request, 'signup.html', context)








def loginPage(request):
    if request.user.is_authenticated:
        return redirect('new')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                message="sucessfully logged in"
                # request.session['appointment_name'] = Appointment.name
                # request.session['email'] = Appointment.email
                return render(request,'new.html',{'message':message})
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')

def contactPage(request):
    return render(request,'contact.html')

def aboutPage(request):
    return render(request,'about.html')

def midPage(request):
    return render(request,'mid.html')

def newPage(request):
    return render(request,'new.html')

@login_required(login_url = 'login')
def appointmentPage(request):
    form = AppointmentForm()
    if request.method == 'POST':
     form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        appoinment = form.cleaned_data.get('email')
        messages.success(request, 'Account was created for ' + appoinment)
        return redirect('pay')
    context = {'form': form}
    return render(request,'appointment.html',context)

@login_required(login_url = 'login')
def medicinePage(request):
    form = MedicineForm()
    #if request.method == 'POST':
    form = MedicineForm(request.POST)
    if form.is_valid():
        form.save()
        # = form.cleaned_data.get('email')
        #messages.success(request, 'Account was created for ' + medicine
        return redirect('Successful')
    context = {'form': form}
    return render(request,'medicine.html',context)

@login_required(login_url = 'login')
def payPage(request):
    form = PayForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success')
    context = {'form': form}
    return render(request,'pay.html',context)



@login_required(login_url = 'login')
def servicePage(request):
    context = {}
    return render(request,'service.html',context)

@login_required(login_url = 'login')
def DieasePage(request):
    if request.method=='POST':
        disease=Diseases()
        disease.diseases_name = request.POST.get('diseases_name')
        disease.medicine_prescribed =request.POST.get('medicine_prescribed')
        disease.cause_of_the_disease =request.POST.get('cause_of_the_disease')
        disease.affected_people_number=request.POST.get('affected_people_number')
        disease.Specialist_doctor=request.POST.get('Specialist_doctor')
        disease.save()

    context = {}
    return render(request,'diseases.html',context)

@login_required(login_url='login')
def DiseasesDisplayPage(request):
    data=Diseases.objects.all()
    eve={
 "diseases_d" : data
 }
    return render(request,"displaydiseases.html",eve)




@login_required(login_url = 'login')
def DoctorsPage(request):
    context = {}
    return render(request,'doctors.html',context)


@login_required(login_url = 'login')
def SuccessfulPage(request):
    return render(request,'Successful.html')

@login_required(login_url = 'login')
def successPage(request):
    return render(request,'Success.html')

def Orthopedic(request):
    return render(request,"orthopedic.html")

def Cardiology(request):
    return render(request,"cardiology.html")

def Pulmonogy(request):
    return render(request,"pulmonogy.html")

def Neurology(request):
    return render(request,"neurology.html")

