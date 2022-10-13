from django.urls import path
from .views import home_view
from app.api.views_api import delete_view, update_view

urlpatterns = [

    #### TEMPLATES
    
    path('', home_view, name='home'),

    #### APIS

    path('delete/<int:pk>', delete_view, name='delete_view'),
    path('update/<int:pk>', update_view, name='update_view'),
]