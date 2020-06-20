from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, CV
from django.utils import timezone
from .forms import PostForm, CvForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form': form })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def cv(request):
    cv_view = CV.objects.order_by('name')
    return render(request,'blog/cv.html',{'cv_view':cv_view})

def new_cv(request):      
    if request.method == "POST":
        cv_base = CvForm(request.POST)
        cv_personal_details = CvForm.personalDetails(request.POST)
        cv_experience = CvForm.experience(request.POST)
        cv_education = CvForm.education(request.POST)
        cv_other = CvForm.other(request.POST)
        cv_references = CvForm.references(request.POST)

        #full_form = [cv_personal_details, cv_experience, cv_education, cv_other,cv_references]           
        if cv_base.is_valid() & cv_personal_details.is_valid() & cv_experience.is_valid() &cv_education.is_valid() & cv_other.is_valid() & cv_references.is_valid():
            
            post_base = cv_base.save(commit=False)
            post_personal = cv_personal_details.save(commit = False)
            post_experience = cv_experience.save(commit=False)
            post_education = cv_education.save(commit=False)
            post_other = cv_other.save(commit=False)
            post_references = cv_references.save(commit=False)
          
            post_base.save()
            post_personal.save()
            post_experience.save()
            post_education.save()
            post_other.save()
            post_references.save()
            return redirect('cv_detail',pk = post_base.pk )
        else:
            print('invalid cv')
            print(cv_personal_details.errors.as_data())
    else:
        cv_base = CvForm()
        cv_personal_details = CvForm.personalDetails()
        cv_experience = CvForm.experience()
        cv_education = CvForm.education()
        cv_other = CvForm.other()
        cv_references = CvForm.references()
            
    return render(request, 'blog/new_cv.html', {'form_base':cv_base,'form_personal_details': cv_personal_details, 'form_experience':cv_experience, 'form_education':cv_education, 'form_other':cv_other, 'form_references':cv_references})

def new_cv_experience(request):
    cv = CvForm.experience()
    return render(request, 'blog/new_cv_experience.html', {'form': cv})

def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    cv.experience = get_object_or_404(CV.experience, pk=pk)
    cv.education = get_object_or_404(CV.education, pk=pk)
    cv_references = get_object_or_404(CV.references, pk=pk)
    return render(request, 'blog/cv_detail.html',{'cv': cv,'cv.experience':cv.experience,'cv.education':cv.education,'cv.references':cv_references})