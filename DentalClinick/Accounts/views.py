from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.http import HttpResponse
import datetime 
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse


from django import forms
from .models import UserAdmin,AddDr,AddWork,UserContact,HomeInfo
from .forms import AdminForm,LoginForm,AddDrForm,AddWorkForm,UserContactForm,HomeInfoForm





def about_us(request):
    """Process images uploaded by users"""
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    homeinfo = HomeInfo.objects.get(pk=1)
    return render(request,'about.html',{'homeinfo':homeinfo,"language_code":language_code})



def show_dr_details(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name='show_dr_details.html' if language_code=='en' else 'show_dr_details.html'
    doctor = AddDr.objects.get(pk=pk)
    return render(request,template_name,{"doctor":doctor,"language_code":language_code})

def show_work_details(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name='show_work_details.html' if language_code=='en' else 'show_work_details.html'
    work = AddWork.objects.get(pk=pk)
    return render(request,template_name,{"work":work,"language_code":language_code})

@login_required(login_url='/ar/login/')
def admin_panel(request):
    return render(request,'admin_panel.html')

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
    if request.user.is_superuser or request.user.is_admin:
        if request.method=="POST":
            form=AdminForm(request.POST)
            if form.is_valid():
                user=form.save()
                print(user)
                print(request.POST)

       

                print("register successful")
                messages.success(request,"Register successful")
                return redirect(f'/{language_code}/')

                # Add the logo image to the story before the table

            #return redirect(f'/{language_code}/form_created/')
            print("unsucessful")
            messages.error(request,get_error_message(request))
            return render(request=request,template_name='register.html',context={'register_form':form,"language_code":language_code})
        else:
            form=AdminForm()
            return render(request=request,template_name='register.html',context={'register_form':form,"language_code":language_code})
    else:
        return render(request=request,template_name='notallowed.html',context={"language_code":language_code})
 

def logout_request(request):
    logout(request)
    messages.info(request,"You have sucessfully logged out")
    return redirect("login")

# Create your views here.
def login_request(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        print(request.POST)
        print(form.is_bound)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)

            #username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            print(username)
            print(password)
            #user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect(f'/{language_code}/')
            else:
                messages.error(request, "Invalid username and password!")
        else:
            messages.error(request, "Invalid form")

    form=LoginForm()
    return render(request=request,template_name='login.html',context={'login_form':form,"language_code":language_code})
    now = datetime.datetime.now()
    return HttpResponse("html")
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
    return render(request,template_name,{"doctors":doctors,"works":works,"homeinfo":homeinfo,"language_code":language_code})

def about(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    return render(request,'about.html',context={"language_code":language_code})

def contactus(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    return render(request,'contact.html',context={"language_code":language_code})



def contacts_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name='users_data.html' if language_code=='en' else 'users_data.html'
    usersdata = UserContact.objects.all().order_by('-created')
    return render(request,template_name,{"usersdata":usersdata,"language_code":language_code})



""" Dr Partiotion """

def dr_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name='drs.html' if language_code=='en' else 'drs.html'
    doctors=AddDr.objects.all()
    return render(request,template_name,{"doctors":doctors,"language_code":language_code})

@login_required(login_url='/ar/login/')
def add_dr(request):
    """Process images uploaded by users"""
    form = AddDrForm()
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    if request.method == 'POST':
        form = AddDrForm(request.POST, request.FILES)
        
        #form.save()
        # Get the current instance object to display in the template
         # Check if the 'image' key exists in request.FILES
        image=request.FILES['image']
        if 'image' in request.FILES:
            image = request.FILES['image']
            print("image")
            print(image)
        else:
            image = None  # Set image to None if it's not in request.FILES

        img_obj = form.instance
        name=(request.POST.get('name'))
        job=(request.POST.get('job'))
        time=(request.POST.get('time'))
        # image=(request.POST.get('image'))
        print(request.POST)
        #print(image)
        description=(request.POST.get('description'))
    
        d = AddDr.objects.create(admin=request.user,name=name,job=job,time=time,image=image,description=description)
        print(d)
        return redirect(f'/{language_code}/dr_page/')
        #return render(request, 'add_dr.html', {'form': form,'img_obj': img_obj})
        
    else:
        form = AddDrForm()
        return render(request, 'add_dr.html', {'form': form,"language_code":language_code})



@login_required(login_url='/ar/login/')
def edit_dr(request,pk):
    if request.user.is_staff or request.user.is_superuser:
        language_code = request.path.split('/')[1]  # Extract the first part of the path
            # Retrieve the AnalysisPrices object
        drtable = AddDr.objects.get(pk=pk)  # Assuming you have only one instance
        print(drtable)
        
        # Create an instance of the form with initial values
        form = AddDrForm(initial={
            'name': drtable.name,
            'job': drtable.job,
            'time': drtable.time,
            'image': drtable.image,
            'description': drtable.description
        })
        if request.method == 'POST':
            # Update the values of AnalysisPrices object
            drtable.name = request.POST['name']
            drtable.job = request.POST['job']
            drtable.time = request.POST['time']
            drtable.image = request.FILES['image']
            drtable.description = request.POST['description']
            drtable.save()
            #return redirect(f'/{language_code}/')
            return redirect(f'/{language_code}/dr_page/')

        
        #form=AnalysisPricesForm()
        return render(request,'add_dr.html',{'form':form})


@login_required(login_url='/ar/login/')
def delete_dr(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
        # Retrieve the AnalysisPrices object
    drtable = AddDr.objects.get(pk=pk)  # Assuming you have only one instance
    print(drtable)
    
    drtable.delete()
    print("Dr Deleted")
    return redirect(f'/{language_code}/dr_page/')

        
""" Dr Partiotion """


""" Work Partiotion """

def work_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name='work.html' if language_code=='en' else 'work.html'
    works = AddWork.objects.all().order_by('-created')
    return render(request,template_name,{"works":works,"language_code":language_code})

@login_required(login_url='/ar/login/')
def add_work(request):
    """Process images uploaded by users"""
    form = AddWorkForm()
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    if request.method == 'POST':
        form = AddWorkForm(request.POST, request.FILES)
        
        # Get the current instance object to display in the template
         # Check if the 'image' key exists in request.FILES
        image=request.FILES['image']
        if 'image' in request.FILES:
            image = request.FILES['image']
            print("image")
            print(image)
        else:
            image = None  # Set image to None if it's not in request.FILES

        img_obj = form.instance
        title=(request.POST.get('title'))
        category=(request.POST.get('category'))
        dr=(request.POST.get('dr'))
        print(type(dr))
        dr_instance=AddDr.objects.get(id=int(dr))
        print(dr_instance)
        # image=(request.POST.get('image'))
        print(request.POST)
        #print(image)
        description=(request.POST.get('description'))
    
        d = AddWork.objects.create(dr=dr_instance,title=title,category=category,image=image,description=description)
        return redirect(f'/{language_code}/work_page/')
        #return render(request, 'add_work.html', {'form': form})

        
    else:
        form = AddWorkForm()
        return render(request, 'add_work.html', {'form': form,"language_code":language_code})




@login_required(login_url='/ar/login/')
def edit_work(request,pk):
    if request.user.is_staff or request.user.is_superuser:
        language_code = request.path.split('/')[1]  # Extract the first part of the path
            # Retrieve the AnalysisPrices object
        worktable = AddWork.objects.get(pk=pk)  # Assuming you have only one instance
        print(worktable)
        
        # Create an instance of the form with initial values
        form = AddWorkForm(initial={
            'title': worktable.title,
            'category': worktable.category,
            'dr': worktable.dr,
            'image': worktable.image,
            'description': worktable.description,
            'created':worktable.created,
        })
        if request.method == 'POST':
            # Update the values of AnalysisPrices object
            worktable.title = request.POST['title']
            worktable.category = request.POST['category']
            worktable.dr = request.POST['time']
            worktable.image = request.FILES['image']
            worktable.description = request.POST['description']
            worktable.created = request.POST['created']
            worktable.save()
            return redirect(f'/{language_code}/work_page/')
            #return render(request,'add_work.html',{'form':form})
        
        
        #form=AnalysisPricesForm()
        return render(request,'add_work.html',{'form':form,"language_code":language_code})


@login_required(login_url='/ar/login/')
def delete_work(request,pk):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
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
        return render(request, 'contact.html', {'form': form,"language_code":language_code})
    



def home_info(request):
    """Process images uploaded by users"""
    form = HomeInfoForm()
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    homeinfotable = HomeInfo.objects.get(pk=1)  # Assuming you have only one instance
    print(homeinfotable)
    # Create an instance of the form with initial values
    form = HomeInfoForm(initial={
        'title': homeinfotable.title,
        'image': homeinfotable.image,
        'description': homeinfotable.description,
    })
    if request.method == 'POST':
        # Update the values of AnalysisPrices object
        homeinfotable.title = request.POST['title']
        homeinfotable.image = request.FILES['image']
        homeinfotable.description = request.POST['description']
        homeinfotable.save()
        return redirect(f'/{language_code}/')

        
    else:
        form = HomeInfoForm()
        return render(request, 'add_home_info.html', {'form': form,"language_code":language_code})