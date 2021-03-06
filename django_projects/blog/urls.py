from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',PostListView.as_view(),name="blog_home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post_detail"),
    path('post/new/',PostCreateView.as_view(),name="post_create"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post_update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post_delete"),
    path('about/',views.about,name="blog_about"),
    path('register/',user_views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/pass_reset.html'),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/pass_reset_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/pass_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/pass_reset_comp.html'),name="password_reset_complete"),
    path('profile/',user_views.profile,name="profile"),
]
