from django.contrib import admin
from .models import Question


# 告诉管理对象, Question对象需要被管理
admin.site.register(Question)

