
from django.shortcuts import render,redirect
from Backend.models import AddproDb,AddcatDb
from Frontend.models import ContactDb,RegistrationDb,CartDb,CheckoutDb

from django.contrib import messages
# Create your views here.

def home_page(request):
    pro= AddproDb.objects.all()
    cat= AddcatDb.objects.all()
    return render(request,"home.html" ,{'pro':pro ,'cat':cat})

def product_page(request,cate):
    prod=AddproDb.objects.filter(Category=cate)
    return render(request,"product.html",{'prod':prod})

def about_page(request):
    return render(request,"about.html")

def singleproduct_page(request,pro_id):
    proo=AddproDb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'proo':proo})
def contact_page(request):
    return render(request,"contact.html")

def contact_save(request):
    if request.method == "POST":
        n = request.POST.get('nm')
        e = request.POST.get('em')
        s = request.POST.get('sub')
        m = request.POST.get('msg')
        obj = ContactDb(Name=n,Email=e,Subject=s,Message=m)
        obj.save()
        return redirect(contact_page)

def sign_in_up_page(request):
    return render(request,"signinup.html")

def sign_save(request):
    if request.method == "POST":
        ab = request.POST.get('uname')
        bc = request.POST.get('mail')
        cd = request.POST.get('pass')
        obj = RegistrationDb(Username=ab,Email=bc,Password=cd)
        obj.save()
        return redirect(sign_in_up_page)

def signup(request):
    if request.method == "POST":
        ur = request.POST.get('uname')
        pd = request.POST.get('pass')
        em = request.POST.get('mail')
        if RegistrationDb.objects.filter(Username=ur,Password=pd).exists():
            request.session['Username'] = ur
            request.session['Password'] = pd
            request.session['Email'] = em
            return redirect(home_page)
        else:
            return redirect(sign_in_up_page)
    else:
        return redirect(sign_in_up_page)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(sign_in_up_page)

def blog_page(request):
    return render(request,"blog.html")

def cart(request):
    if request.method == "POST":
        a = request.POST.get('un')
        b = request.POST.get('pn')
        c = request.POST.get('qn')
        d = request.POST.get('prn')
        e = request.POST.get('tn')
        obj = CartDb(Username=a,Productname=b,Quantity=c,Sing_price=d,Price=e)
        obj.save()
        messages.success(request, "Product Saved Succesfully ")
        return redirect(home_page)

def cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Username'])
    total=0
    for i in data:
        total=total+i.Price
    return render(request,"cart.html",{'data':data,'total':total})

def cart_delete(request,p_id):
    delcat = CartDb.objects.filter(id=p_id)
    delcat.delete()
    return redirect(cart_page)

def checkout_page(request):
    data = CartDb.objects.filter(Username=request.session['Username'])
    total = 0
    for i in data:
        total = total + i.Price
    return render(request, "checkout.html", {'data': data, 'total': total})


def checkout_save(request):
    if request.method == "POST":
        n = request.POST.get('fs')
        e = request.POST.get('ls')
        s = request.POST.get('st')
        o = request.POST.get('ad')
        p = request.POST.get('tc')
        q = request.POST.get('zi')
        r = request.POST.get('ph')
        m = request.POST.get('em')
        obj = CheckoutDb(Firstname=n,Lastname=e,State=s,Address=o,Town=p,Postcode=q,Phonenum=r,Email=m)
        obj.save()
        return redirect(checkout_page)