from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Option, UserAnswer
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserAnswer)