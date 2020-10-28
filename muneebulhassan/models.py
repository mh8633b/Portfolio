from django.db import models

# Create your models here.
class connect(models.Model):
    u_name = models.CharField(max_length=50)
    u_subject = models.CharField(max_length=100)
    u_email = models.CharField(max_length=300)
    def __str__(self):
        return self.u_name


class project(models.Model):
    p_name = models.CharField(max_length=30)
    p_link = models.CharField(max_length=100)
    p_description = models.CharField(max_length=110)
    p_framework = models.CharField(max_length=50)

    def __str__(self):
        return self.p_name

class experience(models.Model):
    e_name = models.CharField(max_length=30)
    e_post = models.CharField(max_length=50)
    e_startdate = models.CharField(max_length=30)
    e_enddate = models.CharField(max_length=30)

    def __str__(self):
        return self.e_name

class experiencedetail(models.Model):
    e_name = models.ForeignKey(experience,on_delete=models.DO_NOTHING)
    e_detail = models.CharField(max_length=100)

    def __str__(self):
        return self.e_name

