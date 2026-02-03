from django.contrib import admin
from .models import *


admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Newsletter)

# Register your models here.
