from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.http import HttpResponse
import datetime 
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404, handler500


from django.http import HttpResponse


from django import forms
from .models import UserAdmin,AddDr,AddWork,UserContact,HomeInfo
from .forms import AdminForm,LoginForm,AddDrForm,AddWorkForm,UserContactForm,HomeInfoForm




def about_us(request):
    """Process images uploaded by users"""
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url
    template_name='about.html' if language_code=='en' else 'about-ar.html'
    homeinfo = HomeInfo.objects.get(pk=1)
    return render(request,template_name,{'homeinfo':homeinfo,"language_code":language_code,'home_background':home_background})



def show_dr_details(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url
    template_name='show_dr_details.html' if language_code=='en' else 'show_dr_details-ar.html'
    doctor = AddDr.objects.get(pk=pk)
    return render(request,template_name,{"doctor":doctor,"language_code":language_code,'home_background':home_background})

def show_work_details(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url
    template_name='show_work_details.html' if language_code=='en' else 'show_work_details-ar.html'
    work = AddWork.objects.get(pk=pk)
    return render(request,template_name,{"work":work,"language_code":language_code,'home_background':home_background})

@login_required(login_url='/ar/login/')
def admin_panel(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url
    template_name='admin_panel.html' if language_code=='en' else 'admin_panel-ar.html'
    return render(request,template_name,{"language_code":language_code,'home_background':home_background})

#Create an error message function
def get_error_message(request):
    password1=request.POST['password1']
    password2=request.POST['password2']
    email=request.POST['email']
    if password1!=password2:
        return "The Passwords didn't match"
    if UserAdmin.objects.filter(email=email).exists():
        return "Email already exists"




# Create your views here.

@login_required(login_url='/ar/login/')
def register_request(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='register.html' if language_code=='en' else 'register-ar.html'  
    if request.user.is_superuser or request.user.is_admin:
        if request.method=="POST":
            form=AdminForm(request.POST)
            if form.is_valid():
                user=form.save()
                
                messages.success(request,"Register successful")
                return redirect(f'/{language_code}/')


            messages.error(request,get_error_message(request))
            return render(request,template_name,context={'register_form':form,"language_code":language_code,'home_background':home_background})
        else:
            form=AdminForm()
            return render(request,template_name,context={'register_form':form,"language_code":language_code,'home_background':home_background})
    else:
        return render(request,'notallowed.html',context={"language_code":language_code,'home_background':home_background})
 

def logout_request(request):
    logout(request)
    messages.info(request,"You have sucessfully logged out")
    return redirect("login")

# Create your views here.
def login_request(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='login.html' if language_code=='en' else 'login-ar.html'  

    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)

            #username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
       
            #user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect(f'/{language_code}/')
            else:
                messages.error(request, "Invalid username and password!")
        else:
            messages.error(request, "Invalid form")

    form=LoginForm()
    return render(request,template_name,context={'login_form':form,"language_code":language_code,'home_background':home_background})

def logout_request(request):
    logout(request)
    messages.info(request,"You have sucessfully logged out")
    return redirect("login")



def home_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name='home.html' if language_code=='en' else 'home-ar.html'
    doctors=AddDr.objects.all()
    works=AddWork.objects.all()
    
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url
    print(home_background)
    return render(request,template_name,{"doctors":doctors,"works":works,"homeinfo":homeinfo,"language_code":language_code,'home_background':home_background})

def about(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    return render(request,'about.html',context={"language_code":language_code,'home_background':home_background})

def contactus(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='contact.html' if language_code=='en' else 'contact-ar.html'
    return render(request,template_name,context={"language_code":language_code,'home_background':home_background})



def contacts_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='users_data.html' if language_code=='en' else 'users_data-ar.html'
    usersdata = UserContact.objects.all().order_by('-created')
    return render(request,template_name,{"usersdata":usersdata,"language_code":language_code,'home_background':home_background})



""" Dr Partiotion """

def dr_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url   
    template_name='drs.html' if language_code=='en' else 'drs-ar.html'
    doctors=AddDr.objects.all()
    return render(request,template_name,{"doctors":doctors,"language_code":language_code,'home_background':home_background})

@login_required(login_url='/ar/login/')
def add_dr(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    if request.user.is_superuser or request.user.is_admin:
  
        template_name='add_dr.html' if language_code=='en' else 'add_dr-ar.html'
        """Process images uploaded by users"""
        form = AddDrForm()
        if request.method == 'POST':
            form = AddDrForm(request.POST, request.FILES)
            
            # Get the current instance object to display in the template
            # Check if the 'image' key exists in request.FILES
            image=request.FILES['image']
            if 'image' in request.FILES:
                image = request.FILES['image']
            
            else:
                image = None  # Set image to None if it's not in request.FILES

            img_obj = form.instance
            name=(request.POST.get('name'))
            job=(request.POST.get('job'))
            time=(request.POST.get('time'))
            description=(request.POST.get('description'))
        
            name_ar_field=(request.POST.get('name_ar_field'))
            job_ar_field=(request.POST.get('job_ar_field'))
            time_ar_field=(request.POST.get('time_ar_field'))
            description_ar_field=(request.POST.get('description_ar_field'))
                
            d = AddDr.objects.create(admin=request.user,name=name,job=job,time=time,image=image,description=description,
            name_ar_field=name_ar_field,job_ar_field=job_ar_field,time_ar_field=time_ar_field,description_ar_field=description_ar_field
            )
            return redirect(f'/{language_code}/dr_page/')
            
        else:
            form = AddDrForm()
            return render(request,template_name , {'form': form,"language_code":language_code,'home_background':home_background})
    else:
        return render(request,'notallowed.html',context={"language_code":language_code,'home_background':home_background})



@login_required(login_url='/ar/login/')
def edit_dr(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='add_dr.html' if language_code=='en' else 'add_dr-ar.html'

    if request.user.is_staff or request.user.is_superuser:
            # Retrieve the AnalysisPrices object
        drtable = AddDr.objects.get(pk=pk)  # Assuming you have only one instance
        
        # Create an instance of the form with initial values

        # Retrieve the AddDr object
        form = AddDrForm(instance=drtable)  
        if request.method == 'POST':
            # Create an instance of the form with the posted data and the instance (existing object)
            form = AddDrForm(request.POST, request.FILES, instance=drtable)

            if form.is_valid():
                # The form is valid, so save it to update the object
                form.save()
                return redirect(f'/{language_code}/dr_page/')
        else:
            # Create an instance of the form with the existing object's data
            form = AddDrForm(instance=drtable)
            return render(request,template_name,{'form':form,'home_background':home_background,"language_code":language_code})
       

        
        return render(request,template_name,{'form':form,'home_background':home_background,"language_code":language_code})
    else:
        return render(request,'notallowed.html',context={"language_code":language_code,'home_background':home_background})


@login_required(login_url='/ar/login/')
def delete_dr(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    # Retrieve the AnalysisPrices object
    drtable = AddDr.objects.get(pk=pk)  # Assuming you have only one instance
    
    drtable.delete()
    return redirect(f'/{language_code}/dr_page/')

        
""" Dr Partiotion """


""" Work Partiotion """

def work_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='work.html' if language_code=='en' else 'work-ar.html'
    works = AddWork.objects.all().order_by('-created')
    return render(request,template_name,{"works":works,"language_code":language_code,'home_background':home_background})

@login_required(login_url='/ar/login/')
def add_work(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='add_work.html' if language_code=='en' else 'add_work-ar.html'
    if request.user.is_admin or request.user.is_superuser:

        """Process images uploaded by users"""
        form = AddWorkForm()
        if request.method == 'POST':
            form = AddWorkForm(request.POST, request.FILES)
            
            # Get the current instance object to display in the template
            # Check if the 'image' key exists in request.FILES
            image=request.FILES['image']
            if 'image' in request.FILES:
                image = request.FILES['image']
       
            else:
                image = None  # Set image to None if it's not in request.FILES

            title=(request.POST.get('title'))
            category=(request.POST.get('category'))
            dr=(request.POST.get('dr'))

            title_ar_field=(request.POST.get('title_ar_field'))
            category_ar_field=(request.POST.get('category_ar_field'))
            dr_ar_field=(request.POST.get('dr_ar_field'))
            description=(request.POST.get('description'))
            description_ar_field=(request.POST.get('description_ar_field'))

            dr_instance=AddDr.objects.get(id=int(dr))
        
            
        
            d = AddWork.objects.create(dr=dr_instance,dr_ar_field=dr_instance,title=title,category=category,image=image,description=description,
            title_ar_field=title_ar_field,category_ar_field=category_ar_field,description_ar_field=description_ar_field                           
            )
            return redirect(f'/{language_code}/work_page/')
            #return render(request, 'add_work.html', {'form': form})

            
        else:
            form = AddWorkForm()
            return render(request, template_name, {'form': form,"language_code":language_code,'home_background':home_background})
    else:
        return render(request,'notallowed.html',context={"language_code":language_code,'home_background':home_background})




@login_required(login_url='/ar/login/')
def edit_work(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='add_work.html' if language_code=='en' else 'add_work-ar.html'

    if request.user.is_admin or request.user.is_superuser:
        language_code = request.path.split('/')[1]  # Extract the first part of the path
            # Retrieve the AnalysisPrices object
        worktable = AddWork.objects.get(pk=pk)  # Assuming you have only one instance
        
        # Create an instance of the form with initial values

        # Retrieve the AddDr object
        form = AddWorkForm(instance=worktable)  
        if request.method == 'POST':
            # Create an instance of the form with the posted data and the instance (existing object)
            form = AddWorkForm(request.POST, request.FILES, instance=worktable)

            if form.is_valid():
                # The form is valid, so save it to update the object
                form.save()
                return redirect(f'/{language_code}/work_page/')
        else:
            # Create an instance of the form with the existing object's data
            form = AddWorkForm(instance=worktable)
            return render(request,template_name,{'form':form,'home_background':home_background,"language_code":language_code})
        # # Create an instance of the form with initial values
 
        return render(request,template_name,{'form':form,"language_code":language_code,'home_background':home_background})
    else:
        return render(request,'notallowed.html',context={"language_code":language_code,'home_background':home_background})


@login_required(login_url='/ar/login/')
def delete_work(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    # Retrieve the AnalysisPrices object
    worktable = AddWork.objects.get(pk=pk)  # Assuming you have only one instance
    print(worktable)
    
    worktable.delete()
    print("Dr Deleted")
    return redirect(f'/{language_code}/work_page/')


""" Work Partiotion """




def user_contact(request):
    """Process images uploaded by users"""
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    template_name='contact.html' if language_code=='en' else 'contact-ar.html'    
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Valid")
            return redirect(f'/{language_code}/')
            #return render(request, 'add_user.html', {'form': form,'img_obj': img_obj})
        print("Not Valid")
        return render(request, 'contact.html', {'form': form})
        
    else:
        form = UserContactForm()
        return render(request, template_name, {'form': form,"language_code":language_code,'home_background':home_background})
    



def home_info(request):
    """Process images uploaded by users"""
    form = HomeInfoForm()
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    #load the home background
    homeinfo=HomeInfo.objects.get(id=1)  
    home_background=language_code+homeinfo.background.url    
    homeinfotable = HomeInfo.objects.get(pk=1)  # Assuming you have only one instance
    print(homeinfotable)
    # Create an instance of the form with initial values
    form = HomeInfoForm(initial={
        'title': homeinfotable.title,
        'title_ar_field': homeinfotable.title_ar_field,
        'image': homeinfotable.image.url if homeinfotable.image else '',
        'description_ar_field': homeinfotable.description_ar_field,
    })
    if request.method == 'POST':
        # Update the values of AnalysisPrices object
        homeinfotable.title = request.POST['title']
        homeinfotable.title_ar_field = request.POST['title_ar_field']
        homeinfotable.image = request.FILES['image']
        homeinfotable.description = request.POST['description']
        homeinfotable.description_ar_field = request.POST['description_ar_field']

        homeinfotable.save()
        return redirect(f'/{language_code}/')

        
    else:
        form = HomeInfoForm()
        return render(request, 'add_home_info.html', {'form': form,"language_code":language_code,'home_background':home_background})




def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)