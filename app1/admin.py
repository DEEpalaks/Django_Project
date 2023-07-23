from django.contrib import admin
from .models import app1
# Register your models her
admin.autodiscover()
admin.site.register(app1)