from django import forms

from .models import Post, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
    
class CvForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ()
    class personalDetails(forms.ModelForm):
        class Meta:
            model = CV
            fields = ('name','address', 'phone_number', 'email', 'objective', 'skills', 'interests')
    class experience(forms.ModelForm):
        class Meta:
            model = CV.new_experience(CV)
            fields = ('job_title','company','start_year','end_year', 'job_description')
    class education(forms.ModelForm):
        class Meta:
            model = CV.education
            fields = ('program','insitution','start_year_ed','end_year_ed','education_description')
    class other(forms.ModelForm):
        class Meta:
            model = CV
            fields = ('involvement','awards')
    class references(forms.ModelForm):
        class Meta:
            model = CV.references
            fields = ('ref_name', 'ref_position','ref_company','ref_contact')
    