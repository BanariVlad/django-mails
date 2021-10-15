from django.db import models
from django.db import models


class Mail(models.Model):
    mail_text = models.CharField(max_length=2000)
    mail_subject = models.CharField(max_length=100, null=True)
    mail_is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.mail_text
# Create your models here.
