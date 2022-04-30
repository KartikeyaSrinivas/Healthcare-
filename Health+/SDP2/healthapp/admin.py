from django.contrib import admin

# Register your models here.

#from .models import UserCreationForm
#admin.site.register(UserCreationForm)

from .models import Appointment
admin.site.register(Appointment)

from .models import Medicine
admin.site.register(Medicine)

from .models import Doctor
admin.site.register(Doctor)

from .models import Diseases
admin.site.register(Diseases)

from .models import Pay
admin.site.register(Pay)

