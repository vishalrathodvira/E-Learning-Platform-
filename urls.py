from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('index1', views.index1, name='index1'),
    path('<int:obj_id>', views.payment, name='payment'),

    path('signup/',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('detail/<int:obj_id>', views.detail, name='detail'),



    

]