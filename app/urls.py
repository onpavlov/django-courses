from django.urls import path
from . import views

urlpatterns = [
    path('', views.LotView.list, name='main'),
    path('lot/<int:id>/', views.LotView.detail, name='lot_detail'),
    path('register/', views.UserView.new, name='registration'),
    path('login/', views.UserView.login, name='login'),
]
