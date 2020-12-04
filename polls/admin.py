from django.contrib import admin
from django.db.models.query_utils import Q
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
