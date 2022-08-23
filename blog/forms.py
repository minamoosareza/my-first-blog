from django import forms
from django.utils.safestring import mark_safe
from .models import Signup, Contact

"""class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)"""
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('name', 'phone', 'email')
        labels ={'name': "نام و نام خانوادگی",'email': "پست الکترونیکی  ", 'phone': "شماره تلفن همراه"}
		
class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['name'].widget.attrs['placeholder'] = "نام و نام خانوادگی"
        self.fields['email'].widget.attrs['placeholder'] = "ایمیل"
        self.fields['message'].widget.attrs['placeholder'] = "پیام"
        self.fields['message'].widget.attrs['rows'] = 5
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        labels ={'name': "",'email':"", 'message': ""}
        
	
#class ContactForm(forms.Form):
 #   name = forms.CharField(max_length=50, label=u"نام و نام خانوادگی")
  #  email = forms.EmailField(max_length=50, label=u" پست الکترونیکی ")
   # message = forms.CharField(widget=forms.Textarea, label=u"پیام")