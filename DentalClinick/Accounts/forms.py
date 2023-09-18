from django import forms
from .models import UserAdmin,AddDr,AddWork,UserContact,HomeInfo
from django.contrib.auth.forms import UserCreationForm

from django.forms import formset_factory

class DateInput(forms.DateInput):
    input_type = 'date'

class AdminForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 20em'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 20em'})
    class Meta:
        model = UserAdmin
        fields =('fname','lname','username','email','birthdate','gender','is_admin','is_staff','password1','password2')

        widgets={
                'fname':forms.TextInput(attrs={'class':'form-control ','style':'max-width: 20em',"id":"","placeholder":""}),
                'lname':forms.TextInput(attrs={'class':'form-control','style':'max-width: 20em',"id":"","placeholder":""}),
                'email':forms.TextInput(attrs={'class':'form-control ','style':'max-width: 20em',"id":"","placeholder":""}),
                'username':forms.TextInput(attrs={'class':'form-control ','style':'max-width: 20em',"placeholder":""}),
                'birthdate':DateInput(attrs={'class':'form-control ','style':' max-width: 20em',"id":"","placeholder":"29/09/1996"}),
                'gender': forms.Select(attrs={'class':'form-control ','style':'max-width: 20em',"id":"","placeholder":""}),
                'is_admin': forms.CheckboxInput(attrs={'class':'form-check-input ','style':' margin-left:20px',"id":"","placeholder":""}),
                'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input ','style':' margin-left:20px',"id":"","placeholder":""}),
          }  
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'   
        
     
   
class AddDrForm(forms.ModelForm):
    class Meta:
            model = AddDr
            fields = ('name','job','image','time','description','name_ar_field','job_ar_field','description_ar_field','time_ar_field')
            widgets={
                'name':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'name_ar_field':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'job':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'job_ar_field':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'time_ar_field':forms.DateTimeInput(attrs={'class':'form-control','style':'width:70%'}),
                'time':forms.DateTimeInput(attrs={'class':'form-control','style':'width:70%'}),
                'image':forms.FileInput(attrs={'class':'form-control','style':'width:70%'}),
                'description':forms.Textarea(attrs={'class':'form-control','style':'width:70%'}),
                'description_ar_field':forms.Textarea(attrs={'class':'form-control','style':'width:70%'})

     }


class HomeInfoForm(forms.ModelForm):
    class Meta:
        model = HomeInfo
        fields = ('title','image','description','title_ar_field','description_ar_field')

        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
            'description':forms.Textarea(attrs={'class':'form-control','style':'width:70%'}),
            'title_ar_field':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
            'description_ar_field':forms.Textarea(attrs={'class':'form-control','style':'width:70%'}),
            'image':forms.FileInput(attrs={'class':'form-control','style':'width:70%'}),

    }



class AddWorkForm(forms.ModelForm):
    class Meta:
            model = AddWork
            fields = ('title','category','image','description','dr','title_ar_field','category_ar_field','dr_ar_field','description_ar_field')
            dr=forms.ModelChoiceField(
                     queryset=AddDr.objects.all(),
                     empty_label='Select a doctor',
                     )

            widgets={
                'title':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'title_ar_field':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'category':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'category_ar_field':forms.TextInput(attrs={'class':'form-control','style':'width:70%'}),
                'description':forms.Textarea(attrs={'class':'form-control','style':'width:70%'}),
                'description_ar_field':forms.Textarea(attrs={'class':'form-control','style':'width:70%'}),

                'image':forms.FileInput(attrs={'class':'form-control','style':'width:70%'}),
                'dr':forms.Select(attrs={'class':'form-control','style':'width:50%'}),
                'dr_ar_field':forms.Select(attrs={'class':'form-control','style':'width:50%'}),
    
     }







class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','name':'password'}))



class UserContactForm(forms.ModelForm):
    class Meta:
            model = UserContact
            fields = ('name','email','subject','description','phonenumber')
            widgets={
            'name' :forms.TextInput(attrs={'class':'form-control','style':'width:100%'}),
            'email' :forms.TextInput(attrs={'class':'form-control','style':'width:100%'}),
            'subject':forms.TextInput(attrs={'class':'form-control','style':'width:100%'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control','style':'width:100%'}),
            'description':forms.Textarea(attrs={'class':'form-control','style':'width:100%'}),
            }




