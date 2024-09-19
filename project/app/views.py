from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,CustomUser,Bank,Transaction

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
# Create your views here.


def index(request):
    return render(request,'index1.html')

def Login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username,password=password)
        admin_user=authenticate(request,username=username,password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect(admin)
        
        elif user is not None:
            login(request,user)
            if user.user_type=="user" and user.status=='accepted':
                return redirect(userhome)
            elif user.user_type=="bank":
                return redirect(bankhome)
            else:
                return render(request,'login.html',{'message': "admin not aproved"})
        else:
            context ={
                'message': "Invalid credentials"
            }
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
     






#user....

def Register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        
        account_no=request.POST['account_no']
        image=request.FILES['image']
        address=request.POST['address']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
        dob=request.POST['dob']
        adharcard=request.POST['adharcard']
        pancard=request.POST['pancard']
        initial_amount=request.POST['initial_amount']
        data=CustomUser.objects.create_user(username=username,password=password,user_type='user')
        data1=User.objects.create(user_id=data,name=name,account_no=account_no,image=image,address=address,email=email,age=age,phone=phone,dob=dob,adharcard=adharcard,pancard=pancard,initial_amount=initial_amount)
        data1.save()
        return redirect(index)
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
        data1=Bank.objects.create(bank_id=data,name=name,ifsc=ifsc,branch=branch,pincode=pincode,email=email,username=username,password=password)
        data1.save()
        return redirect(index)
    else:
        return render(request,'bankreg.html')

def userhome(request):
    data=CustomUser.objects.get(id=request.user.id)
    data1=User.objects.get(user_id=data)
    
    return render(request,'userhome.html',{'data1':data1})


def profileview(request):
    data=CustomUser.objects.get(id=request.user.id)
    data1=User.objects.get(user_id=data)
    return render(request,'profileview.html',{'data1':data1})

def edit(request,id):
    data=User.objects.get(id=id)
    if request.method=="POST":
        data.name=request.POST['name']
    
        data.email=request.POST['email']
        data.address=request.POST['address']
        data.age=request.POST['age']
        data.adharcard=request.POST['adharcard']
        data.dob=request.POST['dob']
        data.phone=request.POST['phone']
        data.pancard=request.POST['pancard']
        if 'image' in request.FILES:
            data.image=request.FILES['image']
        data.save()
        return redirect(profileview)
    else:
        return render(request,'edit.html',{'data':data}) 
    



def more(request):
    data=CustomUser.objects.get(id=request.user.id)
    user=User.objects.get(user_id=data)
    bank=Bank.objects.all()
    
    return render(request,'more.html',{'user':user,'bank':bank})    

def deposite(request):
    data=CustomUser.objects.get(id=request.user.id)
    user=User.objects.get(user_id=data)
    bank=Bank.objects.all()
    if request.method=="POST":
        amount=request.POST['amount']
        if int(amount) > 0:
            user.initial_amount=user.initial_amount+int(amount)
            user.save()
            data1=Transaction.objects.create(transaction_id=data,amount=amount,balance=user.initial_amount,details='deposite')
            data1.save()
            return redirect(userhome)
        else:
            return render(request,'deposite.html',{'message':"invalid amount"})
    else:
        return render(request,'deposite.html',{'user':user,'bank':bank})


def withdrow(request):
    data=CustomUser.objects.get(id=request.user.id)
    user=User.objects.get(user_id=data)        
    if request.method=="POST":
        amount=request.POST['amount']
        if 0< int(amount)<user.initial_amount:
            user.initial_amount=user.initial_amount-int(amount)
            data.save()
            data1=Transaction.objects.create(transaction_id=data,amount=amount,balance=user.initial_amount,details='debit')
            user.save()
            return redirect(userhome)
        else:
            return render(request,'withdrow.html',{'user':user},{'message':"invalid amount"})
    else:
        return render(request,'withdrow.html')   


def history(request):
    data=CustomUser.objects.get(id=request.user.id)
    user=Transaction.objects.filter(transaction_id=data)
    return render(request,'history.html',{'user':user})


def Logout(request):
    auth.logout(request)
    return redirect(Login)


#bank
def bankhome(request):
    data=CustomUser.objects.get(id=request.user.id)
    data1=Bank.objects.get(bank_id=data)

    
    return render(request,'bankhome.html',{'data1':data1})

def bankviewuser(request):
    user=User.objects.all()
    return render(request,'bankviewuser.html',{'user':user}) 

def bankuser(request,id):
    user=User.objects.get(id=id)
    return render(request,'bankuser.html',{'user':user})       

def bankuserhistory(request,id):
    user=User.objects.get(id=id)
    data=CustomUser.objects.get(id=user.user_id.id)
    data1=Transaction.objects.filter(transaction_id=data) 
    return render(request,'userhistory.html',{'data1':data1}) 


def admin(request):
    return render(request,'admin.html')

def viewusers(request):
    user=User.objects.all()
    return render(request,'viewusers.html',{'user':user}) 


def index1(request):
    return render(request,'index1.html')



def adminuseraccept(request,id):
    data=User.objects.get(id=id)
    if request.method=='POST':
        status =request.POST.get('status')
        if status=='accepted':
            data.user_id.status='accepted'
        elif status=='rejected':
            data.user_id.status='rejected'
        data.user_id.save()
        return redirect(viewusers)
    else:
        return redirect(viewusers)  
