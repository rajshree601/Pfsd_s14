from django.contrib import messages
from django.shortcuts import render

from .models import Admin, Register, Packages


def ttmhome(request):
    return render(request, "ttmhome.html")


def loginfail(request):
    return render(request, "loginfail.html")


def checkadminlogin(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        # flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
        flag = Register.objects.filter(username=uname, password=pwd).values()
        # if flag:
        #    if uname == "grkrao" :
        #       messages.info(request, "This is a admin page for TTM project...")
        #        return render(request, "adminhome.html")
        if flag:
            return render(request, "ttmhome.html")
        else:
            messages.info(request, "This is a admin page for TTM project...")
            return render(request, "adminhome.html")


def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username taken...")
                return render(request, "register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name, address=addr, email=email, phno=phno, username=uname,
                                               password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")


def checkpackage(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        desc = request.POST["tourdesc"]
        pack = Packages.objects.create(tourcode=tcode, tourname=tname, tourpackage=tpack, desc=desc)
        pack.save()
        messages.info(request, "Data Inserted Successfully")  # sends the msg to next html page
        return render(request, "adminhome.html")


def viewplaces(request):
    data = Packages.objects.all()  # get all rows from package_table
    return render(request, "viewplaces.html", {"placesdata": data})


def checkchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Register.objects.filter(username=uname, password=opwd).values()
        if flag:
            Register.objects.filter(username=uname, password=opwd).update(password=npwd)
            return render("index.html")
    else:
        return render(request, "changepassword.html")

def logout(request):
    return render(request, "logout.html")
