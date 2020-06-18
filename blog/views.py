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
    return render(request,'blog/cv.html')

def new_cv(request):      
    if request.method == "POST":
        cv_personal_details = CvForm.personalDetails(request.POST)
        cv_experience = CvForm.experience(request.POST)           
        if cv_personal_details.is_valid() & cv_experience.is_valid():
            post_personal = cv_personal_details.save(commit = False)
            post_experience = cv_experience.save(commit=False)
            post_personal.save()
            post_experience.save()
            return render(request, 'blog/new_cv.html',{'form_personal_details': cv_personal_details, 'form_experience':cv_experience})
        else:
            print('invalid cv')
            print(cv_personal_details.errors.as_data())
    else:
        cv_personal_details = CvForm.personalDetails()
        cv_experience = CvForm.experience()
            
    return render(request, 'blog/new_cv.html', {'form_personal_details': cv_personal_details, 'form_experience':cv_experience})

def new_cv_experience(request):
    cv = CvForm.experience()
    return render(request, 'blog/new_cv_experience.html', {'form': cv})

