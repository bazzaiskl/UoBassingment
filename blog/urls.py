from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    #posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/',views.post_delete, name="post_delete"),

    #cv
    path('cv/', views.cv, name="cv"),
    path('new_cv/', views.new_cv, name="new_cv"),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),
    path('cv/<int:pk>/edit/', views.cv_edit,name='cv_edit'),
    path('cv/<int:pk>/delete/', views.cv_delete, name="cv_delete"),

    #other
    path ('signup/',views.SignUp, name = 'signup'),
    
    

]