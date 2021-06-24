from django import forms
from django.forms.fields import FileField
from .models import Properties,Agents
from django.contrib.auth.models import User,auth
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import UserCreationForm

class registerform(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
   

    def __init__(self,*args,**kwargs):
        super(registerform,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class CreateForm(forms.ModelForm):
    class Meta:
        model= Properties
        fields=['title','slug','content','price','address','address2','bath','bed','area','status','prop_type','pincode','city']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
           # 'agent':forms.Select(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'address2':forms.TextInput(attrs={'class':'form-control'}),
            'bath':forms.TextInput(attrs={'class':'form-control'}),
            'bed':forms.TextInput(attrs={'class':'form-control'}),
            'area':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
            'prop_type':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            
               # 'agent' : User.objects.get(pk=request.user.id),
          
       # 'floorplan': forms.ImageField()

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model= Properties
        fields=['title','content','price','address','address2','bath','bed','area','status','prop_type','pincode','city','sliderimg','floorplan','image']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'address2':forms.TextInput(attrs={'class':'form-control'}),
            'bath':forms.TextInput(attrs={'class':'form-control'}),
            'bed':forms.TextInput(attrs={'class':'form-control'}),
            'area':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
            'prop_type':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),

        }


# class agentdetials(forms.ModelForm):

#     class Meta:
#         model=Agents
#         fields= ['phone','image']

#         widgets={
#            # phone:forms.IntegerField(attrs={'class':'form-control'}),
#             image:forms.ImageField()
#         }
