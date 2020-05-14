from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class R456(models.Model):
    "Generated Model"
    dwdwedw = models.BigIntegerField()


class R123(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class RFFFFF(models.Model):
    "Generated Model"
    rffff = models.BigIntegerField()


class RVBB(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class RVVVV(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class RFFFF(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class VGGGG(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class VVVVV(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class RFFFFFdd(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
