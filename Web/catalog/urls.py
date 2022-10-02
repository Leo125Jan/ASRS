from django.urls import path
# from catalog.views import Cover, Position, All_DATA, New_Data, Scan, Search,Logout
from catalog import views

urlpatterns = [                                            
 path('', views.Cover, name='cover'),
 path('newdata', views.New_Data, name='NewData'),
 path('productposition', views.Position, name='ProductPosition'),
 path('alldata', views.All_DATA, name='AllData'),
 path('scan', views.Scan, name='Scan'),
 path('search', views.Search, name='Search'),
 path('logout', views.Logout, name='LogOut'),
]
