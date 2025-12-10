from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



def user_login(request):
    if 'user_id' in request.session:
        return redirect("show_contact") 
    if request.method == "POST":
        
        # print("Session data:", request.session.items())
    
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Empty both field ?
        if not email or not password:
            messages.error(request, "Email and Password are required")
            return render(request, 'login.html')

        # for formate email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid Email Format")
            return render(request,'login.html')

        # check in db
        try:
            user = Registration.objects.get(email=email, password=password)
            messages.success(request, "Login Successful")
            # return redirect('home')
        except Registration.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
            return render(request,'login.html')
                        
        
        request.session["user_id"] = user.id   # session store
        #auto generated id because always user_id is exists (for new user_id auto increment is done)
        print("Logged in user ID:", user.id)
        return redirect("show_contact")
        
    return render(request, "login.html")



def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confrimpassword")

        context ={
            "username": username,
            "email": email,
        }
        # check all feild
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return render(request,'signup.html')

        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid Email Format")
            return render(request,'signup.html',context)

        # for duplicate email check
        if Registration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request,'signup.html',context)

        # Password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request,'signup.html',context)

      
        Registration.objects.create(name=username, email=email, password=password)
        messages.success(request, "Signup Successful! You can now login.")
        return redirect('login')

    return render(request, "signup.html")


# validate-email() ka regex ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
# .get() return the object if exist  else throw error
# username = request.POST.get("username") in this get is dict-function
# Registration.objects.get(email=email,password=password) get  django ORM database function 
# ahiya me login no path("")empty eakhto che aetle hu form ma submit karti vakhte action nahi lakhto aeno matlb ke data ae j jagya ae jase aetle ko loginpage


## validaiton for login 
# 1. bane or banemathi aek pan empty na hovu joie
# 2.email formate
# 3. credential db ma hovu joie 

## signup validation
# 1. check for empty field
# 2. email formate
# 3. password == confirmpassword
# 4. duplicate email check