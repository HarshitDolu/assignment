from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<str:pk>/',views.delete_t,name='delete'),
    path('update/<str:pk>/',views.update,name='update'),
]