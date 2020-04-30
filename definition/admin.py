from django.contrib import admin

# Register your models here.
# relative import 
from .models import Definition
# render
admin.site.register(Definition)
