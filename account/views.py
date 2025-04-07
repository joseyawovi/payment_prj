from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import KYC,Account
from account.forms import KYCForm
from django.contrib.auth.decorators import login_required


def account(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except KYC.DoesNotExist:
            messages.warning(request, "You need to submit your KYC")
            kyc = None  # Prevent variable reference error

        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to log in to access the dashboard")
        print("Message sent")  # Debugging: check if this prints
        return redirect("userauths:sign-in")
    context = {
            "account": account,
            "kyc": kyc,
        }
    return render(request, "account/account.html", context)
   

@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None
    
    if request.method == "POST":
        form = KYCForm(request.POST,request.FILES,instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request,"KYC Form submitted successfully,In review now. ")
            return redirect("core:index")
    else:
        form = KYCForm(instance=kyc)
    context = {
        'form':form,
        'kyc':kyc
    }
    print(kyc.image.url)
    return render(request,"account/kyc-form.html",context)