from django import forms

from .models import Post, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
    
class CvForm(forms.ModelForm):
<<<<<<< HEAD
    class Meta:
        model = CV
        fields = ('name','address', 'phone_number', 'email', 'objective', 'skills', 'interests',)
    
=======
    class personalDetails(forms.ModelForm):
        class Meta:
            model = CV
            fields = ('name','address', 'phone_number', 'email', 'objective', 'skills', 'interests')
<<<<<<< HEAD
>>>>>>> parent of 4697e5c... error where form is invalid
=======
    class experience(forms.ModelForm):
        class Meta:
            model = CV
            fields = ('job_title',)
>>>>>>> parent of 75c49f3... gonna try removin class inheritance in forms.py
