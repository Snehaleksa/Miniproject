from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    user_type=models.CharField(max_length=100)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)


class User(models.Model):
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    account_no=models.IntegerField()
    image=models.FileField(upload_to='media')
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    dob=models.DateField()
    adharcard=models.IntegerField()
    pancard=models.IntegerField()
    initial_amount=models.IntegerField()
    



    def __str__(self):
        return self.name


class Bank(models.Model):
    bank_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    ifsc=models.IntegerField()
    brach=models.CharField(max_length=100)
    pincode=models.IntegerField()
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    
    details=models.CharField(max_length=100)
    amount=models.IntegerField()
    balance=models.IntegerField()

    