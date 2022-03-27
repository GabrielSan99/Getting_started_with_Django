from django.contrib import admin

# Register your models here.

from .models import Question

admin.site.register(Question) #Traz as informações do Question para a página admin