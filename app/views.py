from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def IndexPage(request):
    if 'email' in request.session or 'aemail' in request.session:
        print(f"IN MAIN INDEX CONDITION | ROLE = {request.session['role']}")
        
        if request.session['role'] == "Admin":
            admin = Admin.objects.get(id=request.session['aid'])
            return render(request, "app/index.html",{'user':admin})

        elif request.session['role'] == "HR":
            print("IN HR INDEX")
            admin = Admin.objects.get(id=request.session['id'])
            hr = Hr.objects.get(admin=admin)
            return render(request, "app/index.html",{'user':hr})

        elif request.session['role'] == "Employee":
            admin = Admin.objects.get(id=request.session['id'])
            emp = Emp.objects.get(admin=admin)
            return render(request, "app/index.html",{'user':emp})
    else:
        return redirect('/')

def LoginPage(request):
    return render(request, "app/login.html")

def AdminAddHR(request):
    return render(request, "app/admin-add-hr.html")

def Login(request):
    role = request.POST['role']
    email = request.POST['email']
    passwd = request.POST['passwd']

    admin = Admin.objects.filter(email=email)
    if len(admin) > 0:
        if admin[0].password==passwd:
            if admin[0].role == "Admin":
                print("IN ADMIN")
                request.session['aid'] = admin[0].id
                request.session['aemail'] = admin[0].email
                request.session['role'] = admin[0].role
                return redirect('indexpage')
            elif admin[0].role == "HR":
                hr = Hr.objects.get(admin=admin[0])
                request.session['id'] = admin[0].id
                request.session['email'] = admin[0].email
                request.session['role'] = admin[0].role
                request.session['fname'] = hr.firstname
                print("HR LOGIN DONE")
                return redirect('indexpage')
            elif admin[0].role == "Employee":
                emp = Emp.objects.get(admin=admin[0])
                request.session['id'] = admin[0].id
                request.session['email'] = admin[0].email
                request.session['role'] = admin[0].role
                request.session['fname'] = emp.firstname
                return redirect('indexpage')
        else:
            msg = "Password is incorrect"
            return render(request, "app/login.html",{'err':msg})

    else:
        msg = "User Doesn't Found"
        return render(request, "app/login.html",{'err':msg})

def logout(request):
    if request.session['role'] == 'Admin':
        del request.session['aid']        
        del request.session['aemail']
        del request.session['role']
        return redirect("/")
    elif request.session['role'] == 'HR':
        del request.session['id']
        del request.session['email']
        del request.session['role']
        del request.session['fname']
        return redirect("/")
    elif request.session['role'] == 'Employee':
        del request.session['id']
        del request.session['email']
        del request.session['role']
        del request.session['fname']
        return redirect("/")

def Register_HR_EMP(request):
    role = request.POST['role']
    fname = request.POST['fname']
    lname = request.POST['lname']
    eml = request.POST['email']
    password = request.POST['passwd']
    addr = request.POST['address']
    gen = request.POST['gender']
    bdate = request.POST['bdate']
    phn = request.POST['phone']
    mar = request.POST['marital']

    user = Admin.objects.filter(email=eml)
    if len(user) > 0:
        msg = "User Already Exist"
        return render(request, "app/admin-ad-hr",{'err':msg})
    else:
        admin = Admin.objects.create(email=eml,password=password,role=role)
        if admin.role == "HR":
            hr = Hr.objects.create(admin=admin,firstname=fname,lastname=lname,
            address=addr,gender=gen,bdate=bdate,phone=phn,marital=mar)
            return redirect("adminaddhr")
        elif admin.role == "Employee":
            emp = Emp.objects.create(admin=admin,firstname=fname,lastname=lname,
            address=addr,gender=gen,bdate=bdate,phone=phn,marital=mar)