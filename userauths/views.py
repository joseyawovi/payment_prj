from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.
def RegisterView(request):
    form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"userauths/sign-up.html")
