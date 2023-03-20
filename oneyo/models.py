from django.db import models

class Member(models.Model):
    memberNo = models.AutoField(primary_key=True)
    status = models.IntegerField(null=False)
    Id = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)

class Favorite(models.Model):
    favNo = models.AutoField(primary_key=True)
    memberNo = models.ForeignKey('Member', on_delete=models.CASCADE)
    cookNo = models.ForeignKey('Cook', on_delete=models.CASCADE)
    input = models.CharField(max_length=200, null=True)

class Cook(models.Model):
    cookNo = models.AutoField(primary_key=True)
    channel = models.CharField(max_length=200, null=False)
    title = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=200, null=False)
    ingredient = models.CharField(max_length=200, null=False)
    thumbnail = models.CharField(max_length=500, null=False)
