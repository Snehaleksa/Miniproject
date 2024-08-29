from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,CustomUser,Bank

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
# Create your views here.


def Login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            if user.usertype=="user":
                return redirect(userhome)
            elif user.usertype=="bank":
                return HttpResponse("success")
        else:
            context ={
                'message': "Invalid credentials"
            }
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
     








def Register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        
        account_no=request.POST['account_no']
        image=request.POST['image']
        address=request.POST['address']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
        dob=request.POST['dob']
        adharcard=request.POST['adharcard']
        pancard=request.POST['pancard']
        initial_amount=request.POST['initial_amount']
        data=CustomUser.objects.create_user(username=username,password=password)
        data=User.objects.create(user_id=data,name=name,account_no=account_no,image=image,address=address,email=email,age=age,phone=phone,dob=dob,adharcard=adharcard,pancard=pancard,initial_amount=initial_amount,user_type='user')
        data.save()
        return HttpResponse('success')
    else:
        return render(request,'userregister.html') 
    
def bankregister(request):
    if request.method=='POST':
        name=request.POST['name']
        ifsc=request.POST['ifsc']
        branch=request.POST['branch']
        pincode=request.POST['pincode']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        
        data=CustomUser.objects.create_user(username=username,password=password,user_type='bank')
        data1=Bank.objects.create(bank_id=data,name=name,ifsc=ifsc,brach=branch,pincode=pincode,email=email,username=username,password=password)
        data1.save()
        return HttpResponse("success")
    else:
        return render(request,'bankreg.html')

def userhome(request):
    data=User.objects.get(id=request.user.id)
    return render(request,'userhome.html',{'data':data})