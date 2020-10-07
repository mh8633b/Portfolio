from django.contrib import admin

# Register your models here.
from .models import connect, project, experience, experiencedetail

admin.site.register(connect)
admin.site.register(project)
admin.site.register(experience)
admin.site.register(experiencedetail)