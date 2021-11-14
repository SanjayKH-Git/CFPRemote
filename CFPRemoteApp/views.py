from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import CFPUsers
# Create your views here.

def index(request):
    #return HttpResponse("CFP")
    return render(request,'index.html')

def Login(request):
    uname = request.POST.get('UName')
    Email = request.POST.get('email')
    pswd = request.POST.get('pswd')
    # retrieving PhoneNo from SpamUsers Model
    UName_list = [u.UName for u in CFPUsers.objects.all()]
    # check if  exist in SpamUser Model
    print("worki")
    if uname in UName_list:
        ucred = CFPUsers.objects.get(UName=uname)
        if pswd == ucred.password:
            return HttpResponse("CFP Login Success")
            print("suv")
        else:
            return HttpResponse("Email or Password Wrong... Enter Correct details")
            print('sk')
    else:
        return HttpResponse("You Don't have permission, Contact CyberSapiens")
