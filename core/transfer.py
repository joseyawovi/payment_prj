from account.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages
@login_required
def search_users_account_number(request):
    # account = Account.objects.filter()
    account = Account.objects.all()
    query = request.POST.get("account_number")
    if query:
        account = account.filter(
            Q(account_number=query)|
            Q(account_id=query)
        ).distinct()

    context = {
        "account":account,
        "query":query,
    }
    return render(request,"transfer/search_user_by_account.html",context)

def amountTransfer(request,account_number):
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        messages.warning(request,"Account Does not exist")
        return redirect("core:search_account")
    context = {
        "account":account,
    }
    return render(request,"transfer/amount_transfer.html",context)
