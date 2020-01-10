from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #mathiko views maa overwrite huna sakchha bhanera ( as a )  gareko


from django.conf.urls import url
# from masterdjango.news import views as news_views



urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('physicsnews',views.physicsnews,name='physicsnews'),
    path('contact',views.contact,name='contact'),
    path('download',views.download,name='download'),

    url(r'^signup/$', views.signup, name='signup'),

    path('slider/<id>',views.slider,name='slider'),
    path('photograph/<id>',views.photograph,name='photograph'),
    path('cosmology',views.cosmology,name='cosmology'),
    path('biomedical',views.biomedical,name='biomedical'),
    path('technology',views.technology,name='technology'),

    path('product-details/<slug>',views.product_details,name='product-details'),

    path('register',views.user_register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('users',views.users,name='users'),


    path('password-reset',auth_views.PasswordResetView.as_view(template_name='pages/login/password-reset.html')
         ,name='password-reset'),
    path('password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='pages/login/password-reset-confirm.html')
             ,name='password_reset_confirm'),
    path('password_reset_done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='pages/login/password_reset_done.html')
             ,name='password_reset_done'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/login/password_reset_complete.html'),
         name='password_reset_complete')

]