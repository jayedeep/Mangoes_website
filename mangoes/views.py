from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from .models import CustomUser,Mango_For_Sell,Mangoes_For_Buy,Deliver
from .forms import LoginForm, RegisterForm,UpdateForm,Mangoes_for_sell_form,Mangoes_for_buy_form,Delivery_form
from django.contrib.auth import login,logout,authenticate
from geopy.geocoders import Nominatim
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import UserFilter

from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


def home(request):
    mangoes_for_sell=Mango_For_Sell.objects.all()
    user_filter = UserFilter(request.GET, queryset=mangoes_for_sell)
    print("first",user_filter)
    if request.user.is_authenticated:
        messages.info(request, 'Welcome Back To Home!')
    
    return render(request,'mangoes/index.html',{"filter":user_filter})

@login_required
def profile(request):

    if request.method=="POST":
        form2=UpdateForm(request.POST or None,request.FILES or None,instance=request.user)
        if form2.is_valid():
            form2.save()
            messages.success(request, 'successfully updated profile')

            return redirect('profile')
        else:
            form2 = UpdateForm(instance=request.user)
            messages.error(request, 'sorry! there is error something! Try Again')
            return render(request,'mangoes/profile.html',{"form2":form2})
    else:
        form2 = UpdateForm(instance=request.user)
        messages.info(request,"update Your profile!")
        return render(request, 'mangoes/profile.html', {"form2": form2})
    return render(request, 'mangoes/profile.html', {"form2": form2})


def signup(request):

    if request.method=="POST":
        forms=RegisterForm(request.POST)
        if forms.is_valid():
            first_name=forms.cleaned_data['first_name']
            last_name=forms.cleaned_data['last_name']
            password1=forms.cleaned_data['password1']
            password2= forms.cleaned_data['password2']
            username=first_name
            email = forms.cleaned_data['email']
            farm_name=forms.cleaned_data['farm_name']
            address=forms.cleaned_data['address']
            contact=forms.cleaned_data['contact']

            if password1==password2:
                user=CustomUser.objects.create_user(username=username,farm_name=farm_name,email=email,password=password1,contact=contact,first_name=first_name,last_name=last_name,address=address)
                user.save()
                htmly = get_template('registration/email.html') 
                d = { 'username': username } 
                subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
                html_content = htmly.render(d) 
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
                msg.attach_alternative(html_content, "text / html") 
                msg.send() 
                messages.success(request,"our account has been created ! You are now able to log in")
                return redirect('login')
            else:
                messages.error(request,"please Enter Valid password")
                return render(request,'mangoes/register.html',{"forms":forms})
        else:
            forms = RegisterForm()
            messages.error(request,"please check your credential")

            return render(request,'mangoes/register.html',{"forms":forms})
    else:
        forms = RegisterForm()
        messages.info(request,"please create your account")

        return render(request, 'mangoes/register.html', {"forms": forms})
    return render(request, 'mangoes/register.html', {"forms": forms})

def Login(request):
    if request.method=="POST":
        forms=LoginForm(request.POST)
        print(forms.data)
        if forms.is_valid():
            password=forms.cleaned_data['password']
            username=forms.cleaned_data['username']

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Welcome back! "+request.user.username,)
                return redirect('index')
            else:
                print('user is none')
                messages.error(request,'user is None,Try Again')
                return redirect('login')
        else:
            messages.error(request,'Please enter valid data')            
            return render(request, 'mangoes/login.html', {"forms": forms})
    else:
        forms=LoginForm()
        messages.info(request,'Please Login to use this website!')
        return render(request, 'mangoes/login.html', {"forms": forms})
    return render(request, 'mangoes/login.html', {"forms": forms})

def Logout(request):
    messages.success(request,"You Successfully logged out!")
    logout(request)
    return render(request,'mangoes/index.html')

def list_to_buy(request):
    mangoes_for_sell=Mango_For_Sell.objects.all()
    user_filter = UserFilter(request.GET, queryset=mangoes_for_sell)
    messages.info(request,"Enjoy Products and Buy what you want!")
    print(user_filter)
    return render(request,'mangoes/list_to_buy.html',{'filter':user_filter})

@login_required
def sell(request):
    
    if request.method=='POST':
        forms=Mangoes_for_sell_form(request.POST,request.FILES,)
        # print(forms.data)
        if forms.is_valid():
            # owner=request.user.username
            # Type_Of_Mango=forms.cleaned_data['Type_Of_Mango']
            # weigth=forms.cleaned_data['weigth']
            # ripe=forms.cleaned_data['ripe']
            # pkgd_at=forms.cleaned_data['pkgd_at']
            # photo1=forms.cleaned_data['photo1']
            # photo2=forms.cleaned_data['photo2']
            # photo3=forms.cleaned_data['photo3']
            # photo4=forms.cleaned_data['photo4']
            # photo5=forms.cleaned_data['photo5']
            # photo6=forms.cleaned_data['photo6']
            # price=forms.cleaned_data['price']
            # total_boxes=forms.cleaned_data['total_boxes']
            # limit=forms.cleaned_data['limit']
            # discount=forms.cleaned_data['discount']
            
            # mango=Mango_For_Sell.objects.create(owner=owner,Type_Of_Mango=Type_Of_Mango,weigth=weigth,ripe=ripe,pkgd_at=pkgd_at,photo1=photo1,photo2=photo2,photo3=photo3,photo4=photo4,photo5=photo5,photo6=photo6,price=price,total_boxes=total_boxes,limit=limit,discount=discount)
            # mango.save()
            # print("success")
            messages.success(request,"You successfully created Your Sale.")
            forms.save()
            return redirect("my_sells")
        else:
            messages.error(request,"There is error in the Form,Please Try Again!")
            forms=Mangoes_for_sell_form()
            return render(request,'mangoes/sell.html',{'forms':Mangoes_for_sell_form})
    else:
        forms=Mangoes_for_sell_form()
        messages.success(request,'Sell Your Products!')
        return render(request,'mangoes/sell.html',{'forms':Mangoes_for_sell_form})
    return render(request,'mangoes/sell.html',{'forms':Mangoes_for_sell_form})

