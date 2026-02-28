from django.db import models

class Teacher(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.SmallIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    fan = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ism}"
