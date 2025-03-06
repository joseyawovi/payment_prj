from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from userauths.models import User

def registerView(request):
    form = UserRegisterForm() 

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully")

            new_user = authenticate(username=form.cleaned_data["email"],  # ✅ Fixed dictionary access
                                    password=form.cleaned_data["password1"])

            if new_user is not None:
                login(request, new_user)
                return redirect("core:index")

    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("core:index")
        

    context = {"form": form}
    return render(request, "userauths/sign-up.html", context)

def loginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
       
        
        try:
            user = User.objects.get(email = email)
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in")
                return redirect("core:index")
            else:
                messages.success(request,"Incorrect Credentials")
                return redirect("userauth:sign-in")
                
        except:
            messages.success(request,"User does not exist")
        
    return render(request, "userauths/sign-in.html")

def logoutView(request):
    logout(request)
    messages.success(request,"You have been logged out.")
    return redirect("userauths:sign-in")