from django import forms

from .models import Post, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
    
class CvForm(forms.ModelForm):
    class personalDetails(forms.ModelForm):
        class Meta:
            model = CV
            fields = ('name','address', 'phone_number', 'email', 'objective', 'skills', 'interests')

    class experience(forms.ModelForm):
        class Meta:
            model = CV.experience
            fields = ('job_title','company','start_year','end_year', 'job_description')