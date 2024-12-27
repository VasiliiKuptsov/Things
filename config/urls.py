
from django.contrib import admin
from django.urls import path, include
from catalog import views
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('contact/', views.contacts, name='contact'),
    #Путь напрямую с главной страницы home
    #т.к. предложенные нам страницы home и contacts одинаковые
    path('catalog/', include('catalog.urls', namespace='catalog'))
]
