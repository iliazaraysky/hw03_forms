from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'about'


urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='author'),
    path('tech/', views.AboutTechView.as_view(), name='tech'),

]
