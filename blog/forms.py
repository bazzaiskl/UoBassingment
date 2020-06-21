from django import forms

from .models import Post, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
    
class CvForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('name','address', 'phone_number', 'email', 'objective', 'skills', 'interests',
        'job_title','company','start_year','end_year', 'job_description',
        'program','insitution','start_year_ed','end_year_ed','education_description',
        'involvement','awards',
        'ref_name', 'ref_position','ref_company','ref_contact')