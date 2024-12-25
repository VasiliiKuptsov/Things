
from django.urls import path
#from catalog.apps import NewappConfig
#from catalog.views import home
from . import views

#app_name = NewappConfig.name
app_name = "catalog"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]