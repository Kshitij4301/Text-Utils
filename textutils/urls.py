from django.contrib import admin
from django.urls import path
from . import main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.index, name='index'),
    path('analyze', main.analyze, name='analyze'),
]
