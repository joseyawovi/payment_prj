from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def RegisterView(request):
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
