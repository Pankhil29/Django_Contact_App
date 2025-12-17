from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add_contact/',views.add_contact,name='add_contact'),
    path('show_contact/',views.show_contact,name='show_contact'),
    path('edit_contact/<int:pk>/',views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/',views.delete_contact,name="delete_contact"),
    path('logout/', views.logout, name='logout'),
    # path('search/',views.search,name="search")
]