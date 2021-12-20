from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'), 
    #path('login/', views.login, name='login'),
    path('select_role/', views.select_role, name='select_role'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('signup_success/', views.signup_success, name='signup_success'), 
    #path('face_login/', views.face_login, name='face_login'), 
    
    
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

