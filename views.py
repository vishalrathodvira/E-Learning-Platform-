from email import header
from django.shortcuts import redirect, render
from signup.models import Bestdeal,Address,Payment
from signup . models import New_Arrivals,Feature_Product,All_Product,Header,feedback
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from lib2to3.pgen2.tokenize import generate_tokens
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from login import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from . tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

# Create your views here.
def home(request):
    obj=Header.objects.all()

    return render(request,'home.html',{'obj':obj})



#user registration section
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if User.objects.filter(username=username):
            messages.error(request,'Username already exist! Please try some other username.')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
            
        if password != cpassword:
            messages.error(request,"Passwords didn't matched!!")
            return redirect('signup')

        if len(username)>10:
            messages.error(request,"Username must be under 20 charcters!!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request,"user name must be alpha-numeric!")
            return redirect('signup')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        #wellcome Email
        subject =" wellcome to E-Store!!"
        message="Hello " + myuser.first_name + "!! \n" + "Welcome to E-Store Shoping site !! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nVishal Rathod and S-Store Team"
        from_email = settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ E-Store login!!"

        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        send_mail(email_subject,message2,from_email,to_list,fail_silently=False)    
        return redirect('signin')
    return render(request,'signup.html')
#user registration section end


  #Login section
def signin(request):
    if request.method =='POST':
        uname=request.POST['uname']
        passw=request.POST['pass']
        user=authenticate(username=uname,password=passw)
        if user is not None:
            login(request,user)
            fname=user.first_name
            user=User.objects.all()
            obj=New_Arrivals.objects.all()
            obj1=Feature_Product.objects.all()
            obj2=All_Product.objects.all()
            obj3=Bestdeal.objects.all()
            obj4=Header.objects.all()
            data={
                'fname':fname,
                'userid':uname,
                'user':user,
                'obj':obj,
                'obj1':obj1,
                'obj2':obj2,
                'obj3':obj3,
                'obj4':obj4,
            }
            messages.success(request,'You are successfuly login')
            return render(request,'index1.html',{'data':data})
        else:
            messages.error(request,'User Name Not Found Please Register Your Self !')
            return redirect('signin')

    return render(request,'signin.html')

#login section end

#logout section
def signout(request):
    logout(request)
    messages.success(request,'logout sucessful')
    return redirect('home')
#logout section end

#User activation section 
def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        myuser = User.objects.get(pk=uid)
    except ( TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')
#user activation section end


def index1(request):
    user=User.objects.all()
    obj=New_Arrivals.objects.all()
    obj1=Feature_Product.objects.all()
    obj2=All_Product.objects.all()
    obj3=Bestdeal.objects.all()
    obj4=Header.objects.all()


    data={
        'user':user,
        'obj':obj,
        'obj1':obj1,
        'obj2':obj2,
        'obj3':obj3,
        'obj4':obj4,
    }
    return render(request,'index1.html',{'data':data})

def payment(request,obj_id):
    
    product_objects = All_Product.objects.get(id=obj_id)
    


    if request.method == 'POST':

        fullname = request.POST['fullname']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        contry = request.POST['contry']
        zip = request.POST['zipcode']
        


        add=Address(fullname=fullname,email=email,address=address,city=city,state=state,contry=contry,zip=zip)
        add.save()

        cardname = request.POST['cardname']
        crno = request.POST['crno']
        expmonth = request.POST['expmonth']
        expyear = request.POST['expyear']
        cvv = request.POST['cvv']
        pay=Payment(cardname=cardname,crno=crno,expmonth=expmonth,expyear=expyear,cvv=cvv)
        pay.save()
        a=All_Product.price

         #wellcome Email
        subject4 =" wellcome to E-Store Thanks for !!"
        message3="Hello " + add.email + "!! \n" + "Thanks for Visiting E-Store Shoping site !! \nYour Order has been placed \n. Product name are \n\nThanking You\nVishal Rathod and E-Store Team \n Have a Good Day  " 
        from_email = settings.EMAIL_HOST_USER
        to_list=[add.email]
        send_mail(subject4,message3,from_email,to_list,fail_silently=False)
        messages.success(request,"Thanks You" + add.email + "Thanks  ")
        return render (request,'paymentdone.html')





    return render (request,'payment.html',{'product_objects':product_objects})

    
   
       


def detail(request,obj_id):
    product_objects = All_Product.objects.get(id=obj_id)
    return render(request,'detail.html',{'product_objects':product_objects})






   