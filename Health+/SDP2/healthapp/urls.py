
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage ,name='home'),
    path('signup/', views.registerPage, name='register'),
	#path('user/register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('contact/',views.contactPage,name="contact"),
    path('forgot/',views.forgotpage,name='forgot'),
    path('about/',views.aboutPage,name="about"),
    path('mid/',views.midPage,name="mid"),
    path('appointment/',views.appointmentPage,name="appointment"),
    path('medicine/',views.medicinePage,name="medicine"),
    path('medicine/Successful/',views.SuccessfulPage,name="Successful"),
    path('new/',views.newPage,name="new"),
    path('service/',views.servicePage,name="service"),
    path('new/doctors/',views.DoctorsPage,name="doctors"),
    path('pay/',views.payPage,name="pay"),
    path('pay/Success/',views.successPage,name="success"),
    path('logout/', views.logoutUser, name="logout"),
    path('newdisease/',views.DieasePage,name="newdisease"),
    path('displaydiseases/',views.DiseasesDisplayPage,name="displaydiseases"),
    path('new/orthoedic/',views.Orthopedic,name="orthopedic"),
    path('new/cardiology/',views.Cardiology,name="cardiology"),
    path('new/pulmonogy/',views.Pulmonogy,name="pulmonogy"),
    path('new/neurology/',views.Neurology,name="neurology"),
   # path('appointment/',views.appointmentPage,name="appointment"),

]