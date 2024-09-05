from django.urls import path
from . import views 

urlpatterns = [

    path('user-page/', views.CreateUserPage.as_view(),name='user-page'),
    path('create-user/', views.CreateUser.as_view(),name='create-user'),
    path('update-user/<int:id>/', views.UpdateUser.as_view(),name='update-user'),
]