from django.shortcuts import render, redirect
from Backend.models import AddcatDb,AddproDb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Frontend.models import ContactDb

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index_page(request):
    return render(request, "index.html")
def addcat_page(request):
    return render(request, "addcategory.html")
def Cat_save(request):
    if request.method == "POST":
        a = request.POST.get('cat_name')
        b = request.POST.get('des')
        c = request.FILES['cat_image']
        obj = AddcatDb(CategoryName=a,Description=b,Categoryimage=c)
        obj.save()
        messages.success(request,"Category Saved Succesfully ")
        return redirect(addcat_page)

def Cat_display(request):
    catsave=AddcatDb.objects.all()
    return render(request, "disp_category.html",{'catsave':catsave})

def Cat_edit(request,c_id):
    cateditt = AddcatDb.objects.get(id=c_id)
    return render(request, "edit_category.html", {'cateditt': cateditt})

def cat_update(request,c_id):
    if request.method=="POST":
        a = request.POST.get('cat_name')
        b = request.POST.get('des')
        try:
            c = request.FILES['cat_image']
            fs = FileSystemStorage()
            file = fs.save(c.name, c)
        except MultiValueDictKeyError:
            file = AddcatDb.objects.get(id=c_id).Categoryimage
        AddcatDb.objects.filter(id=c_id).update(CategoryName=a,Description=b,Categoryimage=file)
        return redirect(Cat_display)

def cat_delete(request, c_id):
    delcat = AddcatDb.objects.filter(id=c_id)
    delcat.delete()
    return redirect(Cat_display)

#PRODUCT

def addproduct_page(request):
    cat = AddcatDb.objects.all()
    return render(request, "add_product.html", {'cat': cat})

def product_save(request):
    if request.method == "POST":
        e = request.POST.get('cate')
        f = request.POST.get('pro_name')
        g = request.POST.get('price')
        h = request.POST.get('desc')
        i = request.FILES['pro_image']
        obj = AddproDb(Category=e,Product_Name=f,Price=g,Description=h,Product_image=i)
        obj.save()
        messages.success(request, "Product Saved Succesfully ")
        return redirect(addproduct_page)

def Product_display(request):
    pro = AddproDb.objects.all()
    return render(request,"disp_product.html",{'pro':pro})

def pro_edit(request,p_id):
    cat = AddcatDb.objects.all()
    prod= AddproDb.objects.get(id=p_id)
    return render(request,"edit_product.html",{'prod':prod,'cat':cat})

def pro_update(request,p_id):
    if request.method=="POST":
        e = request.POST.get('cate')
        f = request.POST.get('pro_name')
        g = request.POST.get('price')
        h = request.POST.get('desc')
        try:
            i = request.FILES['pro_image']
            fs = FileSystemStorage()
            file = fs.save(i.name, i)
        except MultiValueDictKeyError:
            file = AddproDb.objects.get(id=p_id).Product_image
        AddproDb.objects.filter(id=p_id).update(Category=e,Product_Name=f,Price=g,Description=h,Product_image=file)
        return redirect(Product_display)



def pro_delete(request, p_id):
    delpro = AddproDb.objects.filter(id=p_id)
    delpro.delete()
    return redirect(Product_display)

#ADMIN

def admin_login_page(request):
    return render(request,"admin_login.html")

def admin_save(request):
    if request.method=='POST':
        un = request.POST.get('uname')
        pd = request.POST.get('pwd')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pd)
            if x is not None:
                messages.success(request,"Login Succesfull!!")
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pd
                return redirect(index_page)
            else:
                messages.error(request,"Ivalid Username/Password!!")
                return redirect(admin_login_page)
        else:
            messages.error(request,"Invalid Username/Password!!")
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def display_contact(request):
    dis_con = ContactDb.objects.all()
    return render(request,"disp_contact.html",{'dis_con':dis_con})

def delete_contact(request,d_id):
    del_con = ContactDb.objects.filter(id=d_id)
    del_con.delete()
    return redirect(display_contact)