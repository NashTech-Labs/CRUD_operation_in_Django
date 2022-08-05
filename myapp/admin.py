from django.contrib import admin
from .models import employees
from .models import empadd
from .models import hobbies
from .models import parents


admin.site.register(employees)
admin.site.register(empadd)
admin.site.register(hobbies)
admin.site.register(parents)


# Register your models here.
