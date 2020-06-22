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
        cv = CvForm(request.POST)       
        if cv.is_valid():            
            post_cv = cv.save(commit=False)
            post_cv.username = request.user          
            post_cv.save()            
            return redirect('cv_detail',pk = post_cv.pk )
        else:
            print('invalid cv')
            print(cv.errors.as_data())
    else:
        cv = CvForm()          
    return render(request, 'blog/new_cv.html', {'form_cv':cv})

def cv_edit(request, pk):
    cv_get = get_object_or_404(CV, pk=pk)
    if request.method =="POST":
        cv = CvForm(request.POST,instance=cv_get)
        if cv.is_valid():
            post_cv = cv.save(commit=False)
            post_cv.save()
            return redirect('cv_detail', pk=cv_get.pk)
    cv = CvForm(instance=cv_get)
    return render(request, 'blog/cv_edit.html',{'form_cv':cv,'cv':cv_get})

def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, 'blog/cv_detail.html',{'cv': cv})