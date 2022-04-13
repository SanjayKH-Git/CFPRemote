from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import CFPUsers
#from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
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
    if uname in UName_list:
        ucred = CFPUsers.objects.get(UName=uname)
        if pswd == ucred.password:
            #return HttpResponse("CFP Login Success")
            return render(request,'CFP_Panel.html')
        else:
            return HttpResponse("Email or Password Wrong... Enter Correct details")
    else:
        return HttpResponse("You Don't have permission, Contact CyberSapiens")

def punish(request):
   try:
    phno = request.POST.get('PhoneNo')
    email = request.POST.get('Email')

    print(phno)
    print(email)

    if phno:
        os.system("chmod +x ./static/Bomber/Tsunami.sh")
        os.system("printf '" + phno + "\n15\n' | ./static/Bomber/Tsunami.sh")
        return render(request, 'CFP_Panel.html')
        #return HttpResponse("<h2>Attacking on " + phno + "</h2>")

    elif email:
        print(type(email))

        os.system('rm -rf data/nodes.json data/dead_providers.json')
        os.system('timeout 10s php index.php update-nodes')
        os.system('timeout 10s php index.php start-bombing '+ email)
        return render(request, 'CFP_Panel.html')

   except Exception as e:
       print(str(e))
       return HttpResponse("<h2>Attacking on finished</h2>")


   return render(request, 'CFP_Panel.html')
