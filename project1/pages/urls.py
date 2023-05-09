
from django.urls import path
from pages import views

urlpatterns = [
    path('',views.sample,name="normal_route"),
    path('rout/<name>',views.sample1,name='dynamic_rote'),
    path('temp/',views.sample2,name='tr'),
    path('temp1/<name>', views.sample3, name='cp'),
    path('temp2/', views.sample4, name='cp1'),
    path('temp3/', views.sample5, name='cp2'),
    path('redirect/', views.sample6, name='rd'),
    path('temp4/',views.sample7,name='ti'),
    path('stat/',views.sample8,name='si'),
    path('reg/',views.register,name='uc'),



]
