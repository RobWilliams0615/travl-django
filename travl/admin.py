from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Facility
from .models import User
from .models import Location
admin.site.register(Facility)
admin.site.register(User)
admin.site.register(Location)
