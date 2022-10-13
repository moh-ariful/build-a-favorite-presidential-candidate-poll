from django.contrib import admin

from pollsapp.models import Choice, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
