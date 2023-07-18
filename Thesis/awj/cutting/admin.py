from django.contrib import admin
from django.contrib.admin.decorators import register
from cutting.models import Cut

# Register your models here.
admin.site.register(Cut)
