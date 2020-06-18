from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv', views.cv, name="cv"),
    path('new_cv', views.new_cv, name="new_cv"),
    path('new_cv_experience', views.new_cv_experience, name="new_cv_experience"),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),
]