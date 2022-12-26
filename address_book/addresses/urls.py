from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_address', views.add_address, name='add_address'),
    path('list_address', views.list_address, name='list_address'),
    path('show_address/<address_id>', views.show_address, name='show_address'),
    path('update_address/<address_id>', views.update_address, name='update_address'),
]
