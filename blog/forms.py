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
>>>>>>> parent of 4697e5c... error where form is invalid