@login_required
def single_page(request,id):
    messages.info(request,"Product You May Like Buy")
    single=Mango_For_Sell.objects.get(id=id)
    locator = Nominatim(user_agent="myGeocoder")
    # print(single.owner.address)
    location = locator.geocode(single.owner.address)
    print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
    return render(request,'mangoes/single_page.html',{'single':single,"Latitude":location.latitude,"Longitude":location.longitude})

@login_required
def my_sells(request):
    messages.info(request,"Your Sales History")
    user=CustomUser.objects.get(id=request.user.id)
    user_sells=Mango_For_Sell.objects.filter(owner=request.user).order_by('-pkgd_at')
    return render(request,'mangoes/my_sells.html',{"user":user,'user_sells':user_sells})

@login_required
def update_product(request,id):
    current=get_object_or_404(Mango_For_Sell,id=id)
    # print(current)
    if request.method=='POST':
        forms=Mangoes_for_sell_form(request.POST or None,request.FILES or None,instance=current)
        print(forms.data,forms.files)
        if forms.is_valid():
            forms.save()
            messages.success(request,"successfully updated Product")
            return redirect("index")
        else:
            messages.error(request,"please Enter Valid Data")
            forms=Mangoes_for_sell_form(instance=current)
            return render(request,'mangoes/update_product.html',{'forms':forms,'current':current})
    else:
        forms=Mangoes_for_sell_form(instance=current)
        messages.info(request,"You may want to update Your Product Content!")
        return render(request,'mangoes/update_product.html',{'forms':forms,'current':current})
    return render(request,'mangoes/update_product.html',{'current':current})
@login_required
def delete_product(request,id):
    messages.success(request,"You deleted successfully")
    current=get_object_or_404(Mango_For_Sell,id=id)
    current.delete()
    return redirect('my_sells')

@login_required
def my_buys(request):
    messages.info(request,"Products You brought till Now")
    users=CustomUser.objects.get(id=request.user.id)
    user_buys=Mangoes_For_Buy.objects.filter(owner=request.user).order_by('-created_at')
    return render(request,'mangoes/my_buys.html',{'user_buy':user_buys,'users' :users})
@login_required
def single_buy(request,id):
    messages.success(request,"Your Product was..")
    single=Mangoes_For_Buy.objects.get(id=id)
    return render(request,'mangoes/single_buy.html',{'single':single})
    # return render(request,'mangoes/single_buy.html')

@login_required
def create_for_buy(request,id):
    # forms=Mangoes_for_buy_form()
    
    single=Mango_For_Sell.objects.get(id=id) #mango owner of this product
    if request.method=="POST":
        
        forms=Mangoes_for_buy_form(request.POST)
        print(forms.data)
        if forms.is_valid():
            print("ok")
            forms.save()
            return redirect("my_buys")
        else:
            print("invalid data")
            forms=Mangoes_for_buy_form()

            return render(request,'mangoes/create_for_buy.html',{"forms":forms,'single':single})
    else:
        forms=Mangoes_for_buy_form()
        return render(request,'mangoes/create_for_buy.html',{"forms":forms,'single':single})
    return render(request,'mangoes/create_for_buy.html',{"forms":forms,'single':single})


def delivery_for_salers(request):
    deliveries=Deliver.objects.filter(owner_of_product__owner=request.user)
    # print(deliveries)
    return render(request,'mangoes/delivery_list.html',{'deliveries':deliveries})

def change_delivery(request,id):
    current=Mangoes_For_Buy.objects.get(id=id)
    deliveries=Deliver.objects.get(product=current)

    if request.method=='POST':
        forms=Delivery_form(request.POST,instance=deliveries)
        print(forms.data,forms.files)
        if forms.is_valid():
            
            forms.save()
            messages.success(request,"successfully updated Product")
            return redirect("delivery_for_sales")
        else:
            messages.error(request,"please Enter Valid Data")
            forms=Delivery_form(instance=deliveries)
            return render(request,'mangoes/update_delivery.html',{'forms':forms,'current':current,'deliveries':deliveries})
    else:
        forms=Delivery_form(instance=deliveries)
        messages.info(request,"You may want to update Your Product Content!")
        return render(request,'mangoes/update_delivery.html',{'forms':forms,'current':current,'deliveries':deliveries})
    return render(request,'mangoes/update_delivery.html',{'current':current,'deliveries':deliveries})



def html_to_pdf_view(request,id):
    current=Mangoes_For_Buy.objects.get(id=id)
    deliveries=Deliver.objects.get(product=current)
    html_string = render_to_string('mangoes/pdf_template.html', {'current':current,'deliveries':deliveries })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return redirect('delivery_for_sales')