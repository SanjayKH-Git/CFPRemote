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
            #return HttpResponse("CFP Login Success")
            return render(request,'CFP_Panel.html')
        else:
            return HttpResponse("Email or Password Wrong... Enter Correct details")
            print('sk')
    else:
        return HttpResponse("You Don't have permission, Contact CyberSapiens")

def punish(request):
   try:
    phno = request.POST.get('PhoneNo')
    if phno:
        os.system("chmod +x ./static/Bomber/Tsunami.sh")
        os.system("printf '" + phno + "\n1\n' | ./static/Bomber/Tsunami.sh")
        return HttpResponse("<h2>Attacking on " + phno + "</h2>")
   except Exception as e:
       return HttpResponse("<h2>Attacking on" + phno + " finished</h2>")
   return render(request, 'CFP_Panel.html')
