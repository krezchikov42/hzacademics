from django.db import models
from django.conf import settings

class Class(models.Model):
    course_num = models.CharField(max_length=64)
    professor = models.CharField(max_length=64)
    semester = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    confidence_level = models.IntegerField(default=0)