from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    vacation_days = models.IntegerField()
    working_days = models.IntegerField()
    holiday_days = models.IntegerField()

    def __str__(self):
        return self.name
