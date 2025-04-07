from django.urls import path
from . import views
from . import transfer
app_name ="core"

urlpatterns = [
    path("",views.index,name="index"),

    #tranfer
    path("seach-account",transfer.search_users_account_number,name="search_account"),
    path("amount_transfer/<account_number>",transfer.amountTransfer,name="amount_transfer"),

]
